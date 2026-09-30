# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo (quarta-feira). SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-09-30_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida por dado próprio.** Faixa etária, gênero, país/cidade e horários de atividade (`online_followers`) seguem **desconhecidos**. Motivo (inalterado): o token válido da Página existe apenas como **Secret do GitHub Actions** e esta rotina roda **no Mac**, fora do Actions, então não o alcança; e **não há arquivo de demografia commitado** no repo (`data/` não tem `audience_demographics.json` nem `comments_recent.json`). Ver "Demografia — bloqueio".
- Base declarada no projeto: **9.418 seguidores** (snapshot 27/09/2026; +152 na semana — a melhor semana registrada). Conta `sofatosnutricao`, IG id `17841472609243044`.
- Perfil presumido pelo nicho (hipótese, **não medido**): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 160 posts com métricas reais, fev–set/2026; coleta única de 27/09; 163 posts no total)
- **O carrossel domina — padrão forte e repetido, não ruído de amostra.**

  | formato | n | alcance mediano | p90 | p75 | p25 | saves/reach | shares/reach | likes/reach | comments/reach |
  |---|---|---|---|---|---|---|---|---|---|
  | **carrossel** | 65 | **474** | 1.245 | 838 | 197 | 0,0177 | 0,0095 | 0,0374 | 0,0 |
  | reel | 77 | 256 | 520 | 381 | 168 | 0,0052 | 0,0 | 0,011 | 0,0 |
  | estático | 18 | 207 | 423 | 330 | 150 | 0,0116 | 0,0083 | 0,0306 | 0,0 |

  Dos 16 posts de maior alcance da conta (top 10%), **15 são carrosséis** (1 Reel), faixa 901–2.450. Dos 25% de menor alcance (n=40): **21 Reels**, 13 carrosséis fracos, 6 estáticos.
- **Comparação de mesma janela (últimos 14 dias — o teste limpo):** 8 carrosséis (mediano **319**) contra 10 estáticos (mediano **166**), **0 Reels**. Mesma semana, mesmo público — carrossel entrega ~2x o estático. Porém o carrossel recente (319) está **abaixo da própria mediana histórica (474)**: os grandes carrosséis de início de setembro saíram da janela e os recentes são medianos.
- **Temas que mais engajam (hierarquia mantida da categorização anterior sobre o MESMO dado; por alcance mediano de carrossel):** sono/recuperação (~1.164, n=9) > timing/janela (~630, n=11) > comparação/ranking (~515, n=23, **maior shares/reach**) > hidratação/eletrólitos (~487, n=8, **maior densidade save+share**) > mito genérico (~466, n=26). Mais fraco: **suplemento de nicho** — BCAA (131), cetonas exógenas (134/168), antioxidantes (204) no fundo; saúde hormonal (155, n=5). _(Nesta rodada o dataset é idêntico ao de 27/09; a hierarquia de tópico é reconfirmada, não recalculada com bucketing grosseiro.)_
- **Estrutura vencedora confirmada:** os maiores alcances derrubam uma crença aceita — lactato não é vilão (2.450 / 1.516), privação de sono e composição (2.437), cafeína não desidrata (1.558), 60 g carbo/h exige intestino treinado (1.426), creatina (1.249), hidrogel comparado (1.245), janela de 30 min (1.212). Vencedores recentes do ciclo: **carga de carboidrato/depleção (918, saves/reach 0,039 — maior salvamento do ciclo)** e **cafeína (975)**. Comparação concreta de produto ("Uno vs Ferrari") é o que mais gera compartilhamento.

### O que eles comentam
- **A audiência salva e compartilha, mas quase não comenta.** 89 comentários somando 160 posts; apenas **36 posts com ≥1** comentário; **mediana de 0 por post**. Comentar não é o comportamento dominante.
- Maior ímã de comentário (contagem, não texto): **Reel de nitrato (~16 comentários)**, muito acima de tudo; depois um pelotão de ~4–5 em Reels/carrosséis de **comparação de produto** e no carrossel de **sono** (1.164 de alcance, 4 comentários). Hipótese fraca (poucos casos): perguntas "serve pra mim?" concentram-se em **comparação de produto**.
- **Análise temática do TEXTO dos comentários: ainda não executada** — depende da Graph API com escopo `instagram_manage_comments`, inacessível a esta rotina (ver abaixo). O `posts_db.json` guarda só a **contagem** de comentários, não o texto.

