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
if SITE and not SITE.startswith(("http://", "https://")):
    SITE = "https://" + SITE
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
        raise RuntimeError(f"{method} {path} -> HTTP {r.status_code}: {r.text[:300]}")
    return r.json()

def upload_image(path: Path, alt: str = "") -> str | None:
    """Sobe a capa para o Ghost e devolve a URL publica."""
    if not path.exists():
        log(f"capa nao encontrada: {path}", "WARN"); return None
    with open(path, "rb") as fh:
        r = requests.post(
            f"{SITE}/ghost/api/admin/images/upload/",
            headers={"Authorization": f"Ghost {token()}", "Accept-Version": "v5.0"},
            files={"file": (path.name, fh, "image/png")},
            data={"purpose": "image", "ref": path.name},
            timeout=90)
    if r.status_code >= 400:
        log(f"falha no upload da capa: HTTP {r.status_code} {r.text[:200]}", "WARN"); return None
    url = r.json()["images"][0]["url"]
    log(f"capa enviada: {url}")
    return url


# ── Seleciona o item ───────────────────────────────────────────────
# Publica no Ghost o artigo do post que acabou de sair no Instagram.
q = json.load(open(DATA / "publishing_queue.json"))
alvo = [i for i in q["queue"]
        if i.get("status") == "published"
        and (not i.get("ghost_post_id") or i.get("ghost_status") != "published")]
if not alvo:
    log("Nenhum post do Instagram aguardando versao no Ghost."); sys.exit(0)

item = alvo[0]
lid  = item["local_id"]
src  = ROOT / "published" / f"{lid}.json"
if not src.exists():
    src = ROOT / "content" / "approved" / f"{lid}.json"
p = json.load(open(src))

art = p.get("article")
if not art:
    log(f"{lid} nao tem secao 'article' — nada a publicar no Ghost.", "WARN"); sys.exit(0)

log(f"Publicando no Ghost: {lid} — {art.get('title')}")

# ── Diagnostico de credenciais ─────────────────────────────────────
kid, _, sec = KEY.partition(":")
log(f"site_host={SITE.split('//')[-1].split('/')[0]} | kid_len={len(kid)} | secret_len={len(sec)}")
if len(kid) != 24:
    log(f"AVISO: o id da chave costuma ter 24 chars hex, este tem {len(kid)}", "WARN")
try:
    int(sec, 16)
except ValueError:
    log("ERRO: a parte apos ':' nao e hexadecimal — provavelmente e a Content API Key, "
        "nao a Admin API Key", "ERROR")
    print("::error::Chave invalida: use a Admin API Key (formato id:secret hex)")
    sys.exit(1)

try:
    site = api("GET", "site/")["site"]
    log(f"autenticado no Ghost — site: {site.get('title')} (v{site.get('version')})")
except Exception as e:
    log(f"FALHA de autenticacao no Ghost: {e}", "ERROR")
    print(f"::error::{e}")
    sys.exit(1)

# ── Verifica duplicata por slug ────────────────────────────────────
slug = art["slug"]
try:
    existente = api("GET", "posts/", filter=f"slug:{slug}", fields="id,slug,status").get("posts", [])
except Exception as e:
    log(f"FALHA ao checar slug: {e}", "ERROR"); print(f"::error::{e}"); sys.exit(1)
ATUALIZAR = None
if existente:
    ATUALIZAR = existente[0]
    log(f"Post ja existe (id {ATUALIZAR['id']}, status {ATUALIZAR['status']}) — sera atualizado.")

cover_url = None
if art.get("cover"):
    cover_url = upload_image(ROOT / art["cover"], art.get("cover_alt", ""))

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
    **({"feature_image": cover_url,
        "feature_image_alt": art.get("cover_alt", "")[:125]} if cover_url else {}),
}]}

if DRY:
    log(f"DRY_RUN — payload validado, {len(art['html'])} chars de HTML. Nao publicado.")
    sys.exit(0)

try:
    if ATUALIZAR:
        atual = api("GET", f"posts/{ATUALIZAR['id']}/", fields="id,updated_at")["posts"][0]
        payload["posts"][0]["updated_at"] = atual["updated_at"]
        res = api("PUT", f"posts/{ATUALIZAR['id']}/", payload, source="html")
    else:
        res = api("POST", "posts/", payload, source="html")
except Exception as e:
    log(f"FALHA ao gravar post: {e}", "ERROR"); print(f"::error::{e}"); sys.exit(1)
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
