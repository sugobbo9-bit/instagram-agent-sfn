# Estratégia Atual — @sofatosnutricao

> **Decisão do Victor (31/10/2026) — claim check semanal.** 1x/semana o slot técnico das 12h BRT vira `claim_NNN` (`series:claim-check`, playbook seção 6): uma promessa de marketing de um gel real confrontada com a evidência, rodízio fixo **Maurten → Dobro BT Nitrato → Xtratus H2Gel**. Veredito só com estudo citado, evidência mista declarada como mista, sem insulto, **Z2 nunca aparece**, preço em R$/g de carbo com fonte+data. Cadência é diretriz do dono: a revisão mede e ajusta hook/ângulo, **não suspende**. _Status 22/11: **ainda 0 claim_* publicados** — 3+ semanas após a diretriz; o gate `claim_check` está pronto, mas a rotina diária nunca renderizou o 1º (claim_001, Maurten). Reescalado (o loop semanal não renderiza imagem)._

> **Decisão do Victor (27/10/2026) — card informativo como 3º post diário.** Série `card_NNN` (`series:card-informativo`, estático, ~19h30–22h BRT; playbook seção 5). A revisão mede separado e **não re-pausa automaticamente** — só reporta e deixa a decisão com o Victor após ≥4 semanas (**janela fecha ~24/11, ou seja, agora**). _Status 22/11: n=11, mediana **118** (fundo do feed, vs técnico 290–406) — tendência negativa clara e estável. A janela de observação do dono está fechando; a recomendação baseada em dados é **pausar/retrabalhar**, mas a decisão é do Victor. Reportado, não re-pausado._

_Atualizado: 2026-11-22, revisão estratégica semanal_
_Base: **8.845 seguidores** (−5 na semana — a sangria praticamente parou) | 232 publicações com métricas reais (Graph API, bootstrap 22/11)_

## O quadro da semana: a sangria de seguidores PAROU; o alcance ainda é refém da curadoria

**Melhor notícia em 6 semanas: os seguidores estabilizaram.** Trajetória: +137 / +152 / +111 / −13 / −430 / −236 / **−5**. Depois de duas quedas grandes, a conta está essencialmente plana. A publicação segue contínua (2–3 posts/dia) e os motores de conteúdo (técnico contrarian no slot 14–15h) estão entregando. A desaceleração −430 → −236 → −5 é consistente com o diagnóstico dos últimos ciclos: **o problema nunca foi o conteúdo forte — era o lastro diluindo o feed.**

**O que ainda não virou: o alcance do carrossel.** Mediana por janela de recência:

| janela | mediana carrossel | n |
|---|---|---|
| baseline all-time | 292 | 120 |
| últimos 30 dias | 178,5 | 40 |
| últimos 14 dias | **144** | 19 |
| últimos 7 dias | **163** | 11 |

O 7d (163) parou de cair e subiu um pouco vs o 118 do ciclo passado — porque os `draft_*` técnicos (contrarian, 14–15h) estão puxando (draft_029=779, der_carga_carbo_curta=764, draft_031=368). Mas a mediana segue afogada pelo lastro diário.

## O diagnóstico central (reconfirmado com dado fresco): o motor funciona, o lastro afoga

### Performance por fluxo de conteúdo (últimos 30d, por prefixo de `local_id`)
| fluxo | n | mediana alcance | shares totais | posts com 0 share |
|---|---|---|---|---|
| **`der_` técnico (derivado de vencedor)** | 9 | **406** | 72 | 1/9 |
| `draft_` técnico | 9 | **290** | 50 | 0/9 |
| **`vs_` versus (nicho)** | 22 | **123,5** | 16 | **16/22** |
| **`card_` estático** | 11 | **118** | 6 | 5/11 |

**Leitura dura (mesma de 2 ciclos, agora com causa-raiz):** de cada ~42 slots recentes de carrossel+estático, **33 são `vs_` (22) + `card_` (11)** — lastro que a plataforma lê como volume fraco. Só **18 técnicos** (`der_`+`draft_`) seguram o alcance. O motor (técnico 290–406, quase sem zero-share) está sendo afogado pelo lastro (versus 123 com 16/22 zero-share + card 118).

### A causa-raiz do lastro de versus: a trava de 11/15 estava VAZANDO
A trava `VERSUS_COMMODITY_BLOCKED` foi adicionada em 15/11, mas vs_020..vs_025 continuaram saindo **diários após a trava** (reach 48–163, maioria 0 share). Investigação deste ciclo: a allowlist `MAINSTREAM_BRANDS` incluía **as próprias marcas de nicho de endurance** (maurten, gu, sis, clif, honey stinger) — então todo versus de gel/goma/bebida de nicho passava como "mainstream" e escapava da trava. **A trava existia mas não travava nada.**

**Ação deste ciclo (enforce em código, testado):** allowlist reduzida a marcas **de massa** (Gatorade, Powerade, Coca-Cola, Red Bull, Monster, Nestlé). Marca de endurance só entra via `distinct_formulas:true` (gap real de fórmula, ex. hidrogel × gel comum). Testado nos **25 arquivos vs_ reais**: 21 reprovam; só mainstream (vs_009/025 Gatorade×Powerade) e distinct (vs_021 SiS×Maurten, flag marcada) passam. Isolado ao template `versus` — **sem risco de blackout** (não toca técnico/card/claim).

