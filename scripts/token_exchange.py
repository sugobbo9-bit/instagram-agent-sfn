"""
token_exchange.py — Troca token curto por longo e, se possivel, por Page Token
permanente. Grava o resultado direto no Secret do repositorio.
Nunca imprime o token.
"""
import os, sys, json, subprocess
from datetime import datetime, timezone
import requests

B = "https://graph.facebook.com/v21.0"
APP_ID     = os.environ["FB_APP_ID"].strip()
APP_SECRET = os.environ["FB_APP_SECRET"].strip()
SHORT      = os.environ["FB_SHORT_TOKEN"].strip()
REPO       = os.environ["GITHUB_REPOSITORY"]

def show(t):
    return f"{t[:6]}...{t[-4:]} (len={len(t)})" if t else "(vazio)"

def get(path, **p):
    r = requests.get(f"{B}/{path}", params=p, timeout=45)
    j = r.json()
    if "error" in j:
        raise SystemExit(f"::error::{path}: {j['error'].get('message')}")
    return j

print("=" * 58)
print("TROCA DE TOKEN")
print("=" * 58)

# 0 — a qual app o token pertence?
print("\n[0] Identificando o app dono do token...")
_d = requests.get(f"{B}/debug_token",
                  params={"input_token": SHORT, "access_token": SHORT}, timeout=45).json()
_dd = _d.get("data", {})
_owner = str(_dd.get("app_id", ""))
print(f"    app_id do token : {_owner}")
print(f"    nome do app     : {_dd.get('application')}")
print(f"    app informado   : {APP_ID}")
print(f"    tipo            : {_dd.get('type')}  | valido: {_dd.get('is_valid')}")
print(f"    permissoes      : {', '.join(sorted(_dd.get('scopes', [])))}")
if _owner and _owner != APP_ID:
    print(f"::error::O token pertence ao app {_owner} ({_dd.get('application')}), "
          f"nao ao app {APP_ID}. Use o App ID/Secret do app {_owner}, "
          f"ou gere o token no Explorer com o app {APP_ID} selecionado.")
    raise SystemExit(1)

# 1 — curto -> longo (60 dias)
print("\n[1] Trocando token curto por longo...")
lng = get("oauth/access_token", grant_type="fb_exchange_token",
          client_id=APP_ID, client_secret=APP_SECRET, fb_exchange_token=SHORT)["access_token"]
print(f"    token longo obtido: {show(lng)}")

d = get("debug_token", input_token=lng, access_token=lng)["data"]
exp = d.get("expires_at", 0)
print(f"    expira em : {'nunca' if exp == 0 else datetime.fromtimestamp(exp, timezone.utc).isoformat()}")
print(f"    permissoes: {', '.join(sorted(d.get('scopes', [])))}")

falta = {"instagram_manage_insights", "instagram_content_publish", "instagram_basic"} - set(d.get("scopes", []))
if falta:
    print(f"::warning::permissoes ainda ausentes: {', '.join(sorted(falta))}")

# 2 — longo -> Page Token (nao expira)
print("\n[2] Buscando Page Access Token permanente...")
final, tipo = lng, "USER (60 dias)"
pages = get("me/accounts", access_token=lng,
            fields="id,name,access_token,instagram_business_account{id,username}").get("data", [])
for p in pages:
    ig = p.get("instagram_business_account")
    if ig and p.get("access_token"):
        final, tipo = p["access_token"], "PAGE (sem validade)"
        print(f"    pagina    : {p.get('name')}")
        print(f"    instagram : @{ig.get('username')} ({ig.get('id')})")
        pd = get("debug_token", input_token=final, access_token=lng)["data"]
        print(f"    expira em : {'nunca' if pd.get('expires_at', 0) == 0 else pd.get('expires_at')}")
        print(f"    permissoes: {', '.join(sorted(pd.get('scopes', [])))}")
        break
else:
    print("::warning::Nenhum Page Token disponivel — usando o token de usuario de 60 dias")

print(f"\n[3] Gravando no Secret INSTAGRAM_ACCESS_TOKEN — tipo {tipo}")
env = {**os.environ, "GH_TOKEN": os.environ["GH_PAT"]}
subprocess.run(["gh", "secret", "set", "INSTAGRAM_ACCESS_TOKEN", "--repo", REPO, "--body", final],
               check=True, env=env, capture_output=True)
print("    secret atualizado.")
print("\n" + "=" * 58)
print(f"OK — token {tipo} instalado")
print("=" * 58)
