# SETUP — Colocar o agente no ar

O repositório já está commitado localmente (branch `main`).
Faltam 3 passos. Levam ~10 minutos.

---

## Passo 1 — Gerar um token novo

O token anterior foi exposto (chat + histórico do navegador). **Invalide-o.**

1. https://developers.facebook.com/tools/explorer/
2. Selecione seu app → gere um User Token com estas permissões:
   - `instagram_basic`
   - `instagram_content_publish`
   - `instagram_business_content_publish`
   - `instagram_manage_insights`
   - `pages_read_engagement`
   - `pages_show_list`
3. Converta para Long-Lived (60 dias):
   `https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=TOKEN_CURTO`

Guarde o token longo. Ele NÃO vai para arquivo nenhum — vai direto para os Secrets do GitHub.

---

## Passo 2 — Criar o repositório e dar push

O repositório precisa ser **público** para que `raw.githubusercontent.com`
sirva as imagens sem autenticação (a Meta faz cURL nas URLs e não envia token).

```bash
cd "/Users/vcb/Documents/Claude/Projects/SFN/Instagram Agent"
git remote add origin https://github.com/SEU_USUARIO/instagram-agent-sfn.git
git push -u origin main
```

Crie o repo antes em https://github.com/new (nome: `instagram-agent-sfn`, público, sem README).

### Se você não quiser o repositório público
Ver a seção "Alternativa com repo privado" no fim deste arquivo.

---

## Passo 3 — Cadastrar o token nos Secrets

No repositório → **Settings → Secrets and variables → Actions → New repository secret**

- Nome: `INSTAGRAM_ACCESS_TOKEN`
- Valor: o token longo do Passo 1

Depois, em **Settings → Actions → General → Workflow permissions**,
marque **Read and write permissions** (os workflows commitam dados de volta).

---

## Passo 4 — Rodar o bootstrap

Aba **Actions → Bootstrap → Run workflow**.

Ele valida o token, descobre o Instagram Business Account ID, importa o
histórico da conta e calcula os baselines por formato. O log mostra tudo
(o token aparece mascarado).

Se passar, o agente está no ar:
- **Publish** roda todo dia às 09:00 (Brasília) e publica o próximo item aprovado
- **Analytics** roda 3x ao dia e coleta os checkpoints de 24h / 72h / 7d / 30d

Para testar sem publicar: **Actions → Publish → Run workflow → dry_run ✓**

---

## Alternativa com repo privado

`raw.githubusercontent.com` exige token em repo privado, e a Meta não envia
token ao buscar a imagem. Duas saídas:

**A) Dois repositórios** — este privado, e um segundo público só com os PNGs
renderizados. Ajuste `raw_url()` em `scripts/publisher.py` para apontar ao repo
público. Nada de estratégia ou métricas fica exposto.

**B) Cloudflare R2** — 10 GB grátis, domínio público. Substitua `raw_url()` por
upload ao R2 e uso da URL pública retornada.

Me avise qual e eu implemento.

---

## Manutenção

O token de 60 dias **expira**. O bootstrap e o publisher avisam quando faltam
menos de 7 dias (`::warning::` no log do Actions). Renove pelo mesmo caminho
do Passo 1 e atualize o Secret.
