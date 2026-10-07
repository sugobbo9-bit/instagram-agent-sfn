# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo (quarta-feira). SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-10-07_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida por dado próprio.** Faixa etária, gênero, país/cidade e horários de atividade (`online_followers`) seguem **desconhecidos**. Motivo (inalterado e reconfirmado nesta rodada): o token válido da Página existe apenas como **Secret do GitHub Actions** (`secrets.INSTAGRAM_ACCESS_TOKEN`) e esta rotina roda **no Mac**, fora do Actions — `INSTAGRAM_ACCESS_TOKEN` está **vazio** neste ambiente e **não há `.env`**; e **não há arquivo de demografia commitado** no repo (`data/` não tem `audience_demographics.json` nem `comments_recent.json`). Ver "Demografia — bloqueio".
- Base declarada no projeto: **9.529 seguidores** (+111 na semana; snapshot da revisão de 04/10 em `current_strategy.md`). Crescimento desacelerou vs. o pico anterior (+152) mas segue positivo, apesar do alcance recente fraco. Conta `sofatosnutricao`, IG id `17841472609243044`.
- Perfil presumido pelo nicho (hipótese, **não medido**): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 168 posts com métricas reais, coleta de 04/10/2026; 171 posts no total; posts de 05–06/10 ainda sem métrica)
- **O carrossel domina — padrão forte e repetido em todas as coletas (16/09 → 04/10).**

  | formato | n | alcance mediano | p90 | p75 | p25 | média saves/r | média shares/r | média likes/r | média comments/r |
  |---|---|---|---|---|---|---|---|---|---|
  | **carrossel** | 69 | **418** | 1.219 | 828 | 196 | 0,0193 | 0,0145 | 0,0417 | 0,0012 |
  | reel | 77 | 256 | 515 | 381 | 168 | 0,0068 | 0,0040 | 0,0135 | 0,0010 |
  | estático | 22 | 209 | 356 | 272 | 168 | 0,0125 | 0,0069 | 0,0325 | 0,0018 |

  Dos posts de maior alcance da conta (top 10%), a esmagadora maioria são carrosséis; os maiores alcances vão de ~900 a 2.450. Entre os 25% de menor alcance, os Reels dominam, com carrosséis fracos e alguns estáticos no fundo.
- **Baseline do carrossel recuou:** mediana all-time **418** (n=69), contra 474 na coleta de 27/09 — os grandes carrosséis de maio–julho pesam menos à medida que a base cresce. A **janela recente segue muito abaixo do baseline**: últimos 14 dias mediana **242** (n=8 carrosséis), últimos 7 dias **204** (n=4); o post medido mais recente é de **03/10** (a coleta foi 04/10). Causa dominante apontada pela estratégia: quase todo carrossel recente saiu **~11h UTC / 8h BRT** (a janela fraca, mediana 269) e a série estática diária seguia no fundo — **execução, não tópico**.
- **Temas que mais engajam (hierarquia estável das coletas anteriores; só 36/168 posts têm tópico estruturado — os 132 "historico_pre_agente" não têm categoria):** sono/recuperação > timing/janela > comparação/ranking (maior shares/reach) > hidratação/eletrólitos (maior densidade save+share) > mito genérico. Mais fraco e com teto baixo confirmado: **suplemento de nicho** (BCAA, cetonas exógenas, antioxidantes) e saúde hormonal. _(Não recalculado com bucketing grosseiro nesta rodada; a hierarquia vem da categorização estruturada + captions das coletas anteriores sobre essencialmente os mesmos posts.)_
- **Estrutura vencedora confirmada:** os maiores alcances derrubam uma crença aceita e entregam protocolo — lactato não é vilão (2.450 / 1.516), privação de sono e composição (2.437), cafeína não desidrata (1.558), 60 g carbo/h exige intestino treinado (1.426), creatina (1.249), hidrogel comparado (1.245), janela de 30 min (1.212), magnésio/sono (1.164). Todos de maio–julho; **nenhum vencedor novo de grande alcance apareceu na janela recente** (os recentes são medianos). Comparação concreta de produto é o que mais gera compartilhamento.

