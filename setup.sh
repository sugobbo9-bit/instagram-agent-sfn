#!/bin/bash
# setup.sh — Configuração inicial do Instagram Agent
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "🚀 Instagram Agent — Setup Inicial"
echo "=================================="

# 1. Dependências Python
echo ""
echo "1. Instalando dependências Python..."
pip3 install -r requirements.txt --quiet

# 2. Puppeteer para renderização
echo ""
echo "2. Instalando Puppeteer (renderização de carrosséis)..."
cd scripts && npm install puppeteer --save-quiet 2>/dev/null && cd ..
echo "   ✅ Puppeteer instalado"

# 3. Verifica .env
echo ""
echo "3. Verificando configuração..."
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "   ⚠️  Arquivo .env criado a partir do .env.example"
  echo "   ➡️  AÇÃO NECESSÁRIA: edite o arquivo .env com suas credenciais do Instagram"
else
  echo "   ✅ .env já existe"
fi

# 4. Testa configuração
echo ""
echo "4. Testando configuração..."
python3 scripts/config.py

echo ""
echo "=================================="
echo "✅ Setup concluído!"
echo ""
echo "Próximos passos:"
echo "  1. Edite .env com suas credenciais do Instagram Graph API"
echo "  2. Execute: python3 scripts/instagram_api.py  (para testar a conexão)"
echo "  3. Execute: python3 scripts/daily_loop.py     (para rodar o ciclo diário)"
echo "  4. Ou simplesmente: claude .                  (para operar via Claude Code)"
