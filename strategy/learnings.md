# Learnings Acumulados — Instagram Agent
_Última atualização: 2026-09-20_

## Sobre a Conta
9.266 seguidores (snapshot 20/09/2026; +137 desde 09/09). Token da Página revalidado no bootstrap de 20/09 (não expira) — demografia a puxar no próximo ciclo.

## Sobre o Público
A audiência **salva e compartilha, mas quase não comenta**: 81 comentários em 135 posts, mediana 0/post (fev–set/2026). Otimizar para conteúdo salvável/compartilhável, não para pedir comentário. Idade/gênero/local: a preencher quando o token for renovado.

## Sobre Formatos
**Carrossel domina** (confirmado com base ampliada e comparação de mesma janela) (base ampliada, 52 carrosséis vs 77 Reels): alcance mediano 483 vs 256; saves/reach 0,019 vs 0,0052; shares/reach 0,0093 vs 0,000. 12 dos 13 maiores alcances são carrosséis; 21 dos 33 menores são Reels. Carrossel = formato padrão; Reel = experimento controlado (só quando o conteúdo é intrinsecamente visual).

## Sobre Hooks
Estrutura vencedora recorrente: **derrubar uma crença aceita** ("X não é o vilão", "a janela de 30 min não existe", "detox é marketing"). A preencher com dados de hook estruturados (hoje só 13 posts têm o campo hook).

## Sobre Tópicos
Por alcance mediano de carrossel (normalizado): **sono/recuperação 1.164** (n=9) > timing/janela 630 (n=11) > comparação/ranking 515 (n=23, maior shares/reach) > hidratação/eletrólitos 487 (maior saves+shares, n=8) > mito 466 (n=26) > suplemento 357 (n=36). Mais fraco: saúde hormonal (155, n=5). Comparação de produto é o que mais gera compartilhamento.

## Sobre Horários
Carrossel na **sexta-feira** (maior volume, n=29) tem o **pior alcance mediano (256)**; segunda (764) e quinta (854) rendem mais; melhores horários 15h e 18h UTC (12h/15h BRT). Hipótese a testar: tirar carrossel da sexta. (Correlação — validar deslocando publicações e com online_followers quando o token voltar.)


## Sobre Estático (NOVO — 2026-09-20)
A série estática "você sabia" virou a nova ineficiência do sistema — mesmo papel que os Reels tinham. 7 estáticos nos últimos 14 dias, alcance mediano 195, todos no fundo, contra 607 dos carrosséis na MESMA janela. As ideias são boa ciência; o formato/embalagem é o que falha. Decisão: pausar a série e reaproveitar as melhores ideias (ice slurry, mouth rinse) como carrossel.

## Sobre Tópicos (atualização 2026-09-20)
Suplemento de nicho confirmou teto baixo: BCAA (131), cetonas exógenas (134), antioxidantes (204) no fundo do ciclo — problema de tópico, não de hook. Priorizar fueling / hidratação / sono / cafeína / comparação de produto. Maior shares/reach do ciclo: comparação de carboidrato (0,045).

## Mudanças Estratégicas
| Data | O que mudou | Por quê | Evidência |
|------|-------------|---------|-----------|
| 2026-08-26 | Sistema iniciado | FIRST_RUN | — |
| 2026-09-16 | Preenchidos Público/Formatos/Tópicos/Horários com dados reais | 1ª rotina de inteligência de audiência | 135 posts com métricas (posts_db.json) |
| 2026-09-16 | Sinalizado: token Graph API expirado | Bloqueia demografia, comentários e publicação | OAuth 190/463 |
| 2026-09-20 | Pausada a série estática "você sabia" | Estático 195 vs carrossel 607 na mesma janela; nova ineficiência | 151 posts; comparação de mesma janela (14d) |
| 2026-09-20 | Proibido carrossel na sexta; padrão 12h BRT | Sexta n=31 alcance mediano 256 (pior); 12h BRT mediana 828 | posts_db normalizado por dia/hora |
| 2026-09-20 | Reduzir suplemento de nicho; +6 derivados de vencedores | BCAA/cetonas/antioxidantes no fundo; vencedores são myth-busting + comparação | winner_library / failure_log |

