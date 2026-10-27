# Estratégia Atual — @sofatosnutricao

> **Decisão do Victor (27/10/2026) — card informativo volta como 3º post diário.** A série antiga "você sabia" (`vsabia_*`) segue encerrada; a nova série `card_NNN` (`series:card-informativo`: ativos, técnicas, biohacks e notícias da alta performance; playbook seção 5) sai 1x/dia à noite (~19h30). `STATIC_PAUSED` foi desligada no `publisher.py`. A revisão semanal mede a série nova separadamente e **não a re-pausa automaticamente** — só reporta e deixa a decisão com o Victor após ≥ 4 semanas.

_Atualizado: 2026-10-11, revisão estratégica semanal_
_Base: 9.516 seguidores (−13 na semana — 1ª semana não-positiva) | 178 publicações com métricas reais (Graph API, coletadas 11/10)_

## O que mudou nesta semana (a virada de processo)

Depois de **4 semanas** em que as duas decisões centrais (pausar estático; publicar a fila estratégica) ficavam só no documento, elas **chegaram à produção**:

1. **Estático pausado DE VERDADE.** 10 carrosséis e **0 estáticos** nos últimos 7 dias. A flag `STATIC_PAUSED` no `publisher.py` está segurando — a série "você sabia" sumiu do feed.
2. **Fila `der_*` sendo consumida.** 3 derivados publicados na semana (`der_carga_carbo_passo`, `der_sono_retest`, `der_ice_slurry`). Restam 5 em `draft` (ritmo ~3/semana).
3. **O formato técnico-com-foto funcionou — forte.** `der_carga_carbo_passo` fez **1.661 de alcance** (maior do era-agente, perto do p90 all-time), **saves/reach 0,049** (maior recente) e 43 shares. A direção de foto do Victor está validada.

## A receita vencedora desta semana (repetir)

O breakout não foi sorte: foi **convergência de todas as alavancas**.
**família vencedora + formato técnico COM FOTO + hook numérico contraintuitivo + janela 14–15h UTC.**
Hook do post: _"Carga de carbo não é jantar macarrão na véspera. É 10 g/kg por 2 dias."_ (derruba crença + número + protocolo).
Essa é a fórmula padrão do slot técnico daqui pra frente.

## O que os dados dizem agora

### Medianas por formato (amostra completa, normalizado)
| formato | n | alcance mediano | p90 | p75 | p25 |
|---|---|---|---|---|---|
| **carrossel** | 79 | **366** | 1.219 | 764 | 197 |
| reel | 77 | 256 | 515 | 381 | 168 |
| estático | 22 | 226 | 356 | 318 | 176 |

Baseline do carrossel caiu 418→366: os 10 posts novos incluem janelas fracas (11h) e os formatos de teste que fraquejaram (analogia `prov_*`, `vs_002`), que puxam a mediana para baixo apesar do breakout de 1.661.

### Janela recente
- **7 dias:** 10 carrosséis (mediana **262**), 0 estáticos, 0 Reels.
- **14 dias:** 14 carrosséis (mediana 257) + 5 estáticos (cauda da série já encerrada).
O alcance mediano segue abaixo do baseline, mas a **distribuição melhorou**: o topo subiu (1.661) e o lixo estático saiu.

### Horário — análise por DIAS DISTINTOS (corrige o confundimento de lote)
A regra antiga "15h UTC rende 3x" estava inflada por lotes (os 17 posts de 15h vêm de só 5 dias). Contando **dias distintos**:

| janela | dias distintos | alcance mediano | leitura |
|---|---|---|---|
| **18h UTC** | 7 | **696** | melhor janela limpa |
| 19h UTC | 6 | 504 | boa |
| **14h UTC** | 6 | **449** | boa (e o breakout saiu aqui) |
| 11h UTC | 15 | 300 | fraca (amostra limpa e grande) |
| 20h UTC | 4 | 454 | ok no geral, mas **fraca no era-agente** (109, 253) |
| 15h UTC | 5 | 828 | **ainda confundida por lote — não usar como âncora** |

No **era-agente** (últimos 30d, mais limpo): **14h e 18h UTC são as melhores**; 11h só salva quando o tópico é muito forte (cafeína/carga fizeram 951/979 às 11h).

