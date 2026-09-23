# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo (quarta-feira). SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-09-23_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida por dado próprio.** Faixa etária, gênero, país/cidade e horários de atividade dos seguidores (`online_followers`) seguem **desconhecidos**. O motivo mudou desde as rodadas anteriores (ver "Demografia — bloqueio" abaixo): o token não está mais expirado, mas **não é acessível a esta rotina** — ele existe apenas como *Secret* do GitHub Actions, e esta execução roda no Mac, fora do Actions.
- Base declarada no projeto: **9.266 seguidores** (performance_history.json, snapshot 20/09/2026; +137 desde 09/09). Conta `sofatosnutricao`, IG id `17841472609243044`.
- Perfil presumido pelo nicho (hipótese, **não medido**): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 151 posts com métricas reais, fev–set/2026; 156 posts no total)
- **O carrossel domina — padrão forte e repetido, não ruído de amostra.**

  | formato | n | alcance mediano | saves/reach | shares/reach | likes/reach | comments/reach |
  |---|---|---|---|---|---|---|
  | **carrossel** | 61 | **495** | 0,0177 | 0,0097 | 0,0374 | 0,0 |
  | reel | 77 | 256 | 0,0052 | 0,0 | 0,011 | 0,0 |
  | estático | 13 | 231 | 0,0121 | 0,0056 | 0,0286 | 0,0 |

  Dos 15 posts de maior alcance da conta, **14 são carrosséis** (1 Reel). Dos 25% de menor alcance (n=38), a maioria é Reel (21) e estático/carrossel fraco (13 carrosséis, 4 estáticos).
- **Comparação de mesma janela (últimos 14 dias — o teste limpo):** 9 carrosséis (mediano **607**) contra 7 estáticos (mediano **195**), **0 Reels**. Mesma semana, mesmo público — carrossel entrega ~3x. O carrossel recente (607) está acima da própria mediana histórica (495).
- **Temas que mais engajam (por alcance mediano de carrossel, normalizado):** sono/recuperação (1.164, n=9) > timing/janela (630, n=11) > comparação/ranking (515, n=23, **maior shares/reach**) > hidratação/eletrólitos (487, n=8, **maior densidade de save+share**) > mito genérico (466, n=26). Mais fraco: **suplemento de nicho** — BCAA (131), cetonas exógenas (134), antioxidantes (204) no fundo; saúde hormonal (155, n=5).
- **Estrutura vencedora confirmada:** os maiores alcances derrubam uma crença aceita — lactato não é vilão (2.450 / 1.516), privação de sono e composição (2.437), cafeína não desidrata (1.558), 60 g carbo/h exige intestino treinado (1.426), creatina (1.249), hidrogel comparado (1.245), janela de 30 min (1.212), detox é marketing (1.046). Comparação concreta de produto ("Uno vs Ferrari" de carboidrato) é o que mais gera compartilhamento.

### O que eles comentam
- **A audiência salva e compartilha, mas quase não comenta.** ~88 comentários somando 151 posts; apenas 35 posts com ≥1 comentário; **mediana de 0 por post**. Comentar não é o comportamento dominante.
- Maiores ímãs de comentário (contagem, não texto): **Reel de nitrato** (~16), e Reels/carrosséis de **comparação de produto** (maltodextrina, ranking de carboidrato em pó, hidrogel, "15 g de carbo/h") — todos ~4–5. Hipótese fraca (poucos casos): perguntas do tipo "serve pra mim?" concentram-se em conteúdo de **comparação de produto**.
- **Análise temática do TEXTO dos comentários: ainda não executada** — depende da Graph API com escopo `instagram_manage_comments`, inacessível a esta rotina (ver abaixo). O `posts_db.json` guarda só a **contagem** de comentários, não o texto.

### Implicação de conteúdo (o que os dados sustentam)
Otimizar para **salvável/compartilhável** (carrossel de mito + comparação de produto), não para "pergunta no fim que peça comentário". Priorizar fueling / hidratação / sono / cafeína / comparação de produto; reduzir suplemento de nicho. Publicar carrossel **fora da sexta** e às **12h BRT** (ver janelas abaixo).

