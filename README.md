# Instagram Agent — Nutrição Esportiva
Sistema autônomo de crescimento para Instagram no nicho de nutrição esportiva.

## Estado Atual
✅ Infraestrutura completa construída
✅ 3 carrosséis redigidos e prontos para render/publicação
⚠️  Credenciais do Instagram ainda não configuradas

## Estrutura
```
Instagram Agent/
├── CLAUDE.md              ← prompt/missão do agente (lido automaticamente pelo Claude Code)
├── .env                   ← suas credenciais (NUNCA commitar)
├── .env.example           ← template de credenciais
├── setup.sh               ← setup inicial
├── requirements.txt
├── strategy/
│   ├── current_strategy.md
│   └── learnings.md
├── data/
│   ├── posts_db.json      ← banco de dados central de posts
│   ├── hook_library.json  ← 20 hooks iniciais
│   ├── topic_library.json ← 25 tópicos mapeados
│   ├── trend_inbox.json   ← inbox de tendências
│   ├── experiments.json   ← registro de experimentos
│   ├── publishing_queue.json ← fila de publicação
│   ├── winner_library.json
│   └── failure_log.json
├── content/
│   ├── drafts/            ← 3 carrosséis prontos
│   ├── approved/
│   └── queue/
├── published/
├── analytics/
├── templates/
├── assets/
├── logs/
└── scripts/
    ├── config.py
    ├── instagram_api.py
    ├── analytics_collector.py
    ├── quality_gate.py
    ├── render_carousel.py
    └── daily_loop.py
```

## Ação Necessária: Credenciais do Instagram

Para publicação e coleta de analytics automáticas, você precisa de:

### 1. Conta Instagram Business ou Creator
Sua conta precisa estar configurada como Business ou Creator no app do Instagram.

### 2. Aplicativo Facebook com Instagram Graph API
1. Acesse: https://developers.facebook.com
2. Crie um aplicativo → tipo "Business"
3. Adicione o produto "Instagram Graph API"
4. Em permissões, solicite: `instagram_basic`, `instagram_content_publish`, `instagram_manage_insights`, `pages_read_engagement`

### 3. Token de Acesso de Longa Duração
1. No Facebook Business Manager, conecte sua página ao app
2. Gere um Page Access Token
3. Converta para Long-Lived Token (válido por 60 dias):
   ```
   GET https://graph.facebook.com/v21.0/oauth/access_token
     ?grant_type=fb_exchange_token
     &client_id={app_id}
     &client_secret={app_secret}
     &fb_exchange_token={short_lived_token}
   ```
4. Obtenha o Instagram Business Account ID:
   ```
   GET https://graph.facebook.com/v21.0/me/accounts?access_token={token}
   ```

### 4. Configure o .env
```bash
INSTAGRAM_BUSINESS_ACCOUNT_ID=123456789
INSTAGRAM_ACCESS_TOKEN=EAAxxxxxxxxxx
FACEBOOK_APP_ID=your_app_id
FACEBOOK_APP_SECRET=your_app_secret
INSTAGRAM_USERNAME=seu_usuario
PROJECT_ROOT=/Users/vcb/Documents/Claude/Projects/SFN/Instagram Agent
```

### 5. Teste a conexão
```bash
python3 scripts/instagram_api.py
```

## Conteúdo Pronto para Publicar
Os 3 primeiros carrosséis estão em `content/drafts/`:
- `draft_001` — Carboidratos 60–90g/hora (glicose + frutose)
- `draft_002` — Cafeína não desidrata (myth-busting)
- `draft_003` — Bonking: é fisiologia, não fraqueza mental

Para renderizar e ver as imagens:
```bash
python3 scripts/render_carousel.py content/drafts/draft_001_carbo_60_90g.json
```

## Uso com Claude Code
```bash
cd "/Users/vcb/Documents/Claude/Projects/SFN/Instagram Agent"
claude .
```
Claude Code lê o CLAUDE.md automaticamente e opera como agente autônomo.

## Ciclo Diário Manual
```bash
python3 scripts/daily_loop.py
```

## Nota sobre renderização
A rede local desta máquina bloqueia o download do binário do Chrome usado
pelo Puppeteer. Enquanto isso não for liberado, a renderização dos slides
roda no ambiente Claude (que já tem Chromium) e os PNGs são gravados de
volta em `content/drafts/<local_id>/`.

Para habilitar renderização 100% local, libere o acesso a
`storage.googleapis.com` e rode:
```bash
cd scripts && npx puppeteer browsers install chrome
```
