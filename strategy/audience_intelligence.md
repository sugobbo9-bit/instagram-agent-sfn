# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo. SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-11-18 (9ª execução)_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida por dado próprio** (idade, gênero, país/cidade, `online_followers` seguem **desconhecidos**). Bloqueio inalterado e reconfirmado em **18/11 (9ª rodada)**: o `.env` do Mac (`SFN/Instagram Agent/.env`, mtime **26/08**, não mudou) traz um `INSTAGRAM_ACCESS_TOKEN` de 306 chars **EXPIRADO desde 26/08/2026** — `GET /{ig-id}` e `follower_demographics` devolvem **OAuthException 190** ("Session has expired on 26-Aug-26"). O `INSTAGRAM_BUSINESS_ACCOUNT_ID` do `.env` é placeholder; o id real é `17841472609243044` (em `performance_history.json`/`account`). O token válido da Página segue só como **Secret do GitHub Actions**, inalcançável a esta rotina. **Não há arquivo de demografia/comentários commitado** em `data/` (`audience_demographics.json` / `comments_recent.json` seguem ausentes). Ver "Demografia — bloqueio".
- **Base: 8.850 seguidores** (snapshot do bootstrap de **15/11**, `account.followers_count`, `media_count` 198). Série semanal: 9.266 → 9.418 (+152) → 9.529 (+111) → 9.516 (−13) → 9.086 (−430) → **8.850 (−236)**. **2ª queda seguida** e a 1ª vez que o −236 aparece nesta rotina. Conta `sofatosnutricao`.
- Perfil presumido pelo nicho (hipótese, **não medido**): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 219 posts com métricas reais; **coleta NOVA "import" de 15/11/2026**; 226 posts no total)
> **Dado fresco nesta rodada.** Pela 1ª vez desde 01/11 há coleta nova: o bootstrap de 15/11 mediu **219 posts** (eram 195 no snapshot de 01/11). Os 7 sem métrica são os mais recentes (publicados 16–17/11, coletados antes). Tudo abaixo vem dessa coleta.

- **O carrossel domina — padrão forte e repetido em 8 coletas (16/09 → 15/11).** MAS a linha de base do carrossel **caiu**:

  | formato | n | alcance mediano | p90 | p75 | p25 | média saves/r | média shares/r | média comments/r | média likes/r |
  |---|---|---|---|---|---|---|---|---|---|
  | **carrossel** | 109 | **301** | 1.164 | 657 | 176 | 0,0157 | 0,0127 | 0,0008 | 0,0394 |
  | reel | 77 | 256 | 520 | 381 | 168 | 0,0068 | 0,0040 | 0,0010 | 0,0135 |
  | estático | 33 | 210 | 359 | 290 | 141 | 0,0114 | 0,0077 | 0,0011 | 0,0330 |

  **Mudança de base (achado da rodada):** a mediana all-time do carrossel **caiu de 366 → 301**. Não é um formato que piorou de natureza — é a **safra recente fraca entrando no conjunto medido**. A deterioração fica explícita por recência:

  | janela | mediana carrossel | mediana estático |
  |---|---|---|
  | all-time (n=109 / 33) | 301 | 210 |
  | últimos 30d (n=29 / 10) | **181** | 100,5 |
  | últimos 14d (n=15 / 6) | **165** | 89,5 |
  | últimos 7d (n=8 / 6) | **118,5** | 89,5 |

  O **alcance do carrossel recente está em queda livre** (301 → 181 → 118,5). O topo da conta segue sendo carrossel (**top 10%, n=21, 838–2.454 = 20/21 carrossel**; único Reel: o de nitrato), mas o **bottom 25% (n=55)** é reels (17) + carrosséis fracos (25) + estáticos (13), com `marca-vs-marca` (11), `card-informativo` (8) e `voce-sabia` (5) entre as séries do fundo.