## Sobre Implementação vs. Estratégia (NOVO — 2026-09-23)
Achado forte da rotina de audiência: **as duas principais decisões do ciclo de 20/09 não estavam implementadas na automação.**
- **Horário:** a estratégia definiu 12h BRT (15h UTC) como melhor janela (mediana 828 vs. 302 às 8h), mas o cron do `publish.yml` é `0 12 * * *` UTC = 09h BRT, e os posts de 18–23/09 saíram ~08h20 BRT. A melhor alavanca de alcance identificada não estava ligada. Correção: `cron 0 15 * * *`.
- **Estático:** decidida a pausa da série "você sabia" em 20/09, mas estáticos continuaram saindo (19, 20, 22/09).
Lição de processo: validar que decisões da revisão semanal chegam à automação (cron/fila), não só ao documento.

## Ciclo 2026-09-27

### Sobre a Conta
9.418 seguidores (+152 na semana — **melhor semana registrada**). Crescimento acelerou mesmo com alcance recente fraco: sinal de que a conversão por alcance melhorou (poucos carrosséis de alto salvamento puxando follows). follows/reach por post ainda cego (Graph API não entrega).

### Sobre Alcance (NOVO)
Alcance recente de carrossel caiu abaixo do baseline: 14d=320, 7d=296 vs all-time 474. Os grandes carrosséis de início de setembro saíram da janela e os recentes são medianos. Baseline all-time também recuou levemente (495→474) com a base ampliada (n=65).

### Sobre Vencedores/Fracassos (NOVO)
- Vencedor do ciclo: **carga de carboidrato/depleção (918, saves/reach 0,039 — maior do ciclo)**. Protocolo prático + myth-busting = altíssimo salvamento. Família nova para explorar.
- Cafeína (975) reforça a família cafeína como vencedora recorrente; funcionou mesmo às 11h UTC — a força do tópico superou o horário ruim.
- Fracasso-alerta: **extensão de sono (178)** com o tópico de MAIOR mediana da conta (1.164). Causa: hook mole sem número + 11h UTC. Bom tópico morre com hook/timing fracos. Reteste como experimento controlado.
- Cetonas (168, 0/0) e janela anabólica (271) reconfirmam teto baixo de nicho/mito saturado.

### Sobre Implementação vs. Estratégia (REINCIDENTE — 3ª semana)
As MESMAS duas decisões seguem sem chegar à execução:
- **Estáticos não pausados** (11 em 14 dias, todos no fundo, às 20h UTC).
- **Horário não corrigido** (carrosséis às 11h UTC/08h BRT em vez de 15h UTC).
Diagnóstico técnico deste ciclo: o `publisher.py` **ignora `scheduled_for`** — publica o próximo `approved` por prioridade quando dispachado. Quem controla o horário/volume são os `workflow_dispatch` da rotina DIÁRIA (~11h carrossel, ~20h estático) mais o cron do publish.yml. **O loop semanal não controla os dispatches diários.** Ação deste run: **tentativa** de mover o cron `0 12`→`0 15` foi BLOQUEADA (PAT sem escopo `workflow`; push rejeitado) — escalado ao Victor. Escalonamento explícito registrado. Lição de processo: decisões de formato/horário precisam ser aplicadas na rotina DIÁRIA, não só no documento nem na fila.

## Mudanças Estratégicas (continuação)
| Data | O que mudou | Por quê | Evidência |
|------|-------------|---------|-----------|
| 2026-09-27 | (TENTADO) cron 0 12 → 0 15 UTC — bloqueado (PAT sem escopo workflow) | Colocaria a publicação por cron na melhor janela | carrossel 15h UTC mediana 828 vs 11-12h UTC ~317 |
| 2026-09-27 | +2 derivados da família "carga de carbo"; reteste de sono como experimento | Explorar vencedor (918, saves/reach 0,039); recuperar tópico forte que falhou por hook | winner_library / failure_log / experiments |
| 2026-09-27 | Escalado: rotina DIÁRIA deve parar estáticos e dispachar 15h UTC | 3ª semana com as decisões sem implementação | posts_db 14d (11 estáticos, carrosséis 11h UTC) |

## Ciclo 2026-09-30 (rotina de audiência)

