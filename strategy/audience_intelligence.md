# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo. SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-11-04 (7ª execução)_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida por dado próprio** (idade, gênero, país/cidade, `online_followers` seguem **desconhecidos**). Bloqueio inalterado: o `.env` do Mac (`SFN/Instagram Agent/.env`, mtime 26/08) traz um `INSTAGRAM_ACCESS_TOKEN` de 306 chars **EXPIRADO desde 26/08/2026** — reconfirmado nesta rodada (Graph API devolve OAuthException 190, "Session has expired on 26-Aug-26"). O `INSTAGRAM_BUSINESS_ACCOUNT_ID` do `.env` é um placeholder (`your_instagram_business_account_id`); o id real vive em `performance_history.json` (`17841472609243044`). O token válido da Página segue só como **Secret do GitHub Actions**, inalcançável a esta rotina. **Não há arquivo de demografia/comentários commitado** em `data/` (`audience_demographics.json` / `comments_recent.json` seguem ausentes). Ver "Demografia — bloqueio".
- **Base: 9.086 seguidores** (snapshot do bootstrap de 01/11, `media_count` 174). Série semanal: 9.266 → 9.418 (+152) → 9.529 (+111) → 9.516 (−13) → **9.086 (−430)**. A **1ª queda GRANDE** da conta — e a 1ª vez que esse número aparece nesta rotina (a execução anterior ainda via 9.516, sem dado novo pós-11/10). Conta `sofatosnutricao`.
- Perfil presumido pelo nicho (hipótese, **não medido**): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 195 posts com métricas reais; coleta única "import" de 01/11/2026; 200 posts no total)
- **O carrossel domina — padrão forte e repetido em 7 coletas (16/09 → 01/11).**

  | formato | n | alcance mediano | p90 | p75 | p25 | média saves/r | média shares/r | média comments/r | média likes/r |
  |---|---|---|---|---|---|---|---|---|---|
  | **carrossel** | 91 | **366** | 1.180 | 760 | 192 | 0,0176 | 0,0130 | 0,0010 | 0,0408 |
  | reel | 77 | 256 | 520 | 381 | 168 | 0,0068 | 0,0040 | 0,0010 | 0,0135 |
  | estático | 27 | 212 | 359 | 299 | 150 | 0,0117 | 0,0081 | 0,0013 | 0,0325 |

  Baseline do carrossel **estável em 366** por mais uma coleta. O **top 10%** de alcance da conta (n=19, 854–2.454) é **18/19 carrossel** (único Reel: o de nitrato); o **bottom 25%** (n=48) é dominado por Reels (20) + carrosséis fracos (18) + estáticos (10), com `voce-sabia` (5), `marca-vs-marca` (4) e `card-informativo` (4) entre as séries do fundo.
- **Estrutura vencedora reconfirmada:** derrubar uma crença aceita + entregar protocolo. **Vencedor re-medido nesta coleta:** carga de carboidrato subiu para **1.840** (era 1.661 em 11/10; saves/r **0,049** — o maior salvamento da conta). Campeões all-time estáveis: lactato (2.450/1.516), privação de sono (2.441), cafeína (1.558), intestino 60g/h (1.426), creatina (1.249), hidrogel (1.245), janela de 30 min (1.212), RED-S (1.180).
- **Hook — contrarian > myth genérico, reconfirmado (dataset de 01/11):**
  - `hook:contrarian` (carrossel, **n=12**): alcance mediano **430**, saves/r mediano **0,0166**.
  - `hook:myth` (carrossel, **n=16**): alcance mediano **312**, saves/r mediano **0,0113**.
  - `hook:number` (n=2): 383 — amostra mínima.
  - Leitura estável: "o protocolo que quase todo mundo faz errado + número" (contrarian) rende mais save que "esse mito diz X" (myth).