### Implicação de conteúdo (o que os dados sustentam)
Otimizar para **salvável/compartilhável** (carrossel de mito + comparação de produto), não para "pergunta no fim que peça comentário". Priorizar fueling / hidratação / sono / cafeína / comparação de produto; reduzir suplemento de nicho. Publicar carrossel **fora da sexta** e às **12h BRT** (ver janelas). Alerta de execução: bom tópico morre com hook/timing fracos (sono fez 178 com hook mole + 11h UTC, sendo o tópico de maior mediana da conta).

### Janelas de publicação (carrossel, BRT)
- **Por dia:** quinta **762** (n=7) e segunda **682** (n=13) são os melhores; terça 630 (n=5); quarta 459 (n=9); **sexta é o pior (256, n=31)** — e concentra o maior volume histórico.
- **Por hora:** **12h BRT = mediana 828** (n=17), a melhor janela; 15h (762) e 17h (753) também fortes; 16h (594); **13h–14h são os piores (158–212)**; **8h BRT é fraco (317, n=9)** — e é o horário em que a automação realmente publica.

---

## ⚠️ Achados operacionais (decisões da estratégia ainda NÃO implementadas na automação)
Reincidente há 3+ semanas (contexto de `learnings.md`/`current_strategy.md`, ciclo 27/09). Duas alavancas continuam desligadas:

1. **Horário — a melhor alavanca não está ligada.** A estratégia quer publicar às **12h BRT (15h UTC)** (mediana 828). Mas os carrosséis saem ~**08h BRT / 11h UTC** (mediana ~317), a janela fraca. Causa técnica (ciclo 27/09): o `publisher.py` **ignora `scheduled_for`**; quem define o horário são os `workflow_dispatch` da rotina **DIÁRIA** + o cron do `publish.yml` (`0 12 * * *` UTC). A tentativa do loop semanal de mover `0 12`→`0 15` foi **bloqueada** (PAT sem escopo `workflow`; push rejeitado) → escalado ao Victor.
2. **Série estática "você sabia" — decidida a pausa, ainda publicando.** ~10–11 estáticos nos últimos 14 dias, um por dia às 20h UTC, todos no fundo (116–242). A pausa precisa ser aplicada na rotina **DIÁRIA**, não só no documento/fila.

_Estes são achados de observação; esta rotina é só de estudo e não altera nada._

---

## Demografia — bloqueio (arquitetural, inalterado)
- O token válido da Página (revalidado no bootstrap de 20/09, não expira) é gravado como **Secret do GitHub Actions** (`secrets.INSTAGRAM_ACCESS_TOKEN`). Secrets do GitHub são **write-only** — não podem ser lidos de volta.
- Esta rotina roda **no Mac**, fora do Actions, então **não alcança o token**: nenhuma chamada à Graph API (`follower_demographics`/`engaged_audience` com breakdown age/gender/city/country, `online_followers`, `{media-id}/comments`) é possível a partir daqui.
- **Não há arquivo de dado próprio de demografia/comentários commitado** no repo (verificado nesta rodada: `data/` não contém `audience_demographics.json` nem `comments_recent.json`).

**Para desbloquear (decisão do Victor):**
- **(preferida)** Adicionar um passo no **GitHub Actions** (ex.: estender `bootstrap.py`/`analytics_collector.py`) que puxe `follower_demographics`/`online_followers` **e o texto dos comentários** dos ~15 posts recentes e faça **commit** de um JSON no repo (`data/audience_demographics.json`, `data/comments_recent.json`). Aí esta rotina passa a ler dado próprio — sem precisar do token no Mac.
- **(alternativa, menos segura)** Colocar um token de leitura válido (com `instagram_manage_insights` e `instagram_manage_comments`) acessível ao Mac — duplica credencial fora do Actions.

> Nomes de métricas: a Graph API depreciou `audience_*`; o vigente é `follower_demographics` (e/ou `engaged_audience`) com `breakdown` em `age`/`gender`/`city`/`country`, e `online_followers` para horários. Requisito mínimo de seguidores (9,4k) costuma ser atendido; confirmar permissão/escopo ao instrumentar.

---