### Dia da semana (dias distintos)
Sexta é o **pior dia, agora com 9 dias distintos** (mediana 259) — deixou de ser artefato de lote. Melhores: **segunda (654), terça (552)**. Quarta/quinta ~424.

## Formatos em teste

- **Técnico com foto (slot ~14h):** VALIDADO (breakout 1.661). Receita acima. Consome a fila `der_*` primeiro.
- **Provocativo "Se X fosse Y" (`prov_*`): ENCERRADO.** Dados confirmam a decisão do Victor (09/10): 484 → 164 → 253, shares baixíssimos. A analogia não sustenta curiosidade após o 1º post.
- **Versus "marca vs marca, só o rótulo" (`vs_*`):** cedo demais (n=2, misto). **gel diferenciado (Maurten hidrogel × GU) = 436; creatina commodity = 109, 0 shares.** Hipótese: versus só funciona quando os produtos **diferem de fato** — não comparar duas monohidratadas iguais. Manter o teste só com produtos realmente distintos.

## Vencedores reconfirmados (famílias para explorar)
- **Carga de carboidrato (breakout 1.661, saves/reach 0,049)** — família campeã; protocolo + myth-busting + foto. Derivados: `der_carga_carbo_erros` (na fila), `der_carga_carbo_curta` (novo — "quando NÃO fazer").
- **Cafeína** — vencedora recorrente (fez 979 até em janela ruim). Reframe com hook numérico mais afiado no slot 14h.
- **Cãibra (654, saves/reach 0,031)** — mito prático universal; 1º derivado agora na fila (`der_caibra_mitos`).
- Padrão estável: **derrubar uma crença + número + protocolo acionável.**

## Experimento concluído
**Sono (hook + timing):** variante venceu **+53% (272 vs 178)** — hook numérico e janela melhor recuperam parte do alcance (confirmado). **Mas** 272 ficou muito abaixo do teto do tópico sono (1.164): o ângulo "extensão de sono" é fraco. Priorizar o ângulo campeão (**privação de sono → composição corporal**, que fez 2.437).

## Decisões para o próximo ciclo
1. **Carrossel técnico com foto = formato padrão**, com a receita do breakout (família vencedora + hook numérico + foto).
2. **Slots:** técnico ~**14h UTC**; 2º post do dia ~**18–19h UTC** (janelas limpas mais fortes). **Abandonar a âncora "15h"** (confundida) e **evitar 11h e 20h**. **Nunca carrossel na sexta.**
3. **Consumir a fila `der_*`** antes de criar tema novo (restam 5). Aplicar a receita de foto+número aos novos derivados (`der_caibra_mitos`, `der_carga_carbo_curta`).
4. **Versus:** só com produtos que diferem de verdade (géis, bebidas com fórmulas distintas) — não commodities.
5. **Sono:** se voltar ao tópico, usar o ângulo de privação/composição, não extensão.
6. **Meta do ciclo:** recuperar a mediana de carrossel para 400+ concentrando a publicação em 14h/18h e mantendo a receita do breakout; voltar o crescimento de seguidores ao positivo.

## Pendências de dados / execução
- **Seguidores estagnaram (−13).** Provável platô/ruído, mas vigiar na próxima coleta. follows/reach por post segue cego na Graph API — conversão não otimizável no nível do post.
- **Horário ainda depende da rotina DIÁRIA + cron.** O breakout saiu às 14h48 (perto da janela boa) — bom sinal de que a rotina diária está dispachando melhor. Confirmar se é consistente. O cron do `publish.yml` continua fora do alcance do token (sem escopo `workflow`); o Victor move à mão se quiser cron fixo em 14h/18h.
- **Demografia/comentários:** o token da Página tem escopo (`instagram_manage_insights`, `instagram_manage_comments`) mas vive só como Secret do Actions. Falta **instrumentar um passo no workflow** que commite `data/audience_demographics.json` e `data/comments_recent.json`. Até lá, o banco de perguntas da audiência não começa.

## Regras imutáveis
Integridade científica, sem engajamento falso, sem gasto sem aprovação, rastreabilidade completa: ideia → pesquisa → criativo → publicação → métricas → aprendizado.