### O que eles comentam
- **A audiência salva e compartilha, mas quase não comenta** — idêntico nas 7 coletas. **92 comentários** somando 195 posts; apenas **39 posts com ≥1**; **mediana 0 por post**. Comentar não é o comportamento dominante.
- Maior ímã de comentário (contagem): **Reel de nitrato (16 comentários)**, muito acima de tudo; depois um pelotão de ~3–5 em **comparação/ranking de produto** (maltodextrina 5, ranking carbo em pó 5, "15 g carbo/h" 5, hidrogel 5, magnésio/sono 4, gel 4, whey vs vegetal 3). Hipótese **reconfirmada** (ainda só por contagem): o que gera pergunta/comentário concentra-se em **comparação de produto** — exatamente o terreno do futuro banco de respostas.
- **Texto dos comentários: ainda não lido** — depende de token válido + escopo `instagram_manage_comments`. O `posts_db.json` guarda só a contagem.

### Formatos agente-era (com a safra pós-11/10 finalmente medida)
- **Versus "marca vs marca" (`series:marca-vs-marca`, n=9):** mediana 182, mas o padrão é **bimodal e claro** — mainstream/diferenciado em cima (**Gatorade×Powerade 699**, Maurten×GU 495), commodity de nicho no fundo (294, 185, 182, 167, 159, 124, 80). **Reconfirma, agora com n=9:** versus só rende quando as marcas são de massa OU as fórmulas de fato diferem. (O Victor já aposentou o versus de commodity.)
- **Card informativo (`series:card-informativo`, estático, n=4):** mediana **110** (175/131/89/86) — padrão do antigo estático. **Sob observação por diretriz do Victor** (não re-pausar antes de ≥4 semanas; n=4, dentro da janela).
- **"Você sabia" (`series:voce-sabia`, estático, n=17):** mediana **212** — a espinha dorsal do estático, estável no terço inferior.
- **Técnico com foto (`visual:foto`, carrossel, n=6):** alcance mediano **469** (1.840 / 511 / 502 / 436 / 354 / 264) — **agora acima do baseline 366**. MAS o topo (1.840) é a **família campeã (carga de carbo)**, que infla a mediana; sem ele, os 5 restantes medianam 436 (ainda acima do baseline). **Upgrade de hipótese:** de "a foto NÃO é a alavanca isolada" (n=3) para "**foto + contrarian vem andando acima do baseline (n=6) — confirmar com n≥10 antes de declarar padrão**". Vários posts foto recentes são contrarian, então foto e hook estão confundidos.
- **Provocativo / "se fosse" (`series:se-fosse`, n=3):** 495/366/188 — o Victor já encerrou; a curiosidade não se sustenta após o 1º.

### Implicação de conteúdo (o que os dados sustentam)
Otimizar para **salvável/compartilhável** (carrossel de **contrarian/mito + comparação de produto que diferem**), não para "pergunta no fim pedindo comentário". Priorizar fueling / hidratação / sono / cafeína / **carga de carbo (família campeã, re-medida 1.840)** / comparação de produto distinto; **reduzir suplemento de nicho** (fundo persistente). Hook **contrarian** ("quase todo mundo faz errado + número + protocolo") como padrão.

### Janelas de publicação (carrossel, UTC, dias distintos — dataset 01/11)
| janela UTC | nPosts | dias distintos | med/dia | leitura |
|---|---|---|---|---|
| **14h** | 8 | 8 | **469** | **forte e LIMPA** (1 post por dia distinto) |
| 18h | 10 | 7 | 630 | forte, mistura lote |
| 19h | 11 | 9 | 474 | moderada (confundida com conteúdo recente fraco) |
| 11h | 15 | 15 | 301 | **fraca, limpa e grande — e é onde a automação publica** |
| 20h | 7 | 7 | 294 | fraca (slot dos vs_* de nicho) |
| 15h | 20 | 8 | 729 | **ainda confundida por lote — NÃO usar como âncora** |
| 16h / 17h | 6 / 7 | 2 / 2 | — | confundidas (poucos dias) |