### O que eles comentam
- **A audiência salva e compartilha, mas quase não comenta** — comportamento idêntico em todas as coletas. **90 comentários** somando 168 posts; apenas **37 posts com ≥1** comentário; **mediana de 0 por post**. Comentar não é o comportamento dominante.
- Maior ímã de comentário (contagem, não texto): **Reel de nitrato (~16 comentários)**, muito acima de tudo; depois um pelotão de ~4–5 em Reels/carrosséis de **comparação de produto** (maltodextrina, ranking de carboidrato, hidrogel, "15 g de carbo/h", gel) e no carrossel de **magnésio/sono** (1.164 de alcance, 4 comentários). Hipótese fraca (poucos casos): perguntas "serve pra mim?" concentram-se em **comparação de produto**.
- **Análise temática do TEXTO dos comentários: ainda não executada** — depende da Graph API com escopo `instagram_manage_comments`, inacessível a esta rotina (ver abaixo). O `posts_db.json` guarda só a **contagem** de comentários, não o texto.

### Implicação de conteúdo (o que os dados sustentam)
Otimizar para **salvável/compartilhável** (carrossel de mito + comparação de produto), não para "pergunta no fim que peça comentário". Priorizar fueling / hidratação / sono / cafeína / comparação de produto; reduzir suplemento de nicho. A alavanca de alcance mais provável segue sendo **tirar o carrossel da janela de 8h BRT (11h UTC)** — mas ver a ressalva de confundimento abaixo antes de tratar qualquer horário como regra fechada.

### Janelas de publicação (carrossel, BRT) — LER COM A RESSALVA DE LOTE
- **Por dia:** segunda **668** (n=14) e terça **630** (n=5) no topo; quinta 590 (n=8); quarta 412 (n=10); **sexta é o pior (236, n=32)** — e concentra o maior volume histórico. _Não há carrossel medido em fim de semana._
- **Por hora:** 12h BRT = **828** (n=17), 15h BRT = 762 (n=9), 17h = 754 (n=2), 16h = 594 (n=6); **8h BRT = 269 (n=13) — a janela fraca, e é onde a automação realmente publica**; 13h–14h são os piores (158–212).
- **⚠️ Ressalva de integridade (registrada em `learnings.md`, 06/10):** a leitura "12h/15h BRT rende ~3x" está **confundida por lote** — dos 17 carrosséis de 12h BRT (15h UTC), 8 saíram no mesmo dia (03/07) e 6 em 07/08; as faixas "piores" de fim de tarde são quase inteiras o lote de 07/08 (17 posts num dia só). O **único sinal limpo por dias distintos é 8h BRT (11h UTC), n=13, mediana 269** — e coincide com a fase de carrossel só-texto. "Pior dia = sexta" (n=32) também concentra lotes. **Tratar horário/dia como teste a validar (≥10 posts por janela em dias distintos), não como fato.**

---

## ⚠️ Achados operacionais (status das alavancas — contexto de `current_strategy.md` 04/10 e `learnings.md`)
1. **Estático "você sabia" — pausa agora ENFORÇADA EM CÓDIGO (04/10).** A flag `STATIC_PAUSED` no `publisher.py` faz o publisher recusar qualquer item `static`. Era a decisão que ficou 4 semanas só no documento. Resolvido no único chokepoint que o loop semanal controla.
2. **Horário (12h BRT / 15h UTC) ainda depende da rotina DIÁRIA e do cron.** O `publisher.py` ignora `scheduled_for`; quem define o horário é o cron do `publish.yml` (`0 12 * * *` UTC) e os `workflow_dispatch` da rotina diária (~11h). Mover `0 12`→`0 15` precisa de permissão de Workflows no token (que o token fine-grained não tem) — **escalado ao Victor**.
3. **Novidades de 06/10 (decididas com o Victor) — ainda SEM dado próprio para medir:** novo carrossel provocativo diário com imagens (`prov_*`, ~17h BRT); carrossel técnico passa a ter foto na capa + miolo e hook mais afiado (~12h BRT); rotina diária passa a consumir a fila `der_*` (derivados de vencedores) antes de criar tema novo; quality gate ganhou travas em código. **Nenhum `prov_*` nem carrossel-com-foto tem métrica ainda** (coleta é de 04/10; esses posts são de 05–06/10 em diante).