### Sobre o Dado (reconfirmação, sem coleta nova)
Sem nova coleta de métricas desde 27/09: os 160 posts medidos têm `collected_at = 2026-09-27` e o post mais recente com métrica é de 26/09. Os carrosséis de 27–30/09 ainda não têm métricas. Quadro de engajamento **idêntico** ao ciclo de 27/09, reconfirmado sobre o dataset completo (carrossel 474 vs reel 256 vs estático 207; sexta pior dia 256/n=31; 12h BRT melhor hora 828/n=17; audiência salva/compartilha e quase não comenta, 89 comentários / mediana 0 em 160 posts). `audience_intelligence.md` foi alinhado de 151→160 posts e base 9.266→9.418.

### Bloqueio de dado próprio (REINCIDENTE — 4 semanas)
Demografia (`follower_demographics`/`online_followers`) e **texto** dos comentários seguem **não medíveis** por esta rotina: o token válido existe só como Secret do GitHub Actions (inalcançável do Mac) e **não há arquivo commitado** (`data/audience_demographics.json` / `data/comments_recent.json`). Desbloqueio depende de **instrumentar um passo no Actions** que commite esses JSONs; comentários exigem também o escopo **`instagram_manage_comments`** (o mesmo para responder no futuro). Enquanto isso, o banco de perguntas/objeções da audiência não pode começar.

## Ciclo 2026-10-04

### Sobre a Conta
9.529 seguidores (+111 na semana; desacelerou vs +152, mas segue positivo). Alcance recente fraco não travou o crescimento — conversão por alcance segue boa. follows/reach por post ainda cego.

### Sobre Alcance (reconfirmado e piorando)
Baseline do carrossel caiu 474→418 (n=69). Janela recente muito abaixo: 14d=241, 7d=204. Causa: quase todo carrossel recente saiu às **11h UTC** (mediana histórica 269) e os estáticos diários seguem no fundo. É execução, não tópico.

### Lição de processo (DEFINITIVA — 4ª semana): parar de só escrever, começar a enforçar em código
As mesmas 2 decisões (pausar estático; publicar 15h UTC) ficaram 3 ciclos só no documento/fila e nunca chegaram à execução, porque **quem produz/aprova/dispacha é a rotina DIÁRIA** (outra tarefa agendada), não o loop semanal nem o código do repo. Mudança de abordagem neste ciclo: **enforçar no único chokepoint que o loop semanal controla — o `publisher.py`.** Adicionada a flag `STATIC_PAUSED`: o publisher recusa `static` e publica o próximo carrossel/Reel aprovado, independente do que a rotina diária aprove. Horário (cron em `.github/workflows/`) e a publicação da fila estratégica (precisa de render) continuam fora do alcance — esses seguem escalados. Regra nova: **se uma decisão não é aplicável pelo loop semanal via código do repo, escalar explicitamente e não fingir que a reescrita do documento resolve.**

### Sobre a Fila Estratégica (NOVO)
Os derivados de vencedores e o reteste de sono estão como `draft` **sem arquivo renderizado** (`content/` vazio para os `der_*`). A rotina diária não os renderiza/aprova — publica a própria série `vsabia_*` (17 drafts estáticos no backlog). Por isso o experimento de sono (`exp_sono_hook_timing`) **não concluiu**. O loop semanal (texto/análise, sem render) não pode publicá-los. Lever exclusivo da rotina diária.

### Sobre Vencedores/Fracassos
- Novo vencedor: **cãibra muscular (654, saves/reach 0,031)** — mito prático universal; família "erros/mitos práticos".
- Reconfirmados: carga de carbo (950, saves/reach 0,039) e cafeína (979).
- "Fracassos" ferro (156) e keto (194) saíram às 11h UTC → **confundidos pelo horário**, não condenados por tópico. Retestar em 15h. (Honestidade analítica: não declarar tópico morto a partir de post em janela ruim.)

### Sobre Horário/Dia (base ampliada, n=69 carrossel)
15h UTC 828 (n=17) ≫ 11h 269 (n=13); piores 16h (158)/17h (212). Pior dia: sexta 236 (n=32, maior volume — e é onde mais se publica carrossel). Melhores: segunda 668, terça 630.

