# Estratégia Atual — @sofatosnutricao
_Atualizado: 2026-10-04, revisão estratégica semanal_
_Base: 9.529 seguidores (+111 na semana) | 168 publicações com métricas reais (Graph API, coletadas 04/10)_

## O que os dados dizem agora

### Medianas por formato (amostra completa, normalizado)
| formato | n | alcance mediano | p90 | p75 | p25 | shares/reach | saves/reach |
|---|---|---|---|---|---|---|---|
| **carrossel** | 69 | **418** | 1.218 | 828 | 196 | — | — |
| reel | 77 | 256 | 515 | 381 | 168 | ~0 | baixo |
| estático | 22 | 209 | 356 | 272 | 168 | baixo | baixo |

### Janela recente (o que saiu de fato)
- **Últimos 7 dias:** 4 carrosséis (mediana **204**) + 5 estáticos (mediana 221) + 0 Reels.
- **Últimos 14 dias:** 8 carrosséis (mediana **241**) + 10 estáticos (mediana 199) + 0 Reels.
- O alcance recente do carrossel está **muito abaixo do baseline** (241 vs 418) e o baseline all-time caiu (474→418). Causa dominante: quase todo carrossel recente saiu **às 11h UTC** (janela fraca) e os estáticos diários seguem no fundo.

## Conclusões

### 1 — Crescimento desacelerou, mas segue positivo.
+111 na semana (9.418 → 9.529), abaixo do pico anterior (+152) mas ainda saudável, apesar do alcance recente fraco. A conta converte bem por alcance (puxada pelos poucos carrosséis de alto salvamento). follows/reach por post segue cego na Graph API — otimização de conversão não é possível no nível do post. **Não sacrificar qualidade por alcance bruto.**

### 2 — A causa do alcance fraco é execução, não estratégia (4ª semana).
Quase todo carrossel recente saiu **às 11h UTC** (mediana histórica 269) em vez de **15h UTC** (mediana 828) — a diferença é de ~3x. E a **série estática diária** continua saindo, toda no fundo. As duas maiores alavancas identificadas há 4 semanas seguiram desligadas. **A estratégia e a fila estão certas; o que falha é a aplicação na rotina diária.**

### 3 — Ação executada neste ciclo: pausa do estático agora é código.
Em vez de só reescrever o documento (4ª vez), a pausa do estático foi **enforçada no `publisher.py`** (`STATIC_PAUSED`): o publisher recusa qualquer item `static` e publica o próximo carrossel/Reel aprovado. É o único ponto por onde toda publicação passa, então vale **independentemente** do que a rotina diária aprove. Reversível. A série "você sabia" (backlog de 17 drafts `vsabia_*`) deixa de poluir o feed.

### 4 — O horário (15h UTC) ainda depende do Victor / rotina diária.
O `publisher.py` ignora `scheduled_for` e publica o próximo `approved` por prioridade quando é dispachado. **Quem define o horário é (a) o cron do `publish.yml` (`0 12` UTC) e (b) os `workflow_dispatch` da rotina diária (~11h).** O cron está em `.github/workflows/` — fora do alcance do token atual (fine-grained, sem permissão de Workflows); a tentativa de mover `0 12`→`0 15` está registrada no log semanal. Os dispatches diários vêm da rotina diária (outra tarefa agendada), que este loop não controla.

### 5 — A fila estratégica não está sendo publicada.
Os derivados de vencedores (gel vs bebida, carga de carbo passo a passo/erros, lactato prático, ice slurry, mouth rinse) e o **reteste de sono** seguem como `draft` **sem arquivo renderizado** em `content/`. A rotina diária não os promoveu a `approved` nem os renderizou — publicou a própria série estática. Resultado: o experimento de sono não concluiu e os vencedores não geraram derivados no ar. **Lever: a rotina diária precisa consumir a fila estratégica.**

### 6 — Vencedores reconfirmados (famílias para explorar).
- **Carga de carboidrato/depleção (950, saves/reach 0,039)** — maior valor de salvamento; protocolo prático + myth-busting.
- **Cafeína (979)** — família recorrente; funciona mesmo em horário ruim.
- **Cãibra muscular (654, saves/reach 0,031)** — NOVO; corrige mito prático universal (cãibra ≠ só sal/água). Família "erros/mitos práticos de treino".
- Padrão vencedor estável: **derrubar uma crença + entregar protocolo acionável**. Comparação de produto segue como motor de compartilhamento (gel 0,045).

### 7 — "Fracassos" recentes são confundidos pelo horário — não condenar tópicos.
Ferro (156) e keto/low-carb (194) saíram **às 11h UTC**. Ferro teve shares/reach 0,038 (bom sinal). Não são testes limpos: o alcance baixo é dominado pela janela ruim. **Retestar em 15h UTC antes de desistir** — ferro com hook de sintoma; low-carb com ângulo de periodização (train-low), não mito keto.

### 8 — Horário e dia (reconfirmado).
Melhor: **15h UTC (12h BRT) mediana 828** (n=17); depois 18h (762), 20h (754), 14h (627). Piores: **11h (269)**, 16h (158), 17h (212). Pior dia: **sexta (236, n=32)**; melhores segunda (668) e terça (630).

## Decisões para o próximo ciclo

1. **Carrossel = formato padrão** (mantido). Reel só como experimento de conteúdo intrinsecamente visual.
2. **Estático PAUSADO — agora em código** (`publisher.py STATIC_PAUSED`). Só volta como dado/gráfico único excepcional, e apenas desligando a flag.
3. **Publicar às 15h UTC (12h BRT).** *Depende do Victor (cron) e da rotina diária (dispatch) — ver Pendências.* Nunca 11h/16h/17h; nunca carrossel na sexta.
4. **Rotina diária deve consumir a fila estratégica:** renderizar e aprovar os derivados de vencedores e o reteste de sono, em vez de gerar série estática. *Escalado.*
5. **Explorar famílias vencedoras:** carga de carbo (passo a passo; erros), cafeína (dose/timing), cãibra/erros práticos, comparação de produto.
6. **Retestar ferro e low-carb em 15h UTC** com os ângulos acima antes de arquivá-los.
7. **Meta do ciclo:** recuperar o alcance mediano do carrossel para 500+ ligando a janela de 15h UTC e consumindo a fila; concluir o experimento de sono.

## Pendências de dados / execução
- **CRÍTICO (4ª semana): a rotina DIÁRIA precisa (a) dispachar carrosséis às 15h UTC (não 11h) e (b) renderizar/aprovar a fila estratégica** em vez de produzir estáticos. O estático já está barrado no publisher, mas o horário e a publicação dos vencedores dependem da rotina diária, fora do alcance deste loop.
- **CRÍTICO: dar permissão de Workflows ao token** (ou o Victor mudar o cron à mão). O token atual (fine-grained) não edita `.github/workflows/`; mover o cron `0 12`→`0 15` UTC precisa disso. Ver resultado da tentativa no log semanal.
- follows/reach e visitas ao perfil ainda não vêm no import da Graph API — conversão em seguidor segue cega no nível do post.
- Demografia/`online_followers` e **texto** dos comentários: o token da Página tem escopos suficientes (`instagram_manage_insights`, `instagram_manage_comments`), mas vive só como Secret do Actions; falta **instrumentar um passo no workflow** que commite `data/audience_demographics.json` e `data/comments_recent.json`. Enquanto isso, o banco de perguntas da audiência não começa.

## Regras imutáveis
Integridade científica, sem engajamento falso, sem gasto sem aprovação, rastreabilidade completa: ideia → pesquisa → criativo → publicação → métricas → aprendizado.