- **Estrutura vencedora reconfirmada:** derrubar uma crença aceita + entregar protocolo. Famílias campeãs all-time estáveis: **lactato (2.454/2.450/1.516)**, **privação de sono (2.441)**, **carga de carboidrato (1.840 — maior salvamento da conta, saves/r 0,049)**, **cafeína (1.558)**, intestino 60 g/h (1.426), creatina (1.249), hidrogel (1.245), janela de 30 min (1.212), RED-S (1.164–1.180). O único versus no top: **isotônico Gatorade×Powerade (1.061, 10 shares)**.

- **Hook — contrarian > myth, RECONFIRMADO com n maior (dataset 15/11):**
  - `hook:contrarian` (carrossel, **n=20**): alcance mediano **374,5**, saves/r mediano **0,0149**, shares/r mediano 0,0109.
  - `hook:myth` (carrossel, **n=16**): alcance mediano **312**, saves/r mediano **0,0113**, shares/r mediano 0,0077.
  - `hook:number` (n=2): 383 — amostra mínima.
  - Leitura estável e agora mais robusta (n sobe de 12→20): "o protocolo que quase todo mundo faz errado + número" (contrarian) rende **mais alcance E mais save** que "esse mito diz X" (myth).

### O que eles comentam
- **A audiência salva e compartilha, mas quase não comenta** — idêntico nas 8 coletas. **94 comentários** somando 219 posts; apenas **41 posts com ≥1**; **mediana 0 por post**. Comentar não é o comportamento dominante.
- Maior ímã de comentário (contagem): **Reel de nitrato (16 comentários, reach 945)**, muito acima de tudo; depois um pelotão de ~3–5 em **comparação/ranking de produto e Reels de dúvida prática**. Hipótese **reconfirmada** (ainda só por contagem): o que gera pergunta/comentário concentra-se em **comparação de produto** e **dúvida operacional** — exatamente o terreno do futuro banco de respostas.
- **Texto dos comentários: ainda não lido** — depende de token válido + escopo `instagram_manage_comments`. O `posts_db.json` guarda só a contagem.

### Formatos agente-era (safra de 15/11 medida)
- **Versus "marca vs marca" (`series:marca-vs-marca`, n=19):** mediana **165**, padrão **bimodal e nítido** — mainstream/diferenciado em cima (**Gatorade×Powerade 1.061/10 shares**, Maurten×GU 495/3), commodity de nicho no fundo (a maioria com **0 share**: maxtitanium-probiotica 197, probiotica-newmillen 187, gu-sis 181, …, o pior **maxtitanium-dux 46**). **Reconfirma com n=19:** versus só rende quando as marcas são de massa OU as fórmulas de fato diferem. (Victor já aposentou o versus de commodity; trava `VERSUS_COMMODITY_BLOCKED` entrou no `quality_gate.py`.)
- **Card informativo (`series:card-informativo`, estático, n=9):** mediana **98** (196/160/129/103/98/91…) — **fundo do feed**, mesmo padrão do antigo estático, tendência fortemente negativa. **Sob observação por diretriz do Victor** (não re-pausar antes de ≥4 semanas; janela fecha ~24/11; n=9, dentro da janela). Reportado, não re-pausado.
- **"Você sabia" (`series:voce-sabia`, estático, n=17):** mediana **212** — a espinha dorsal do estático, estável no terço inferior.
- **Técnico com foto (`visual:foto`, carrossel, n=13):** alcance mediano **406** — acima do baseline (301), mas **inflado pela família campeã** (carga de carbo 1.840) e **confundido com o hook contrarian** (vários posts foto recentes são contrarian). n subiu de 6→13, mas o confundimento persiste: **ainda NÃO dá para isolar a foto como alavanca** — segue como hipótese a confirmar com corte limpo.
- **Provocativo / "se fosse" (`series:se-fosse`, n=3):** 495/366/189 — o Victor já encerrou; a curiosidade não se sustenta após o 1º.

### Fluxo de conteúdo recente (por prefixo de `local_id`, últimos 30d) — o feed está diluído
| fluxo | n | mediana alcance | shares totais | posts com 0 share |
|---|---|---|---|---|
| **`der_` técnico (derivado de vencedor)** | 9 | **406** | 72 | 1 |
| `draft_` técnico | 4 | 261,5 | 16 | 0 |
| **`vs_` versus de commodity de nicho** | 16 | **138,5** | 15 | **11** |
| **`card_` estático** | 9 | **98** | 5 | 4 |