### Janelas de publicação (carrossel, normalizado)
- **Por dia (BRT):** segunda 722 (n=12) e quinta 679 (n=6) são os melhores; **sexta é o pior (256, n=31)** — e é onde está o maior volume histórico.
- **Por hora (BRT):** **12h BRT (15h UTC) = mediana 828** (n=17), a melhor janela; 15h (751) e 17h (750) também fortes; **13h–14h BRT são os piores (157–212)**; 8h BRT é fraco (302, n=5).

---

## ⚠️ Achados operacionais desta rodada (decisões da estratégia NÃO implementadas na automação)
Duas decisões-chave do ciclo (revisão de 2026-09-20) **não estão refletidas no que a automação realmente publica** — vale conferir, porque anulam o benefício das principais alavancas identificadas:

1. **Horário de publicação — a melhor alavanca não está ligada.** A estratégia decidiu publicar às **12h BRT (15h UTC)** — a janela de maior alcance (mediana 828). Mas o cron do `publish.yml` é `0 12 * * *` **UTC = 09h BRT**, e os carrosséis dos dias 18–23/09 saíram todos por volta de **08h20 BRT** (janela fraca, mediana histórica 302). Ou seja: a conta continua publicando no horário fraco da manhã, não no horário forte do meio-dia. **Correção sugerida:** mudar o cron para `0 15 * * *` (= 12h BRT). *(Observação — não medível ainda: os posts de 21–23/09 ainda não têm métricas.)*
2. **Série estática "você sabia" — decidida a pausa, mas ainda publicando.** A revisão de 20/09 decidiu **pausar** a série. Ainda saíram estáticos em 19/09, 20/09 e 22/09 (17h BRT). Podem ser itens já enfileirados; confirmar que a fila foi limpa dos estáticos.

_Estes são achados de observação; a rotina é só de estudo e não altera nada._

---

## Demografia — bloqueio (mudou de natureza)
Rodadas anteriores registraram o token **expirado** (26/08/2026, OAuth 190/463). O bootstrap de 20/09 **revalidou** um Page Token de longa duração (não expira). Porém, na arquitetura atual:

- O token válido é gravado como **Secret do GitHub Actions** (`secrets.INSTAGRAM_ACCESS_TOKEN`), por `token_exchange.py` via `gh secret set`. Secrets do GitHub são **write-only** — não podem ser lidos de volta.
- O `.env` local no Mac (`Instagram Agent/.env`) contém apenas **placeholders** (`your_...`), não o token real.
- Esta rotina de estudo roda **no Mac**, fora do GitHub Actions, então **não alcança o token** — nenhuma chamada à Graph API (`follower_demographics` / `engaged_audience` com breakdown age/gender/city/country, `online_followers`, ou `{media-id}/comments`) é possível a partir daqui.

**Para desbloquear (uma das opções, decisão do Victor):**
- **(preferida)** Adicionar um passo no GitHub Actions (ex.: estender `bootstrap.py`/`analytics_collector.py`) que puxe `follower_demographics`/`online_followers` e o **texto dos comentários** dos ~15 posts recentes e faça **commit** de um JSON no repo (ex.: `data/audience_demographics.json`, `data/comments_recent.json`). Aí esta rotina passa a ler dado próprio de demografia e comentários — sem precisar do token no Mac.
- **(alternativa)** Colocar um token de leitura válido (com `instagram_manage_insights` e `instagram_manage_comments`) no `.env` do Mac — porém isso duplica credencial fora do Actions e é menos seguro.

> Nota sobre nomes de métricas: a Graph API depreciou `audience_*`; o vigente para demografia é `follower_demographics` (e/ou `engaged_audience`) com `breakdown` em `age`/`gender`/`city`/`country`, e `online_followers` para horários. Requisito mínimo de seguidores para expor demografia costuma ser atendido (9,2k), mas confirmar permissão/escopo ao instrumentar.

