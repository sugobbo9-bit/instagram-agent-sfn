"""
config.py — Configuração central do Instagram Agent
Lê variáveis de ambiente do arquivo .env na raiz do projeto
"""
import os
import sys
from pathlib import Path

# Raiz do projeto — dois níveis acima deste script
PROJECT_ROOT = Path(__file__).parent.parent

# Carrega .env se existir
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

# Credenciais Instagram
INSTAGRAM_BUSINESS_ACCOUNT_ID = os.environ.get("INSTAGRAM_BUSINESS_ACCOUNT_ID", "")
if not INSTAGRAM_BUSINESS_ACCOUNT_ID:
    # fallback: gravado pelo bootstrap em data/performance_history.json
    try:
        import json as _j
        _ph = _j.load(open(PROJECT_ROOT / "data" / "performance_history.json"))
        INSTAGRAM_BUSINESS_ACCOUNT_ID = (_ph.get("account") or {}).get("ig_id", "") or ""
    except Exception:
        pass
INSTAGRAM_ACCESS_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN", "")
FACEBOOK_APP_ID = os.environ.get("FACEBOOK_APP_ID", "")
FACEBOOK_APP_SECRET = os.environ.get("FACEBOOK_APP_SECRET", "")
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME", "")

# Caminhos de diretórios
DIRS = {
    "root": PROJECT_ROOT,
    "strategy": PROJECT_ROOT / "strategy",
    "research": PROJECT_ROOT / "research",
    "content": PROJECT_ROOT / "content",
    "drafts": PROJECT_ROOT / "content" / "drafts",
    "approved": PROJECT_ROOT / "content" / "approved",
    "queue": PROJECT_ROOT / "content" / "queue",
    "published": PROJECT_ROOT / "published",
    "analytics": PROJECT_ROOT / "analytics",
    "templates": PROJECT_ROOT / "templates",
    "assets": PROJECT_ROOT / "assets",
    "data": PROJECT_ROOT / "data",
    "logs": PROJECT_ROOT / "logs",
    "scripts": PROJECT_ROOT / "scripts",
}

# Configurações de conteúdo
INSTAGRAM_GRAPH_API_BASE = "https://graph.facebook.com/v21.0"
CAROUSEL_DIMENSIONS = (1080, 1350)
REEL_DIMENSIONS = (1080, 1920)

# Configurações de analytics
ANALYTICS_CHECKPOINTS_HOURS = [24, 72, 168, 720]  # 24h, 72h, 7d, 30d

def check_credentials():
    """Verifica se as credenciais estão configuradas."""
    missing = []
    for var in ["INSTAGRAM_BUSINESS_ACCOUNT_ID", "INSTAGRAM_ACCESS_TOKEN"]:
        if not os.environ.get(var):
            missing.append(var)
    return missing

if __name__ == "__main__":
    missing = check_credentials()
    if missing:
        print(f"⚠️  Credenciais ausentes: {', '.join(missing)}")
        print(f"   Crie o arquivo {PROJECT_ROOT}/.env com base em .env.example")
    else:
        print("✅ Configuração OK")
        print(f"   Conta: {INSTAGRAM_USERNAME}")
        print(f"   Account ID: {INSTAGRAM_BUSINESS_ACCOUNT_ID[:6]}...")
