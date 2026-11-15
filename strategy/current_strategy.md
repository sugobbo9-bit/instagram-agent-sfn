# Estratégia Atual — @sofatosnutricao

> **Decisão do Victor (31/10/2026) — claim check semanal.** 1x/semana o slot técnico das 12h BRT vira `claim_NNN` (`series:claim-check`, playbook seção 6): uma promessa de marketing de um gel real confrontada com a evidência, rodízio fixo **Maurten → Dobro BT Nitrato → Xtratus H2Gel**. Veredito só com estudo citado, evidência mista declarada como mista, sem insulto, **Z2 nunca aparece**, preço em R$/g de carbo com fonte+data. Cadência é diretriz do dono: a revisão mede e ajusta hook/ângulo, **não suspende**. _Status 15/11: **ainda 0 claim_* publicados** — 2 semanas após a diretriz, a rotina diária nunca renderizou o 1º (claim_001, Maurten). Reescalado._

> **Decisão do Victor (27/10/2026) — card informativo como 3º post diário.** Série `card_NNN` (`series:card-informativo`, estático, ~19h30–22h BRT; playbook seção 5). A revisão mede separado e **não re-pausa automaticamente** — só reporta e deixa a decisão com o Victor após ≥4 semanas (janela fecha ~24/11). _Status 15/11: n=9, mediana **98** (fundo do feed) — tendência fortemente negativa, mas **dentro da janela de observação do dono**: reportado, não re-pausado._

_Atualizado: 2026-11-15, revisão estratégica semanal_
_Base: **8.850 seguidores** (−236 na semana; 2ª queda seguida) | 219 publicações com métricas reais (Graph API, bootstrap 15/11)_

## O quadro da semana: a publicação voltou, mas o alcance está em queda livre

**Boa notícia: o blackout acabou.** A publicação está contínua desde 10/11 (2–3 posts/dia). Os únicos buracos recentes foram **10–25/out (14 dias, o grande)** e **07–09/nov (3 dias)**. A consistência — prioridade nº 1 dos últimos ciclos — está, por ora, restabelecida.

**Má notícia: seguidores continuam caindo e o alcance do carrossel despencou.** Trajetória: +137 / +152 / +111 / −13 / −430 / **−236**. E a mediana de alcance do carrossel está em queda acelerada:

| janela | mediana carrossel |
|---|---|
| baseline all-time (n=109) | 301 |
| últimos 14 dias (n=19) | **173** |
| últimos 7 dias (n=8) | **118,5** |

Com a publicação restaurada, o furo deixou de ser **consistência** e passou a ser **curadoria**: o feed está ~65% preenchido por dois formatos que a estratégia já condenou e que não entregam alcance nem seguidores.

## O diagnóstico central: o feed está diluído por lixo diário

### Performance por fluxo de conteúdo (últimos 30d, por prefixo de `local_id`)
| fluxo | n | mediana alcance | shares totais | posts com 0 share |
|---|---|---|---|---|
| **`der_` técnico (derivado de vencedor)** | 9 | **406** | 72 | 1 |
| `draft_` técnico | 4 | 261 | 16 | 0 |
| **`vs_` versus de commodity de nicho** | 16 | **138** | 15 | **11** |
| **`card_` estático** | 9 | **98** | 5 | 4 |
| `claim_` claim-check | 0 | — | — | — |

**Leitura dura:** de cada ~29 slots recentes de carrossel+estático, **25 são `vs_` de nicho (16) + `card_` (9)** — conteúdo que a plataforma lê como "volume fraco". Só **13 técnicos** (`der_`+`draft_`) seguram o alcance. O motor (técnico, mediana 406) está sendo afogado pelo lastro (versus 138 + card 98). É a mesma mecânica que derrubou a série estática em set/out — agora com os `vs_*`.

### Horário — carrossel por DIAS DISTINTOS (últimos 45d)
| janela | dias distintos | mediana | leitura |
|---|---|---|---|
| **15h UTC** | 5 | **546** | slot técnico — o motor |
| 14h UTC | 11 | 300 | slot técnico (mais limpo) |
| 11h UTC | 5 | 264 | fraca |
| **19h UTC** | 8 | **157** | **morto** (onde saem os `vs_*`) |
| **20h UTC** | 12 | **166** | **morto** (onde saem os `vs_*`) |

