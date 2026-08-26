"""
bootstrap.py — Primeira execucao no runner com rede.
Valida o token, descobre o Instagram Business Account ID, puxa o historico
da conta e estabelece os baselines por formato.
Roda no GitHub Actions (workflow_dispatch).
"""
import os, sys, json, time
from datetime import datetime, timezone
from pathlib import Path
import requests

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
B = "https://graph.facebook.com/v21.0"
TOK = os.environ.get("INSTAGRAM_ACCESS_TOKEN", "").strip()

if not TOK:
    print("::error::INSTAGRAM_ACCESS_TOKEN ausente nos Secrets"); sys.exit(1)

S = requests.Session()

def g(path, **params):
    params["access_token"] = TOK
    r = S.get(f"{B}/{path}", params=params, timeout=45)
    try: j = r.json()
    except Exception: j = {"error": {"message": r.text[:300]}}
    if "error" in j:
        raise RuntimeError(f"{path}: {j['error'].get('message')}")
    return j

def mask(s):
    return f"{s[:6]}...{s[-4:]} (len={len(s)})" if s else "(vazio)"

print("=" * 60)
print("BOOTSTRAP — Instagram Agent")
print("=" * 60)

# ── 1. Valida token ────────────────────────────────────────────────
print("\n[1] Validando token...")
dbg = g("debug_token", input_token=TOK)["data"]
exp = dbg.get("expires_at", 0)
exp_h = "nunca expira" if exp == 0 else datetime.fromtimestamp(exp, timezone.utc).isoformat()
print(f"    token         : {mask(TOK)}")
print(f"    tipo          : {dbg.get('type')}")
print(f"    valido        : {dbg.get('is_valid')}")
print(f"    expira em     : {exp_h}")
print(f"    permissoes    : {', '.join(dbg.get('scopes', [])) or '(nenhuma)'}")

need = {"instagram_basic", "pages_read_engagement"}
pub  = {"instagram_content_publish", "instagram_business_content_publish"}
have = set(dbg.get("scopes", []))
if not (need & have):
    print(f"::warning::permissoes de leitura ausentes: {need - have}")
if not (pub & have):
    print(f"::warning::sem permissao de publicacao ({' ou '.join(pub)}) — so leitura funcionara")

if exp and (exp - time.time()) < 7 * 86400:
    print("::warning::token expira em menos de 7 dias — gere um novo Long-Lived Token")

# ── 2. Descobre a conta ────────────────────────────────────────────
print("\n[2] Descobrindo Instagram Business Account...")
accounts = g("me/accounts",
    fields="id,name,instagram_business_account{id,username,name,followers_count,media_count,biography}")
pages = accounts.get("data", [])
if not pages:
    print("::error::Nenhuma Pagina do Facebook vinculada a este token."); sys.exit(1)

ig, page = None, None
for p in pages:
    if p.get("instagram_business_account"):
        ig, page = p["instagram_business_account"], p
        break

if not ig:
    print("::error::Nenhuma conta Instagram Business vinculada as Paginas.")
    for p in pages: print(f"    pagina sem IG: {p.get('name')} ({p.get('id')})")
    sys.exit(1)

print(f"    pagina FB     : {page.get('name')} ({page.get('id')})")
print(f"    instagram     : @{ig.get('username')} ({ig.get('id')})")
print(f"    seguidores    : {ig.get('followers_count')}")
print(f"    posts         : {ig.get('media_count')}")

IG_ID = ig["id"]
Path(os.environ.get("GITHUB_ENV", "/dev/null")).open("a").write(f"IG_ID={IG_ID}\n")

# ── 3. Puxa historico ──────────────────────────────────────────────
print("\n[3] Puxando historico de publicacoes...")
media, url, params = [], f"{IG_ID}/media", {
    "fields": "id,timestamp,media_type,media_product_type,caption,permalink,like_count,comments_count",
    "limit": 100}
while url and len(media) < 400:
    j = g(url, **params) if "?" not in url else S.get(url, timeout=45).json()
    media.extend(j.get("data", []))
    nxt = j.get("paging", {}).get("next")
    url, params = (nxt, {}) if nxt else (None, {})
    if url: time.sleep(0.4)