---

## Comentários — PENDENTE de instrumentação + escopo
O estudo do **texto** dos comentários dos posts recentes continua **não executado**. Dois bloqueios encadeados:
1. **Acesso ao token:** como acima, o token só existe no Actions; esta rotina no Mac não o alcança, logo não chama `{media-id}/comments`.
2. **Escopo:** mesmo com token acessível, ler (e futuramente responder) comentários exige o escopo **`instagram_manage_comments`**. Confirmar que ele está presente no token ao instrumentar.

Enquanto isso, o levantamento de sentimento e das perguntas/objeções mais frequentes (embrião do futuro banco de respostas) fica parado. O que dá para dizer hoje, só por contagem: o volume de comentários é baixíssimo e se concentra em **comparação de produto** e no **Reel de nitrato**.

---

## Lacunas de dados (o que ainda não conseguimos medir)
- Demografia (idade/gênero/local) e `online_followers` — bloqueado pelo acesso ao token (acima).
- **follows/reach** e `profile_visits` por post — não vêm no import atual do `posts_db.json`; não medível a partir do dado atual. Métrica-alvo para instrumentar (permitiria otimizar por conversão em seguidor, não só por alcance).
- Texto/sentimento dos comentários — ver seção acima.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-09-23 (3ª execução)
**O que foi feito:** re-análise completa de engajamento a partir de `posts_db.json` (151 posts com métricas / 156 no total). Nova tentativa de acessar demografia e comentários via Graph API.

**O que mudou desde a última vez:**
- **Sem novos posts medidos** desde 19/09 — o post mais recente COM métrica é de 19/09 (coleta de 20/09). Os 5 posts de 20–23/09 ainda não têm métricas. Portanto o **quadro de engajamento não mudou** em relação à revisão de 20/09: carrossel domina, myth-busting vence, comparação de produto gera compartilhamento, suplemento de nicho no fundo, sexta é o pior dia, 12h BRT o melhor horário, audiência salva/compartilha e quase não comenta. **Tudo reconfirmado, nada novo no engajamento.**
- **Diagnóstico do bloqueio de demografia mudou de natureza:** não é mais "token expirado" (como em 16/09) — o token foi revalidado em 20/09. Agora o bloqueio é **arquitetural**: o token vive só como Secret do GitHub Actions e esta rotina no Mac não o alcança. Isso muda a recomendação: em vez de "renovar token", o caminho é **instrumentar um passo no Actions que faça commit da demografia/comentários** (ver seção Demografia).

**Achados novos (observação operacional):**
1. **A melhor alavanca de horário não está implementada.** Estratégia quer 12h BRT (mediana 828); a automação publica ~08–09h BRT (`cron 0 12 * * *` UTC). Correção: `cron 0 15 * * *`.
2. **A pausa da série estática ainda não valeu na prática** — estáticos publicados em 19, 20 e 22/09.

**A confirmar na próxima execução:**
- Se o horário de publicação foi corrigido para 12h BRT e se isso subiu o alcance mediano dos carrosséis novos.
- Se a série estática parou de fato.
- Se foi criado o passo de Actions para commit de demografia/comentários — e, se sim, começar a análise demográfica e temática de comentários com dado próprio.

### 2026-09-16 (1ª execução desta rotina)
**Feito:** primeira montagem do documento; análise de engajamento com 135 posts. Tentativa de Graph API falhou por **token expirado (26/08)**. Victor notificado para renovar token e reconfirmar escopo `instagram_manage_comments`.
**Achados:** carrossel > Reel confirmado com n maior; sono/recuperação é o tema de maior alcance mediano (1.164); sexta é o pior dia; audiência salva/compartilha e quase não comenta (mediana 0).

_(A revisão estratégica de 2026-09-20 — pausa do estático, proibição de sexta, padrão 12h BRT, corte de suplemento de nicho — está registrada em `current_strategy.md` e `learnings.md`)._