## Mudanças Estratégicas (continuação)
| Data | O que mudou | Por quê | Evidência |
|------|-------------|---------|-----------|
| 2026-10-04 | **EXECUTADO: `publisher.py STATIC_PAUSED`** — publisher recusa formato estático | Enforce em código da pausa decidida há 4 semanas e nunca aplicada pela rotina diária | estático 199 vs carrossel 241 na mesma janela; 10 estáticos em 14d no fundo |
| 2026-10-04 | +1 vencedor (cãibra 654) e +2 fracassos (ferro 156, keto 194, confundidos por horário) | Winner/failure system | posts_db 04/10 |
| 2026-10-04 | Escalado: rotina diária deve dispachar 15h UTC e consumir a fila estratégica (render+approve) | 4ª semana; horário e fila fora do alcance do loop semanal | carrossel 15h 828 vs 11h 269; der_* sem render |
| 2026-10-06 | **Novo formato diário `prov_*` (carrossel provocativo com imagens, ~17h BRT)** no lugar do estático "você sabia" | Pedido do Victor; o post "carbo fosse carro" teve shares/reach 4,5% (34 shares) vs mediana 0,8% dos `draft_*` | 1 post — hipótese, medir em 10 `prov_*` |
| 2026-10-06 | **Carrossel técnico ganha foto** (capa + 2–3 slides) e hook mais afiado; passa a sair ~12h BRT (tag `time:12brt`) | Pedido do Victor; todo carrossel da fase agente era só texto | ver `strategy/playbook_visual.md` |
| 2026-10-06 | **Rotina diária passa a consumir a fila `der_*`** antes de criar tema novo | Resolve a pendência crítica de 4 semanas (derivados nunca renderizados) | fila 06/10: 9 `der_*` em `draft` |
| 2026-10-06 | Quality gate ganhou travas: Z2 só em `comparativo`, licença/crédito de foto, `fact` obrigatório no provocativo | Publicação sem revisão humana precisa de trava em código, não em prompt | `scripts/quality_gate.py` |

### CORREÇÃO 2026-10-06 — a regra "15h UTC rende 3x" está confundida por lote
Conferido em `posts_db.json`: dos 17 carrosséis de 15h UTC, **8 saíram no mesmo dia (03/07)** e 6 em 07/08; as faixas "piores" de 16h (n=6) e 17h (n=7) são quase inteiras o lote de **07/08** (17 posts num dia só, todos baixos). O único dado limpo é 11h UTC (n=13 em 13 dias distintos, mediana 269) — e ele coincide com a fase de carrossel só-texto. **Não dá para afirmar efeito de horário com essa base.** Meio-dia BRT segue como teste razoável; comparar só após ≥10 posts `time:12brt`, sabendo que foto e hook mudaram junto. Mesma cautela para "pior dia = sexta" (n=32 concentra lotes): reconferir por dias distintos antes de tratar como regra.

### 2026-10-07 — 1ª execução do técnico com foto: funcionou, com um deslize
`der_carga_carbo_passo` saiu às 11:48 BRT no Instagram e no Ghost, com capa-foto, kicker e 2 faixas de foto, consumindo a fila `der_*` (pendência de 4 semanas resolvida na 1ª tentativa). Deslize: o slide 5 usou uma foto de largada com corredores de frente, apesar da regra "sem rosto identificável" no prompt. Mesma lição de 04/10 — **regra que importa vai para o código**: criado `scripts/face_check.py` (YuNet); a busca marca, o render registra, o gate reprova.

### 2026-10-07 — Piloto provocativo no ar e direção fechada
`prov_001` ("Se suplemento fosse carro") publicado às 15:21 BRT (post_id 17924119977425747) com OK do Victor. Diretriz dele: **manter o conceito do post dos carros e criar ideias novas dentro dele** — todo `prov_*` é "Se X fosse Y"; as outras mecânicas saíram do playbook. Banco de 11 ideias com âncoras conferidas no PubMed em `strategy/playbook_visual.md`. Medir por `idea:` e `universe:`.
Publicação falhou na 1ª tentativa com "Media ID is not available" (2ª ocorrência em 3 dias, mesma de draft_022): o `publisher.py` agora repete o `media_publish` com o mesmo `creation_id` até 4 vezes.

### 2026-10-09 — "Se X fosse Y" encerrado; 17h vira marca x marca
O Victor achou as analogias exageradas depois de 3 posts (`prov_001`–`prov_003`). Novo formato do slot das 17h: **dois produtos reais lado a lado, só com dados do rótulo oficial, sem julgamento de valor** (`template: versus`). Gate reprova palavras de julgamento e produto sem fonte de rótulo datada. Piloto `vs_001` (Maurten Gel 100 x GU Energy Gel) aguardando OK.

