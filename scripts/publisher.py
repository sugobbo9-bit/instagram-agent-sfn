"""
publisher.py — Publica o proximo item aprovado da fila via Instagram Graph API.
Roda no GitHub Actions. As imagens sao servidas por raw.githubusercontent.com.
"""
import os, sys, json, time
from datetime import datetime, timezone
from pathlib import Path
import requests

ROOT = Path(__file__).parent.parent
DATA, B = ROOT / "data", "https://graph.facebook.com/v21.0"
TOK  = os.environ.get("INSTAGRAM_ACCESS_TOKEN", "").strip()
REPO = os.environ.get("GITHUB_REPOSITORY", "")
REF  = os.environ.get("GITHUB_REF_NAME", "main")
DRY  = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")

if not TOK: print("::error::INSTAGRAM_ACCESS_TOKEN ausente"); sys.exit(1)

S = requests.Session()

def g(path, **p):
    p["access_token"] = TOK
    r = S.get(f"{B}/{path}", params=p, timeout=45); j = r.json()
    if "error" in j: raise RuntimeError(f"GET {path}: {j['error'].get('message')}")
    return j

def post(path, **d):
    d["access_token"] = TOK
    r = S.post(f"{B}/{path}", data=d, timeout=90); j = r.json()
    if "error" in j: raise RuntimeError(f"POST {path}: {j['error'].get('message')}")
    return j

def raw_url(rel):
    return f"https://raw.githubusercontent.com/{REPO}/{REF}/{rel.replace(chr(92),'/')}"

def wait(cid, limit=180):
    for _ in range(limit // 5):
        st = g(cid, fields="status_code,status").get("status_code")
        if st == "FINISHED": return
        if st in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {cid}: {st} — {g(cid, fields='status').get('status')}")
        time.sleep(5)
    raise TimeoutError(f"container {cid} nao ficou pronto")

def log(m, lvl="INFO"):
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] {m}")
    (ROOT / "logs").mkdir(exist_ok=True)
    with open(ROOT / "logs" / "publisher.jsonl", "a") as f:
        f.write(json.dumps({"ts": ts, "level": lvl, "msg": m}) + "\n")

# ── Descobre a conta ───────────────────────────────────────────────
ph = json.load(open(DATA / "performance_history.json"))
IG_ID = os.environ.get("IG_ID") or (ph.get("account") or {}).get("ig_id")
if not IG_ID:
    try:
        me = g("me", fields="id,instagram_business_account{id,username}")
        if me.get("instagram_business_account"):
            IG_ID = me["instagram_business_account"]["id"]
    except Exception:
        pass
if not IG_ID:
    try:
        acc = g("me/accounts", fields="instagram_business_account{id,username}")
        for _p in acc.get("data", []):
            if _p.get("instagram_business_account"):
                IG_ID = _p["instagram_business_account"]["id"]; break
    except Exception:
        pass
if not IG_ID: print("::error::Instagram Business Account nao encontrado"); sys.exit(1)

# ── Pega o proximo da fila ─────────────────────────────────────────
qp = DATA / "publishing_queue.json"
q  = json.load(open(qp))
pend = [i for i in q["queue"] if i.get("status") == "approved"]
if not pend:
    log("Fila sem itens aprovados. Nada a publicar."); sys.exit(0)

pend.sort(key=lambda i: i.get("priority", 99))
item = pend[0]
lid  = item["local_id"]
log(f"Publicando {lid} ({item['format']}) — {item.get('topic')}")

src = ROOT / "content" / "approved" / f"{lid}.json"
if not src.exists(): print(f"::error::draft ausente: {src}"); sys.exit(1)
p = json.load(open(src))

# ── Quality gate ───────────────────────────────────────────────────
sys.path.insert(0, str(ROOT / "scripts"))
from quality_gate import run_gate
ok, fails = run_gate(p)
if not ok:
    log(f"Quality gate REPROVOU {lid}: {fails}", "ERROR")
    item["status"] = "quality_gate_failed"; item["quality_failures"] = fails
    json.dump(q, open(qp, "w"), indent=2, ensure_ascii=False); sys.exit(1)
log("Quality gate aprovado.")

# ── Monta URLs publicas ────────────────────────────────────────────
files = [str(Path(f).relative_to(ROOT)) if str(f).startswith(str(ROOT)) else f
         for f in p.get("creative_files", [])]
files = [f if not f.startswith("/") else f.split("Instagram Agent/")[-1] for f in files]
urls  = [raw_url(f) for f in sorted(files)]
log(f"{len(urls)} imagens: {urls[0] if urls else '(nenhuma)'}")

for u in urls:
    h = S.head(u, timeout=30, allow_redirects=True)
    if h.status_code != 200:
        print(f"::error::imagem inacessivel ({h.status_code}): {u}"); sys.exit(1)
log("Todas as imagens acessiveis publicamente.")

if DRY:
    log("DRY_RUN ativo — parando antes de publicar."); sys.exit(0)

# ── Publica ────────────────────────────────────────────────────────
cap = p.get("caption", "")
try:
    if p["format"] == "carousel":
        kids = []
        for u in urls:
            kids.append(post(f"{IG_ID}/media", image_url=u, is_carousel_item="true")["id"])
            time.sleep(1)
        log(f"{len(kids)} containers filhos criados.")
        cid = post(f"{IG_ID}/media", media_type="CAROUSEL",
                   children=",".join(kids), caption=cap)["id"]
    elif p["format"] == "static":
        cid = post(f"{IG_ID}/media", image_url=urls[0], caption=cap)["id"]
    elif p["format"] == "reel":
        cid = post(f"{IG_ID}/media", media_type="REELS",
                   video_url=raw_url(p["video_file"]), caption=cap, share_to_feed="true")["id"]
    else:
        raise RuntimeError(f"formato desconhecido: {p['format']}")

    wait(cid)
    res = post(f"{IG_ID}/media_publish", creation_id=cid)
    pid = res["id"]
    log(f"PUBLICADO: {lid} -> media_id {pid}")
except Exception as e:
    log(f"FALHA ao publicar {lid}: {e}", "ERROR")
    item["status"] = "publish_failed"; item["error"] = str(e)
    item["failed_at"] = datetime.now(timezone.utc).isoformat()
    json.dump(q, open(qp, "w"), indent=2, ensure_ascii=False)
    sys.exit(1)

# ── Registra ───────────────────────────────────────────────────────
now = datetime.now(timezone.utc).isoformat()
item.update(status="published", published_at=now, post_id=pid)
json.dump(q, open(qp, "w"), indent=2, ensure_ascii=False)

db = json.load(open(DATA / "posts_db.json"))
db["posts"].append({
    "post_id": pid, "local_id": lid, "publication_date": now,
    "format": p["format"], "topic": p.get("topic"), "content_pillar": p.get("content_pillar"),
    "hook": p.get("hook"), "caption": cap, "cta": p.get("cta"),
    "scientific_sources": p.get("scientific_sources", []),
    "creative_files": files, "experiment_tags": p.get("experiment_tags", []),
    "metrics": {}, "performance_tier": None, "derivatives_created": [],
})
json.dump(db, open(DATA / "posts_db.json", "w"), indent=2, ensure_ascii=False)

(ROOT / "published").mkdir(exist_ok=True)
p.update(post_id=pid, published_at=now, status="published")
json.dump(p, open(ROOT / "published" / f"{lid}.json", "w"), indent=2, ensure_ascii=False)
log("Banco de dados atualizado.")