**Leitura honesta:** janela e conteúdo estão **confundidos** — os piores números recentes de 19–20h coincidem com os `vs_*` de commodity despejados ali. O sinal **limpo** é: **14h UTC é o slot forte e limpo** (469, 8 dias distintos) e **11h UTC é o slot fraco onde a automação de fato publica** (301, 15 dias). Concentrar o que importa em 14–15h segue sendo a alavanca de execução.

---

## Demografia — bloqueio (token do Mac EXPIRADO, inalterado)
- `.env` do Mac com `INSTAGRAM_ACCESS_TOKEN` **expirado em 26/08/2026** (OAuthException 190) — reconfirmado nesta rodada via `GET /{ig-id}`. Arquivo não mudou desde 26/08.
- Token válido da Página só como **Secret do GitHub Actions**, write-only, inalcançável aqui.
- **Nenhum arquivo de demografia/comentários commitado** no repo (reconfirmado).
- Nenhuma chamada a `follower_demographics`/`engaged_audience` (breakdown age/gender/city/country), `online_followers` ou `{media-id}/comments` é possível a partir daqui.

**Para desbloquear (decisão do Victor):**
- **(preferida)** Passo no **GitHub Actions** que puxe `follower_demographics`/`online_followers` **e o texto dos comentários** dos ~15 posts recentes e **commite** `data/audience_demographics.json` + `data/comments_recent.json`. Aí esta rotina lê dado próprio sem token no Mac.
- **(rápida)** Regerar o token de longa duração e atualizar o `.env` do Mac (com `instagram_manage_insights` + `instagram_manage_comments`) — destrava demografia E comentários imediatamente para o estudo.
- Métricas vigentes (v21.0): `follower_demographics`/`engaged_audience` com `breakdown` age/gender/city/country; `online_followers` p/ horários. Requisito mínimo de seguidores (9k) costuma ser atendido; confirmar escopo ao instrumentar.

---

## Comentários — PENDENTE de token válido + escopo `instagram_manage_comments`
O estudo do **texto** dos comentários segue **não executado**: (1) token do Mac expirado; (2) ler/responder comentário exige **`instagram_manage_comments`** — o mesmo escopo necessário para responder no futuro. O embrião do **banco de respostas** (sentimento + perguntas/objeções mais frequentes) fica parado. Só por contagem: volume baixíssimo (92 comentários / 195 posts, mediana 0), concentrado em **comparação/ranking de produto** e no **Reel de nitrato** (padrão estável há 7 coletas).

---

## Lacunas de dados (o que ainda não conseguimos medir)
- Demografia (idade/gênero/local) e `online_followers` — token do Mac expirado; sem arquivo próprio.
- **follows/reach** e `profile_visits` por post — o snapshot `import` do `posts_db.json` **não traz** esses campos (0 de 195 registros têm `follows`); conversão em seguidor segue **cega no nível do post**.
- Texto/sentimento dos comentários — ver acima.
- Granularidade temporal da coleta: a coleta de 01/11 é um **snapshot único `import`** (sem checkpoints 24h/72h/7d/30d separados); não dá para ver a curva de maturação de cada post, só o lifetime no momento da coleta.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-11-04 (7ª execução)
**O que foi feito:** 1ª análise de audiência sobre a **coleta nova de 01/11** (195 posts medidos / 200 no total) — a primeira safra de dado fresco desde o import de 11/10. Reteste do token do `.env` do Mac (resultado: **ainda expirado 26/08**, arquivo inalterado). Reconfirmação de que não há arquivo de demografia/comentários no repo. Reanálise completa: formato, hook, série, foto, janela (dias distintos), contagem de comentários, top 10%/bottom 25%.