_Estes são achados de observação; esta rotina é só de estudo e não altera nada._

---

## Demografia — bloqueio (arquitetural, inalterado)
- O token válido da Página é gravado como **Secret do GitHub Actions** (`secrets.INSTAGRAM_ACCESS_TOKEN`). Secrets do GitHub são **write-only** — não podem ser lidos de volta.
- Esta rotina roda **no Mac**, fora do Actions, então **não alcança o token** (confirmado nesta rodada: `INSTAGRAM_ACCESS_TOKEN` vazio, sem `.env`; `scripts/instagram_api.py` lê o token de `INSTAGRAM_ACCESS_TOKEN`). Nenhuma chamada à Graph API (`follower_demographics`/`engaged_audience` com breakdown age/gender/city/country, `online_followers`, `{media-id}/comments`) é possível a partir daqui.
- **Não há arquivo de dado próprio de demografia/comentários commitado** no repo (verificado nesta rodada).

**Para desbloquear (decisão do Victor):**
- **(preferida)** Adicionar um passo no **GitHub Actions** (ex.: estender `bootstrap.py`/`analytics_collector.py`) que puxe `follower_demographics`/`online_followers` **e o texto dos comentários** dos ~15 posts recentes e faça **commit** de um JSON no repo (`data/audience_demographics.json`, `data/comments_recent.json`). Aí esta rotina passa a ler dado próprio — sem precisar do token no Mac.
- **(alternativa, menos segura)** Colocar um token de leitura válido (com `instagram_manage_insights` e `instagram_manage_comments`) acessível ao Mac — duplica credencial fora do Actions.

> Nomes de métricas: a Graph API depreciou `audience_*`; o vigente é `follower_demographics` (e/ou `engaged_audience`) com `breakdown` em `age`/`gender`/`city`/`country`, e `online_followers` para horários. Requisito mínimo de seguidores (9,5k) costuma ser atendido; confirmar permissão/escopo ao instrumentar.

---

## Comentários — PENDENTE de instrumentação + escopo `instagram_manage_comments`
O estudo do **texto** dos comentários dos posts recentes continua **não executado**, por dois bloqueios encadeados: (1) o token só existe no Actions, inacessível a esta rotina no Mac; (2) ler (e futuramente responder) comentários exige o escopo **`instagram_manage_comments`** — o mesmo necessário para responder no futuro. Enquanto isso, o levantamento de sentimento e das perguntas/objeções mais frequentes (embrião do futuro **banco de respostas**) fica parado. O que dá para dizer só por contagem: volume baixíssimo (90 comentários / 168 posts, mediana 0), concentrado em **comparação de produto** e no **Reel de nitrato**.

---

## Lacunas de dados (o que ainda não conseguimos medir)
- Demografia (idade/gênero/local) e `online_followers` — bloqueado pelo acesso ao token (acima).
- **follows/reach** e `profile_visits` por post — não vêm no import atual do `posts_db.json`; conversão em seguidor segue **cega no nível do post** (só o agregado é visível, e está saudável: +111/semana).
- Texto/sentimento dos comentários — ver seção acima.
- Efeito dos novos formatos de 06/10 (`prov_*`, carrossel com foto) — sem métrica até a próxima coleta.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-10-07 (5ª execução)
**O que foi feito:** re-análise completa de engajamento sobre a **nova coleta de 04/10** do `posts_db.json` (168 posts com métricas / 171 no total). Reconfirmação dos bloqueios de token/demografia/comentários no Mac (token vazio, sem `.env`, sem arquivo próprio commitado). O documento vivo foi alinhado ao dataset de 04/10 e às decisões da revisão de 04–06/10.