Reconfirmado: o único motor é **14–15h UTC**. Os `vs_*` saem em **19–20h** (os piores horários) — dobro de penalidade: formato errado no horário errado.

### Hook (tag `hook:`)
**Contrarian segue vencendo:** contrarian (n=20) mediana **374**, myth (n=16) **312**. Hook contrarian+numérico é o padrão de produção. Reconfirmado pelos campeões.

## Vencedor do ciclo
- **`der_carga_carbo_curta` = 717** (15:55 UTC, 25 shares, 13 saves, shares/reach 0,035). **Família carga de carboidrato reconfirmada pela 4ª vez** (passo 1.840/1.661, carga 918). Hook contrarian que vira a própria família do avesso ("quando carregar carbo é DESPERDÍCIO"). **6x o alcance do feed recente.** É a receita padrão: família campeã + hook contrarian + slot 15h + foto.

## Fracassos do ciclo (diagnóstico)
- **`vs_*` versus de commodity de nicho (ENFORCE EM CÓDIGO):** padrão reincidente e agravado, n=16, mediana 138, 11/16 com 0 share, todos no fundo (vs_018 creatina Max Titanium×Dux=46, o pior do mês). Decisão de 01/11 (aposentar) nunca aplicada pela rotina diária. **Ação deste ciclo: trava `VERSUS_COMMODITY_BLOCKED` no `quality_gate.py`** — o gate reprova versus sem marca mainstream (allowlist) e sem `distinct_formulas:true`. Testado nos arquivos reais (vs_019/018/016 reprovados; vs_009 Gatorade×Powerade aprovado).
- **Série `card_*` (estático, mediana 98):** mesmo padrão do antigo estático. **Sob observação por diretriz do Victor** — não re-pausar antes de ~24/11; reportado.

## Decisões para o próximo ciclo
1. **Curadoria > volume (a alavanca nº 1 agora).** Com a publicação restaurada, o que trava a conta é o feed diluído. A trava de versus-commodity (em código) remove ~metade do lastro sem tocar no motor técnico nem arriscar blackout (só afeta o template `versus`).
2. **Alimentar o motor técnico.** `der_*` (carga de carbo, lactato, cafeína, cãibra) no slot **14–15h UTC**, com foto e hook contrarian+numérico. É o único fluxo que entrega alcance e shares.
3. **Horário:** conteúdo relevante só em 14–15h. Parar de jogar qualquer coisa em 19–20h (mortos).
4. **Claim-check:** 2 semanas sem o 1º post. **Reescalado ao Victor** — depende da rotina diária renderizar `claim_001` (Maurten). O gate `claim_check` já está pronto.
5. **Card informativo:** respeitar a janela de observação do dono (≥4 semanas, fecha ~24/11); no próximo ciclo a decisão de manter/pausar terá base completa (hoje mediana 98, tendência clara).
6. **Meta do ciclo:** estancar a queda de seguidores via curadoria; recuperar a mediana de carrossel de 118 → 250+ cortando o lastro de versus/card e concentrando em técnico 14–15h.

## Pendências de dados / execução
- **Rotina diária publica o que a estratégia aposentou.** O loop semanal só controla o repo (publisher/gate). A trava de versus foi o passo possível; **horário dos dispatches e a série card seguem fora do alcance do loop** — dependem da rotina diária. Reescalado.
- **Claim-check nunca renderizado** (diretriz de 31/10). Lever exclusivo da rotina diária.
- **Token do Mac expirado (26/08):** `INSTAGRAM_ACCESS_TOKEN` no `.env` expirado — bloqueia demografia + texto de comentários para análise local. 8ª rodada bloqueada. Desbloqueio: regerar token longo (`instagram_manage_insights` + `instagram_manage_comments`) OU passo no Actions que commite `data/audience_demographics.json` + `data/comments_recent.json`.
- **follows/reach por post:** segue cego na Graph API.

## Regras imutáveis
Integridade científica, sem engajamento falso, sem gasto sem aprovação, sem alterar credenciais, rastreabilidade completa: ideia → pesquisa → criativo → publicação → métricas → aprendizado.