### Horário — carrossel por DIAS DISTINTOS (últimos 60d)
| janela | dias distintos | mediana | leitura |
|---|---|---|---|
| **15h UTC** | 5 | **546** | slot técnico — o motor |
| **14h UTC** | 16 | **307** | slot técnico (o mais usado, limpo) |
| 11h UTC | 8 | 282,5 | fraca |
| **19h UTC** | 8 | **158** | **morto** (saída dos `vs_`) |
| **20h UTC** | 18 | **147,5** | **morto** (saída dos `vs_` e cards) |

Reconfirmado pela enésima vez: o único motor é **14–15h UTC**. Todo `vs_` sai em **19–20h** (os piores horários) — dupla penalidade: formato fraco no horário morto. Mesmo o único versus mainstream recente (vs_025 Gatorade×Powerade) fez só 88 nesse slot. O horário dos dispatches segue fora do alcance do loop (rotina diária).

### Hook (tag `hook:`, carrossel)
**Contrarian segue à frente:** contrarian (n=25) mediana **343** > myth (n=16) **312**. Hook contrarian+numérico/contraintuitivo é o padrão de produção — reconfirmado pelos 3 campeões do ciclo (beterraba, carga-carbo-curta, lactato all-time).

## Vencedor do ciclo
- **`draft_029` beterraba/nitrato = 779** (14:50 UTC, 21 shares, shares/reach 0,027, 10 saves). **NOVA família de conteúdo (nitrato/beterraba)** estreia como vencedora. Hook contrarian que vira a expectativa: *"o suco de beterraba funciona — só que cada vez menos quanto mais você treina"*. 6x o feed recente. Receita padrão confirmada: hook contrarian + slot 14–15h + foto. **Família nova para explorar** (2 derivados na fila: dose eficaz; quem responde / efeito do enxaguante bucal).
- Reconfirmado: **`der_carga_carbo_curta` = 764** (era 717; família carga de carbo pela 4ª vez, 25 shares, shares/reach 0,033).

## Fracassos do ciclo (diagnóstico)
- **`vs_*` nicho (ROOT CAUSE em código):** vs_020..024 vazaram a trava por 1 semana por causa da allowlist mal calibrada (ver acima). **Corrigido e testado.** Lição (4ª repetição): regra de curadoria que importa tem de ser enforçada em código **e testada contra os arquivos reais** — allowlist errada é pior que trava nenhuma (dá falsa sensação de controle).
- **Série `card_*` (estático, mediana 118, n=11):** mesmo teto do antigo estático. **Janela de observação do dono fecha ~24/11** — recomendação por dados é pausar/retrabalhar, mas a decisão é do Victor. Reportado, não re-pausado.

## Decisões para o próximo ciclo
1. **Curadoria em código > volume (alavanca nº 1, agora de fato aplicada).** A correção da allowlist remove o lastro de versus de nicho no único chokepoint que o loop controla (o gate), sem tocar no motor nem arriscar blackout. **Métrica de sucesso para a semana que vem:** nº de `vs_` de nicho publicados deve cair para ~0; a mediana de carrossel recente deve subir de 144–163 em direção a 250+.
2. **Alimentar o motor técnico.** `der_*`/`draft_*` (carga de carbo, lactato, cafeína, cãibra, **nitrato/beterraba — novo**) no slot **14–15h UTC**, com foto e hook contrarian+numérico. É o único fluxo que entrega alcance e shares.
3. **Horário:** conteúdo relevante só em 14–15h. Parar de jogar qualquer coisa em 19–20h (mortos). Fora do alcance do loop — depende da rotina diária. Reescalado.
4. **Claim-check:** 3+ semanas sem o 1º post. Gate pronto; depende da rotina diária renderizar `claim_001` (Maurten). Reescalado (o loop semanal não renderiza imagem).
5. **Card informativo:** a janela do dono (≥4 semanas) fecha ~24/11. A base de dados está completa (mediana 118, tendência clara). Decisão de manter/pausar é do Victor; a recomendação por dados é pausar ou retrabalhar formato/slot.
6. **Meta do ciclo:** consolidar a estabilização de seguidores (−5) e recuperar a mediana de carrossel recente (144–163 → 250+) cortando de fato o lastro de versus e concentrando no técnico 14–15h.

## Pendências de dados / execução
- **Rotina diária publica o que a estratégia aposentou** (horário 19–20h, série card, versus de nicho — este último agora barrado no gate). O loop semanal só controla o repo (publisher/gate); horário dos dispatches e a série card seguem fora do alcance. Reescalado.
- **Claim-check nunca renderizado** (diretriz de 31/10). Lever exclusivo da rotina diária.
- **Token do Mac expirado (26/08):** `INSTAGRAM_ACCESS_TOKEN` no `.env` expirado — bloqueia demografia + texto de comentários para análise local. 10ª rodada bloqueada. Desbloqueio: regerar token longo (`instagram_manage_insights` + `instagram_manage_comments`) OU passo no Actions que commite `data/audience_demographics.json` + `data/comments_recent.json`.
- **follows/reach por post:** ausente em 0/232 — com seguidores quase planos, segue impossível atribuir follow a post específico na Graph API.

## Regras imutáveis
Integridade científica, sem engajamento falso, sem gasto sem aprovação, sem alterar credenciais, rastreabilidade completa: ideia → pesquisa → criativo → publicação → métricas → aprendizado.