**O que mudou desde a última execução (10/28):**
- **Coleta nova (01/11):** de 178→**195 posts medidos** (185→200 total). Toda a safra pós-11/10 — antes invisível — **finalmente tem número**: o burst 26–31/10, os `card_*`, `vs_005`, `der_cafeina_dose_timing`, o lactato 947, o Gatorade×Powerade 699.
- **Seguidores despencaram:** de 9.516 (último dado que esta rotina via) para **9.086 (−430)** — a **1ª queda grande** da conta, agora visível aqui. (Diagnóstico de causa — blackout de 14d + burst fraco — está em `current_strategy.md`/`learnings.md`, já filado pela revisão estratégica de 01/11.)
- **Carga de carbo re-medida em 1.840** (era 1.661) — segue sendo o pico de salvamento da conta (saves/r 0,049).
- **Versus com n=9:** o split mainstream (699/495) × nicho (≤294) ficou ainda mais nítido.
- **Foto subiu a n=6, mediana 469 (acima do baseline)** — hipótese atualizada de "não é a alavanca" para "andando acima do baseline, confundida com hook contrarian, confirmar em n≥10".
- **Janelas:** 14h UTC emergiu como o slot **forte e limpo** (469, 8 dias distintos); 15h segue confundida por lote; 11h (onde a automação publica) é fraca e limpa (301).

**Achados reconfirmados (estáveis em 7 coletas):** carrossel domina (366 vs 256 vs 212); contrarian > myth (430/0,0166 vs 312/0,0113); comparação de produto compartilha e concentra os poucos comentários; suplemento/versus de nicho no fundo; audiência salva/compartilha e quase não comenta (mediana 0, Reel de nitrato outlier com 16).

**Bloqueios que persistem:** demografia e **texto** de comentários **não medíveis** (token do Mac expirado, sem arquivo próprio commitado); follows/reach ausente do snapshot.

**A confirmar na próxima execução:**
- Se o −430 continuou, estabilizou ou reverteu (depende de nova coleta).
- Foto como alavanca com **n≥10** (hoje n=6, confundida com contrarian).
- `card_*` após ≥4 semanas (hoje n=4, dentro da janela de observação do Victor).
- Se o token do Mac foi **regerado** ou se entrou o passo de Actions que commita demografia/comentários — aí iniciar demografia + análise temática de comentários (banco de respostas).

### 2026-10-28 (6ª execução)
1ª análise sobre a coleta de 11/10 (178 medidos / 185 total). Token do `.env` do Mac testado: expirado 26/08. Novos formatos agente-era medidos pela 1ª vez (foto n=3, provocativo n=3, versus n=2). Achado de hook: contrarian (n=7, 424, 0,018) > myth (n=16, 312, 0,011). Seguidores fecharam em 9.516 (−13), 1ª semana não-positiva, sem dado novo desde 11/10. Coleta de métricas parada em 11/10 (safra pós-11/10 invisível).

### 2026-10-07 (5ª execução)
Reanálise sobre a coleta de 04/10 (168 posts / 171 total). Reconfirmou bloqueios de token/demografia/comentários no Mac (à época: token vazio, sem `.env`). Baseline carrossel recomputado 474→418. Base 9.418→9.529 (+111). Incorporou correção de integridade das janelas (confundimento por lote; só 8h BRT era sinal limpo).

### 2026-09-30 (4ª execução)
Reanálise (160 posts / 163 total; coleta 27/09). Quadro idêntico ao ciclo 27/09. Base 9.266→9.418 (+152). Carrossel domina; myth-busting vence; comparação compartilha; nicho no fundo; mediana 0 de comentário.

### 2026-09-23 (3ª execução)
Reanálise (151 posts). Diagnóstico do bloqueio de demografia mudou de "token expirado" para **arquitetural** (token só no Actions). Registrados achados operacionais: horário publica ~08h BRT; estático não pausado.

### 2026-09-16 (1ª execução)
Primeira montagem do documento; 135 posts. Graph API falhou por token expirado (26/08). Achados: carrossel > Reel; sono/recuperação maior alcance mediano (1.164); sexta pior dia; audiência salva/compartilha e quase não comenta.

_(As revisões estratégicas e decisões — pausa/enforce do estático, proibição de sexta, famílias vencedoras, retestes, formatos prov_*/foto/versus, volta do card informativo 19h30, claim-check, escalonamento do blackout — estão em `current_strategy.md` e `learnings.md`.)_
