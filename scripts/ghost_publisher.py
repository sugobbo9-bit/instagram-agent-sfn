"""
ghost_publisher.py — Publica no Ghost a versao longa do mesmo tema do post do Instagram.
Autenticacao: Admin API Key (id:secret) -> JWT HS256.
Roda no GitHub Actions, no mesmo itinerario do publisher do Instagram.
"""
import os, sys, json, time
from datetime import datetime, timezone
from pathlib import Path
import jwt, requests

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
KEY    = os.environ.get("GHOST_ADMIN_API_KEY", "").strip()
SITE   = os.environ.get("GHOST_API_URL", "").strip().rstrip("/")
STATUS = os.environ.get("GHOST_STATUS", "draft").strip()   # draft | published
DRY    = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")

def log(m, lvl="INFO"):
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] {m}")
    (ROOT / "logs").mkdir(exist_ok=True)
    with open(ROOT / "logs" / "ghost.jsonl", "a") as f:
        f.write(json.dumps({"ts": ts, "level": lvl, "msg": m}) + "\n")

if not KEY or ":" not in KEY:
    print("::error::GHOST_ADMIN_API_KEY ausente ou malformada (esperado id:secret)"); sys.exit(1)
if not SITE:
    print("::error::GHOST_API_URL ausente"); sys.exit(1)

def token():
    kid, secret = KEY.split(":")
    iat = int(time.time())
    return jwt.encode(
        {"iat": iat, "exp": iat + 300, "aud": "/admin/"},
        bytes.fromhex(secret),
        algorithm="HS256",
        headers={"kid": kid, "alg": "HS256", "typ": "JWT"},
    )

def api(method, path, payload=None, **params):
    r = requests.request(
        method, f"{SITE}/ghost/api/admin/{path}",
        headers={"Authorization": f"Ghost {token()}",
                 "Accept-Version": "v5.0",
                 "Content-Type": "application/json"},
        json=payload, params=params, timeout=60)
    if r.status_code >= 400:
        raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text[:400]}")
    return r.json()

# ── Seleciona o item ───────────────────────────────────────────────
# Publica no Ghost o artigo do post que acabou de sair no Instagram.
q = json.load(open(DATA / "publishing_queue.json"))
candidatos = [i for i in q["queue"]
              if i.get("status") == "published" and not i.get("ghost_post_id")]
if not candidatos:
    log("Nenhum post do Instagram aguardando versao no Ghost."); sys.exit(0)

# Encontra o primeiro candidato que tem secao 'article'
item = None
p = None
for c in candidatos:
    _lid = c["local_id"]
    _src = ROOT / "published" / f"{_lid}.json"
    if not _src.exists():
        _src = ROOT / "content" / "approved" / f"{_lid}.json"
    if _src.exists():
        _p = json.load(open(_src))
        if _p.get("article"):
            item = c
            p = _p
            break
    log(f"{_lid} sem 'article' — pulando.", "WARN")

if item is None:
    log("Nenhum candidato com secao 'article' encontrado."); sys.exit(0)

lid = item["local_id"]
art = p.get("article")
log(f"Publicando no Ghost: {lid} — {art.get('title')}")

# ── Verifica duplicata por slug ────────────────────────────────────
slug = art["slug"]
existente = api("GET", "posts/", filter=f"slug:{slug}", fields="id,slug,status").get("posts", [])
if existente:
    log(f"Ja existe post com slug '{slug}' (id {existente[0]['id']}). Nada a fazer.", "WARN")
    item["ghost_post_id"] = existente[0]["id"]
    json.dump(q, open(DATA / "publishing_queue.json", "w"), indent=2, ensure_ascii=False)
    sys.exit(0)

payload = {"posts": [{
    "title": art["title"],
    "slug": slug,
    "html": art["html"],
    "custom_excerpt": art.get("excerpt"),
    "tags": [{"name": t} for t in art.get("tags", [])],
    "status": STATUS,
    "meta_title": art.get("meta_title") or art["title"],
    "meta_description": art.get("excerpt"),
    # nao dispara newsletter para a lista de membros
    "email_only": False,
}]}

if DRY:
    log(f"DRY_RUN — payload validado, {len(art['html'])} chars de HTML. Nao publicado.")
    sys.exit(0)

res = api("POST", "posts/", payload, source="html")
post = res["posts"][0]
log(f"Ghost OK: id={post['id']} status={post['status']} url={post.get('url')}")

item["ghost_post_id"]  = post["id"]
item["ghost_url"]      = post.get("url")
item["ghost_status"]   = post["status"]
json.dump(q, open(DATA / "publishing_queue.json", "w"), indent=2, ensure_ascii=False)

db = json.load(open(DATA / "posts_db.json"))
for row in db["posts"]:
    if row.get("local_id") == lid:
        row["ghost_post_id"] = post["id"]
        row["ghost_url"] = post.get("url")
        break
json.dump(db, open(DATA / "posts_db.json", "w"), indent=2, ensure_ascii=False)
log("Bancos atualizados.")