**Leitura:** o motor (técnico `der_`+`draft_`, mediana 406/261) está sendo **afogado** pelo lastro (`vs_` 138,5 + `card_` 98), que é a maioria dos slots recentes. É a mesma mecânica que derrubou a série estática em set/out, agora com os `vs_*`. **Hipótese de audiência (forte, repetida):** a queda de alcance da conta é movida por **curadoria do feed** (volume de formatos fracos), não por falha do motor técnico — que, quando sai, ainda entrega 400+ e shares.

### Implicação de conteúdo (o que os dados sustentam)
Otimizar para **salvável/compartilhável** (carrossel de **contrarian/mito + comparação de produto que diferem**), não para "pergunta no fim pedindo comentário". Priorizar fueling / hidratação / sono / cafeína / **carga de carbo (família campeã, 1.840)** / lactato / comparação de produto distinto; **cortar suplemento/versus de nicho** (fundo persistente, 0 share) e reavaliar o `card_` ao fim da janela. Hook **contrarian** como padrão. Concentrar publicação em **14–15h UTC**.

### Janelas de publicação (carrossel, UTC, últimos 45d)
| janela UTC | n | dias distintos | mediana | leitura |
|---|---|---|---|---|
| **15h** | 5 | 5 | **546** | **slot técnico — o motor** |
| 14h | 11 | 11 | 300 | slot técnico, **limpo** (1 post/dia) |
| 11h | 2 | 2 | 319,5 | amostra baixa nesta janela |
| 18h | 1 | 1 | 495 | amostra mínima |
| **19h** | 8 | 8 | **157,5** | **morto** (onde saem os `vs_*`) |
| **20h** | 12 | 12 | **166** | **morto** (onde saem os `vs_*`) |

**Leitura honesta:** janela e conteúdo seguem **confundidos** — os piores números de 19–20h coincidem com os `vs_*` de commodity despejados ali. Sinal limpo: **14–15h UTC é o bloco forte**; **19–20h é onde o lastro é publicado**. Concentrar o que importa em 14–15h segue sendo a alavanca de execução.

---

## Demografia — bloqueio (token do Mac EXPIRADO, inalterado — 9ª rodada)
- `.env` do Mac com `INSTAGRAM_ACCESS_TOKEN` **expirado em 26/08/2026** (OAuthException 190) — reconfirmado em **18/11** via `GET /{ig-id}` + `follower_demographics`. Arquivo não mudou desde 26/08.
- Token válido da Página só como **Secret do GitHub Actions**, write-only, inalcançável aqui.
- **Nenhum arquivo de demografia/comentários commitado** no repo (reconfirmado).
- Nenhuma chamada a `follower_demographics`/`engaged_audience` (breakdown age/gender/city/country), `online_followers` ou `{media-id}/comments` é possível a partir daqui.

**Para desbloquear (decisão do Victor):**
- **(preferida)** Passo no **GitHub Actions** que puxe `follower_demographics`/`online_followers` **e o texto dos comentários** dos ~15 posts recentes e **commite** `data/audience_demographics.json` + `data/comments_recent.json`. Aí esta rotina lê dado próprio sem token no Mac.
- **(rápida)** Regerar o token de longa duração e atualizar o `.env` do Mac (com `instagram_manage_insights` + `instagram_manage_comments`) — destrava demografia E comentários imediatamente.
- Métricas vigentes (v21.0): `follower_demographics`/`engaged_audience` com `breakdown` age/gender/city/country; `online_followers` p/ horários. Requisito mínimo de seguidores costuma ser atendido; confirmar escopo ao instrumentar.

---