**O que mudou desde a última execução (30/09):**
- **Chegou uma coleta nova (04/10).** O doc anterior refletia a coleta de 27/09 (160 posts); agora há **168 posts medidos**, todos com `collected_at = 2026-10-04`. O post medido mais recente é de **03/10**; os posts de 05–06/10 (inclui os novos `prov_*` e carrosséis com foto) **ainda não têm métrica**.
- **Baseline do carrossel recomputado para baixo: 474 → 418** (n 65→69). Janela recente segue fraca: 14d=242 (n=8), 7d=204 (n=4). Alinha com `current_strategy.md` (04/10).
- **Base de seguidores:** 9.418 → **9.529** (+111; abaixo do pico de +152, ainda positivo).
- **Decisões de estratégia implementadas/novas desde 30/09:** `STATIC_PAUSED` agora **em código** no `publisher.py` (04/10); novos formatos diários decididos em 06/10 (`prov_*` provocativo com imagem; carrossel técnico com foto; rotina diária consome fila `der_*`; travas no quality gate).
- **Correção de integridade incorporada ao resumo:** a vantagem de "12h/15h BRT ~3x" está **confundida por lote** (registrado em `learnings.md` 06/10). O resumo de janelas agora traz essa ressalva; só 8h BRT (n=13, dias distintos) é sinal limpo.

**Achados reconfirmados (estáveis em 5 coletas):** carrossel domina (418 vs reel 256 vs estático 209); myth-busting + protocolo prático vence; comparação de produto gera compartilhamento; suplemento de nicho no fundo; audiência salva/compartilha e quase não comenta (90 comentários, mediana 0, Reel de nitrato como outlier de comentário); nenhum vencedor novo de grande alcance na janela recente.

**Bloqueios que persistem:** demografia e texto de comentários seguem **não medíveis** por esta rotina — sem token acessível no Mac e sem arquivo de dado próprio commitado. Depende de instrumentação no Actions (+ escopo `instagram_manage_comments` para comentários).

**A confirmar na próxima execução:**
- Se houve **nova coleta** após 04/10, para finalmente medir os `prov_*` e os carrosséis com foto (hipótese de 06/10: provocativo com imagem teve shares/reach ~4,5% num único post — medir em ≥10).
- Se o cron de horário (15h UTC) e o consumo da fila `der_*` chegaram de fato à rotina diária (render + approve), subindo o alcance mediano do carrossel para 500+.
- Se foi criado o **passo de Actions** que commita demografia/comentários — e, se sim, iniciar a análise demográfica e temática dos comentários com dado próprio.

### 2026-09-30 (4ª execução)
Re-análise de engajamento sobre `posts_db.json` (160 posts / 163 total; coleta de 27/09). Nenhuma coleta nova desde 27/09 à época — quadro idêntico ao do ciclo 27/09. Documento alinhado ao dataset de 160 posts; base 9.266→9.418 (+152). Reconfirmado: carrossel domina; myth-busting vence; comparação de produto compartilha; nicho no fundo; mediana 0 de comentário; alcance recente de carrossel abaixo do baseline (319 vs 474). Bloqueios de demografia/comentários persistem.

### 2026-09-23 (3ª execução)
Re-análise de engajamento (151 posts). Sem novos posts medidos desde 19/09. Diagnóstico do bloqueio de demografia mudou de "token expirado" para **arquitetural** (token só no Actions, inalcançável do Mac). Recomendação: instrumentar passo no Actions que commite demografia/comentários. Registrados dois achados operacionais: horário não corrigido (publica ~08h BRT) e estático não pausado.

### 2026-09-16 (1ª execução desta rotina)
Primeira montagem do documento; análise de engajamento com 135 posts. Graph API falhou por **token expirado (26/08)**. Achados: carrossel > Reel; sono/recuperação é o tema de maior alcance mediano (1.164); sexta é o pior dia; audiência salva/compartilha e quase não comenta (mediana 0).

_(A revisão estratégica de 20/09 e os ciclos de 27/09 e 04–06/10 — pausa/enforce do estático, proibição de sexta, padrão 12h BRT, corte de suplemento de nicho, família "carga de carbo", reteste de sono, novos formatos `prov_*`/foto — estão em `current_strategy.md` e `learnings.md`.)_
