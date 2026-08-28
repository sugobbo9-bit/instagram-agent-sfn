# SETUP — Colocar o agente no ar

O repositório já está commitado localmente (branch `main`).
Faltam 3 passos. Levam ~10 minutos.

---

## Passo 1 — Gerar um token novo

O token anterior foi exposto (chat + histórico do navegador) e já expirou.

### 1.1 — Pegar App ID e App Secret
https://developers.facebook.com/apps/ → seu app →
**Configurações → Básico**. Copie o **ID do aplicativo** e a
**Chave secreta do aplicativo** (botão "Mostrar").

### 1.2 — Gerar token curto no Explorer
https://developers.facebook.com/tools/explorer/

- **Meta App**: selecione seu app
- **User or Page**: `User Token`
- Em **Permissions**, marque exatamente estas seis:

```
instagram_basic
instagram_content_publish
instagram_manage_insights     <-- a que faltava
pages_read_engagement
pages_show_list
business_management
```

- Clique **Generate Access Token** e autorize.

`instagram_manage_insights` é a permissão crítica. Sem ela, as 110
publicações da conta voltam sem nenhuma métrica e o sistema de winners,
percentis e derivativos não funciona.

### 1.3 — Trocar por um token de 60 dias
Cole no navegador, substituindo os três valores:

```
https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=TOKEN_CURTO
```

A resposta traz `access_token` — esse é o token longo (60 dias).

### 1.4 — (Recomendado) Converter para Page Token, que não expira
Com o token longo do passo anterior:

```
https://graph.facebook.com/v21.0/me/accounts?access_token=TOKEN_LONGO
```

Na resposta, o campo `access_token` dentro da Página
**"Somente os Fatos Nutrição"** é um Page Access Token **sem validade**.
Use esse. Assim você nunca mais precisa renovar nada.

### 1.5 — Cadastrar no GitHub
https://github.com/sugobbo9-bit/instagram-agent-sfn/settings/secrets/actions

Edite o secret `INSTAGRAM_ACCESS_TOKEN` e cole o token.
Não coloque o token em nenhum arquivo do projeto.

### 1.6 — Rodar
- **Actions → Bootstrap → Run workflow** — preenche os baselines com as
  métricas reais dos 110 posts
- **Actions → Publish → Run workflow** — publica o primeiro carrossel

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