## Comentários — PENDENTE de token válido + escopo `instagram_manage_comments`
O estudo do **texto** dos comentários segue **não executado**: (1) token do Mac expirado; (2) ler/responder comentário exige **`instagram_manage_comments`** — o mesmo escopo necessário para responder no futuro. O embrião do **banco de respostas** (sentimento + perguntas/objeções mais frequentes) fica parado. Só por contagem: volume baixíssimo (94 comentários / 219 posts, mediana 0), concentrado em **comparação/ranking de produto** e no **Reel de nitrato** (16; padrão estável há 8 coletas).

---

## Lacunas de dados (o que ainda não conseguimos medir)
- Demografia (idade/gênero/local) e `online_followers` — token do Mac expirado; sem arquivo próprio.
- **follows/reach** e `profile_visits` por post — o snapshot `import` do `posts_db.json` **não traz** esses campos (**0 de 219** registros têm `follows`); conversão em seguidor segue **cega no nível do post**. Lacuna crítica dado o −236: não dá para dizer QUAL conteúdo perde/ganha seguidor.
- Texto/sentimento dos comentários — ver acima.
- Granularidade temporal: a coleta de 15/11 é um **snapshot único `import`** (sem checkpoints 24h/72h/7d/30d); mede o lifetime no momento da coleta, não a curva de maturação.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-11-18 (9ª execução)
**O que foi feito:** Retest do token do `.env` do Mac (`GET /{ig-id}`, `follower_demographics`) e reanálise completa da **coleta NOVA de 15/11** (`posts_db.json`): formato (com cortes de recência 30d/14d/7d), hook, série, foto, fluxo por `local_id`, janelas (dias distintos), contagem de comentários, top 10%/bottom 25%, versus bimodal, seguidores.

**O que mudou desde a última execução (11/11):**
- **DADO FRESCO, enfim.** Pela 1ª vez desde 01/11 há coleta nova: **bootstrap de 15/11, 219 posts medidos** (eram 195). Era o item nº 1 de "a confirmar" das rodadas 7 e 8 — agora há sinal de audiência novo.
- **Seguidores: 8.850 (−236), 2ª queda seguida.** Trajetória: …9.516 → 9.086 (−430) → **8.850 (−236)**. A sangria não estancou; desacelerou de −430 para −236.
- **Base do carrossel caiu: 366 → 301 (all-time).** E a queda recente é severa: carrossel 30d=181, 14d=165, **7d=118,5**. O alcance do carrossel recente está em **queda livre** — safra fraca entrando no conjunto, não mudança de natureza do formato.
- **Hook contrarian reconfirmado com n maior:** contrarian n=12→**20** (374,5 alcance, 0,0149 saves/r) segue > myth n=16 (312, 0,0113). Padrão mais robusto.
- **foto subiu a n=13** (mediana 406, acima do baseline) **mas segue confundida com contrarian** e inflada pela carga de carbo — ainda não isolável como alavanca.
- **Versus com n=19:** bimodal reconfirmado (Gatorade×Powerade 1.061/10 shares no topo; commodity de nicho no fundo, maioria **0 share**, pior maxtitanium-dux 46).
- **Fluxo recente (30d):** motor técnico `der_` 406/72 shares vs lastro `vs_` 138,5 (11/16 com 0 share) + `card_` 98. **Feed diluído por formato fraco** — hipótese central da queda de alcance (curadoria, não falha do motor).
- **card-informativo n=9, mediana 98** — fundo, tendência negativa, **dentro da janela de observação do Victor** (fecha ~24/11); reportado, não re-pausado.
- **Comentários:** 94/219, 41 com ≥1, mediana 0; Reel de nitrato (16) outlier. Padrão idêntico. Texto ainda bloqueado.
- **Token do Mac:** re-testado 18/11 — **ainda expirado 26/08** (OAuthException 190). Demografia + texto de comentários bloqueados (9ª rodada).

**Hipóteses acionáveis (com tamanho de amostra):**
- **(confirmada, n=20 vs 16)** Hook contrarian > myth em alcance E save — padrão de produção.
- **(confirmada, 8 coletas)** Carrossel é o motor de save/share; reels+estáticos dominam o fundo (top 10% = 20/21 carrossel).
- **(confirmada, n=19)** Versus só rende com marca mainstream ou fórmula distinta; commodity de nicho = piso de alcance + 0 share.
- **(forte, repetida)** A queda de alcance da conta é movida por **curadoria** (volume de `vs_`/`card_` fracos afogando o técnico), não por falha do motor técnico.
- **(pendente de corte limpo)** Foto como alavanca isolada — n=13 mas confundida com contrarian.