print(f"    {len(media)} publicacoes encontradas")

FMT = {"IMAGE": "static", "CAROUSEL_ALBUM": "carousel", "VIDEO": "reel"}

def fmt_of(m):
    if m.get("media_product_type") == "REELS": return "reel"
    return FMT.get(m.get("media_type"), "static")

# ── 4. Insights por post ───────────────────────────────────────────
print("\n[4] Coletando insights (pode levar alguns minutos)...")
BASE = "reach,likes,comments,shares,saved,total_interactions"
REEL = BASE + ",views,ig_reels_avg_watch_time,ig_reels_video_view_total_time"

rows, errs = [], 0
for i, m in enumerate(media):
    f = fmt_of(m)
    try:
        d = g(f"{m['id']}/insights", metric=(REEL if f == "reel" else BASE))
        ins = {x["name"]: x["values"][0]["value"] for x in d.get("data", [])}
    except Exception as e:
        errs += 1; ins = {}
    reach = ins.get("reach") or 0
    row = {
        "post_id": m["id"], "publication_date": m.get("timestamp"), "format": f,
        "topic": None, "content_pillar": None, "hook": None,
        "caption": (m.get("caption") or "")[:2000], "cta": None,
        "scientific_sources": [], "creative_files": [], "experiment_tags": ["historico_pre_agente"],
        "permalink": m.get("permalink"),
        "metrics": {"import": {"collected_at": datetime.now(timezone.utc).isoformat(), **ins,
            **({} if not reach else {
                "shares_per_reach": round(ins.get("shares", 0) / reach, 4),
                "saves_per_reach":  round(ins.get("saved", 0) / reach, 4),
                "comments_per_reach": round(ins.get("comments", 0) / reach, 4),
                "likes_per_reach":  round(ins.get("likes", 0) / reach, 4)})}},
        "performance_tier": None, "derivatives_created": [],
    }
    rows.append(row)
    if (i + 1) % 25 == 0: print(f"    {i+1}/{len(media)}...")
    time.sleep(0.25)
print(f"    concluido ({errs} sem insights — normal em posts antigos)")

# ── 5. Baselines por formato ───────────────────────────────────────
print("\n[5] Calculando baselines por formato...")
def med(v):
    v = sorted(x for x in v if x is not None)
    if not v: return None
    n = len(v)
    return round(v[n//2] if n % 2 else (v[n//2-1] + v[n//2]) / 2, 4)

baseline = {}
for f in ("reel", "carousel", "static"):
    sub = [r for r in rows if r["format"] == f and r["metrics"]["import"].get("reach")]
    m = [r["metrics"]["import"] for r in sub]
    baseline[f + "s" if f != "static" else "static"] = {
        "sample_size": len(sub),
        "median_reach": med([x.get("reach") for x in m]),
        "median_shares_per_reach": med([x.get("shares_per_reach") for x in m]),
        "median_saves_per_reach": med([x.get("saves_per_reach") for x in m]),
        "median_comments_per_reach": med([x.get("comments_per_reach") for x in m]),
    }
    b = baseline[f + "s" if f != "static" else "static"]
    print(f"    {f:9s} n={b['sample_size']:3d}  reach_mediano={b['median_reach']}")

# ── 6. Grava ───────────────────────────────────────────────────────
db = json.load(open(DATA / "posts_db.json"))
known = {p["post_id"] for p in db["posts"]}
db["posts"].extend(r for r in rows if r["post_id"] not in known)
json.dump(db, open(DATA / "posts_db.json", "w"), indent=2, ensure_ascii=False)

ph = json.load(open(DATA / "performance_history.json"))
ph["baseline"] = baseline
ph["account"] = {"ig_id": IG_ID, "username": ig.get("username"),
                 "followers_count": ig.get("followers_count"),
                 "media_count": ig.get("media_count"),
                 "bootstrapped_at": datetime.now(timezone.utc).isoformat()}
json.dump(ph, open(DATA / "performance_history.json", "w"), indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print(f"BOOTSTRAP OK — @{ig.get('username')} | {len(rows)} posts importados")
print("=" * 60)