## Comentários — PENDENTE de instrumentação + escopo `instagram_manage_comments`
O estudo do **texto** dos comentários dos posts recentes continua **não executado**, por dois bloqueios encadeados: (1) o token só existe no Actions, inacessível a esta rotina no Mac; (2) ler (e futuramente responder) comentários exige o escopo **`instagram_manage_comments`** — o mesmo necessário para responder no futuro. Enquanto isso, o levantamento de sentimento e das perguntas/objeções mais frequentes (embrião do futuro **banco de respostas**) fica parado. O que dá para dizer só por contagem: volume baixíssimo, concentrado em **comparação de produto** e no **Reel de nitrato**.

---

## Lacunas de dados (o que ainda não conseguimos medir)
- Demografia (idade/gênero/local) e `online_followers` — bloqueado pelo acesso ao token (acima).
- **follows/reach** e `profile_visits` por post — não vêm no import atual do `posts_db.json`; conversão em seguidor segue **cega no nível do post** (só o agregado é visível, e está saudável: +152/semana).
- Texto/sentimento dos comentários — ver seção acima.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-09-30 (4ª execução)
**O que foi feito:** re-análise completa de engajamento sobre `posts_db.json` (160 posts com métricas / 163 no total). Verificação da existência de dado próprio de demografia/comentários (nenhum commitado). Tentativa de checagem de token no Mac foi bloqueada por política de segurança — não é necessária: o caminho de dado próprio (arquivo commitado) é o único válido para esta rotina, e está vazio.

**O que mudou desde a última vez (23/09 no doc; 27/09 na estratégia):**
- **Nenhuma coleta nova de métricas desde 27/09.** Todos os 160 registros têm `collected_at = 2026-09-27`; o post mais recente COM métrica é de **26/09**. Os posts de 27–30/09 (inclui o carrossel de índice glicêmico de 30/09) ainda **não têm métricas**. Portanto o **quadro de engajamento é idêntico** ao do ciclo de 27/09 — nada de novo a medir.
- **O documento vivo foi alinhado ao dataset de 160 posts** (antes refletia 151 posts / base 9.266). Números do perfil, tabela de formato, dia e hora foram **reconfirmados** sobre o dataset completo: carrossel 474 vs reel 256 vs estático 207; top 10% = 15/16 carrosséis; sexta = pior dia (256, n=31); 12h BRT = melhor hora (828, n=17); 8h BRT (onde a conta publica) = 317.
- **Base de seguidores atualizada** no resumo: 9.266 → **9.418** (+152, melhor semana), refletindo o snapshot de 27/09.

**Achados reconfirmados (nada novo no engajamento; mesmo dado):** carrossel domina; myth-busting + protocolo prático vence; comparação de produto gera compartilhamento; suplemento de nicho no fundo; audiência salva/compartilha e quase não comenta (mediana 0); alcance recente de carrossel abaixo do baseline (319 vs 474).

**Bloqueios que persistem:** demografia e texto de comentários seguem **não medíveis** por esta rotina — sem token acessível no Mac e sem arquivo de dado próprio commitado. Depende de instrumentação no Actions (+ escopo `instagram_manage_comments` para comentários).

**A confirmar na próxima execução:**
- Se houve **nova coleta** de métricas após 27/09 (para medir os carrosséis de 27–30/09 e ver se a janela de 12h/15h UTC, se aplicada, subiu o alcance).
- Se foi criado o **passo de Actions** que commita demografia/comentários — e, se sim, iniciar a análise demográfica e temática dos comentários com dado próprio.
- Se o horário de publicação e a pausa do estático finalmente chegaram à rotina diária.

### 2026-09-23 (3ª execução)
Re-análise de engajamento (151 posts). Sem novos posts medidos desde 19/09. Diagnóstico do bloqueio de demografia mudou de "token expirado" para **arquitetural** (token só no Actions, inalcançável do Mac). Recomendação: instrumentar passo no Actions que commite demografia/comentários. Registrados dois achados operacionais: horário não corrigido (publica ~08h BRT) e estático não pausado.

### 2026-09-16 (1ª execução desta rotina)
Primeira montagem do documento; análise de engajamento com 135 posts. Graph API falhou por **token expirado (26/08)**. Achados: carrossel > Reel; sono/recuperação é o tema de maior alcance mediano (1.164); sexta é o pior dia; audiência salva/compartilha e quase não comenta (mediana 0).

_(A revisão estratégica de 20/09 e o ciclo de 27/09 — pausa do estático, proibição de sexta, padrão 12h BRT, corte de suplemento de nicho, família "carga de carbo", reteste de sono — estão em `current_strategy.md` e `learnings.md`.)_