**Bloqueios que persistem:** demografia e **texto** de comentários não medíveis (token do Mac expirado, sem arquivo próprio commitado); **follows/reach ausente** do snapshot (crítico frente ao −236); coleta é snapshot único (sem curva de maturação).

**A confirmar na próxima execução:**
- Se o −236 continuou, estabilizou ou reverteu (depende de novo snapshot de seguidores).
- Se a trava `VERSUS_COMMODITY_BLOCKED` e a concentração em 14–15h reduziram o lastro e recuperaram a mediana recente do carrossel (hoje 118,5 em 7d).
- `card_*` ao fim da janela do Victor (~24/11): decisão manter/pausar com base completa (hoje mediana 98).
- Se o token do Mac foi regerado ou entrou o passo de Actions que commita demografia/comentários → iniciar demografia + análise temática de comentários (banco de respostas).

### 2026-11-11 (8ª execução)
Retest do token (ainda expirado 26/08) e reanálise do `posts_db.json` (então 195 medidos, snapshot único de 01/11). **Nenhum dado de engajamento novo** — 8ª leitura coerente do mesmo quadro (carrossel 366 / reel 256 / estático 212; contrarian 430/0,0166 > myth 312/0,0113; 92 comentários, mediana 0, Reel de nitrato 16; top 10% 18/19 carrossel). Total subiu 200→207 mas os 12 novos eram fila sem métrica/`permalink`. **2º blackout de publicação detectado** (último `permalink` em 31/10; ~11 dias parados; fila 6/12 `marca-vs-marca` de commodity). Token re-testado: expirado 26/08.

### 2026-11-04 (7ª execução)
1ª análise sobre a coleta de 01/11 (195 medidos / 200 total) — 1º dado fresco desde 11/10. Seguidores 9.516→**9.086 (−430)**, 1ª queda grande. Carga de carbo re-medida 1.840. Versus n=9 com split mainstream×nicho nítido. Foto n=6, mediana 469. 14h UTC emergiu como slot forte e limpo. Token: expirado 26/08.

### 2026-10-28 (6ª execução)
1ª análise sobre a coleta de 11/10 (178 medidos / 185 total). Formatos agente-era medidos pela 1ª vez (foto n=3, provocativo n=3, versus n=2). Hook: contrarian (n=7, 424) > myth (n=16, 312). Seguidores 9.516 (−13), 1ª semana não-positiva. Coleta de métricas parada em 11/10. Token: expirado 26/08.

### 2026-10-07 (5ª execução)
Reanálise (coleta 04/10; 168/171). Reconfirmou bloqueios de token/demografia/comentários. Baseline carrossel 474→418. Base 9.418→9.529 (+111). Correção de integridade das janelas (confundimento por lote).

### 2026-09-30 (4ª execução)
Reanálise (coleta 27/09; 160/163). Base 9.266→9.418 (+152). Carrossel domina; myth-busting vence; comparação compartilha; nicho no fundo; mediana 0 de comentário.

### 2026-09-23 (3ª execução)
Reanálise (151 posts). Diagnóstico do bloqueio de demografia mudou de "token expirado" para **arquitetural** (token só no Actions). Horário publica ~08h BRT; estático não pausado.

### 2026-09-16 (1ª execução)
Primeira montagem; 135 posts. Graph API falhou por token expirado (26/08). Achados: carrossel > Reel; sono/recuperação maior alcance mediano; sexta pior dia; audiência salva/compartilha e quase não comenta.

_(As revisões estratégicas e decisões — pausa/enforce do estático, proibição de sexta, famílias vencedoras, retestes, formatos prov_*/foto/versus, volta do card informativo, claim-check, escalonamento dos blackouts, trava de versus-commodity — estão em `current_strategy.md` e `learnings.md`.)_
