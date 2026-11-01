# Estratégia Atual — @sofatosnutricao

> **Decisão do Victor (31/10/2026) — claim check semanal.** 1x/semana o slot técnico das 12h BRT vira `claim_NNN` (`series:claim-check`, playbook seção 6): uma promessa de marketing de um gel real confrontada com a evidência, em rodízio fixo **Maurten → Dobro BT Nitrato → Xtratus H2Gel**. Veredito só com estudo citado, evidência mista declarada como mista, sem insulto, **Z2 nunca aparece**, preço em R$/g de carbo com fonte+data. Cadência é diretriz do dono: a revisão mede (shares/reach, saves/reach, comentários) e ajusta hook/ângulo, **não suspende**. _Status 01/11: 0 claim_* publicados ainda — a rotina diária precisa renderizar o 1º (claim_001, Maurten)._

> **Decisão do Victor (27/10/2026) — card informativo como 3º post diário.** Série `card_NNN` (`series:card-informativo`, estático, ~19h30 BRT; playbook seção 5). A revisão mede separado e **não re-pausa automaticamente** — só reporta e deixa a decisão com o Victor após ≥4 semanas. _Status 01/11: n=4, mediana 110 (fundo) — tendência fraca reportada, dentro da janela de observação._

_Atualizado: 2026-11-01, revisão estratégica semanal_
_Base: **9.086 seguidores** (−430 na semana — 1ª queda grande) | 195 publicações com métricas reais (Graph API, coletadas 01/11)_

## O alerta da semana: seguidores caíram 430

Primeira queda grande da conta (−430: 9.516 → 9.086). Histórico recente: +137 / +152 / +111 / −13 / **−430**. Dois drivers prováveis, ambos de **execução**, não de ciência:

1. **Blackout de 14 dias (11/10 → 26/10).** A conta ficou sem publicar duas semanas. Depois voltou com um **burst de 15 posts em 6 dias** (26–31/10). Sumir e reaparecer em rajada é o padrão clássico que derruba alcance e seguidores. **Escalado ao Victor: descobrir por que a rotina diária parou e blindar contra novos blackouts** — esta é a prioridade nº 1 do ciclo.
2. **Feed recente diluído.** Boa parte do burst foram `vs_*` de commodity e `card_*` estáticos de baixo alcance (ver abaixo), que ensinam o algoritmo que a conta virou volume fraco.

A ciência e os formatos fortes continuam funcionando — o problema é **consistência e curadoria do que entra no feed**.

## O que os dados dizem agora

### Medianas por formato (amostra completa, normalizado)
| formato | n | alcance mediano | p90 | p75 | p25 |
|---|---|---|---|---|---|
| **carrossel** | 91 | **366** | 1.180 | 748 | 195 |
| reel | 77 | 256 | 515 | 381 | 168 |
| estático | 27 | 212 | 342 | 295 | 150 |

Carrossel segue o formato dominante. Reel só como experimento controlado de conteúdo intrinsecamente visual. Estático (inclui a série `card_*` nova) segue no fundo.

### Janela recente (burst 26–31/10)
Carrossel mediana **185** (7d) — muito abaixo do baseline 366. O burst pós-blackout foi fraco na média porque metade foram versus de commodity. Mas o **topo** segue alto quando a receita é respeitada (lactato 947).

### Horário — carrossel por DIAS DISTINTOS (últimos 45d)
| janela | dias distintos | alcance mediano | leitura |
|---|---|---|---|
| **15h UTC** | 3 | **511** | slot técnico forte |
| **14h UTC** | 5 | **436** | slot técnico forte (mais limpo) |
| 18h UTC | 1 | 495 | forte, amostra fina |
| 11h UTC | 12 | 282 | fraca |
| **19h UTC** | 5 | **188** | **morto** (onde saem os vs_*) |
| **20h UTC** | 5 | **185** | **morto** (onde saem os vs_*) |

**Leitura dura:** a rotina diária está jogando o conteúdo que importa (versus, cards) nos **piores horários da conta** (19–20h, 22h). O único motor é o slot técnico **14–15h UTC**.

### Hook (tag `hook:`)
**Contrarian vence myth, reconfirmado e mais forte:** contrarian (n=12) mediana **430**, saves/reach **0,0166**; myth (n=16) mediana 312, saves/reach 0,0113. Enquadrar como "o protocolo que quase todo mundo faz errado + número" rende mais que "esse mito diz X".

## Vencedores do ciclo (famílias para explorar)
- **Lactato (der_lactato_pratico = 947, vencedor do ciclo)** — hook contrarian ("o lactato não te cansa, ele te diz o ritmo") + reframe prático. Família campeã all-time (lactato 2450). Derivado novo na fila: `der_lactato_limiar`.
- **Versus MAINSTREAM (Gatorade×Powerade = 699)** — junto com Maurten×GU (495), o único versus que funciona: marcas que todo mundo conhece / fórmulas de fato distintas.
- **Cafeína (der_cafeina_dose_timing = 511)** — família vencedora recorrente, reconfirmada.
- **Cãibra (der_caibra_mitos = 436, saves/reach 0,025)** — mito prático universal, alto salvamento.
- Padrão estável: **derrubar uma crença (contrarian) + número + protocolo acionável, no slot 14–15h, com foto.**

## Fracassos do ciclo (diagnóstico)
- **Versus de commodity de nicho (ENCERRAR):** 6 no fundo (vs_008 whey=80, vs_005 beta-alanina=124, vs_007 tabs=159, vs_002 creatina=167, vs_004 whey=182, vs_006 cafeína cápsula=185). Falha repetida (n=6), não ruído. Marcas de nicho (Growth/Max Titanium/Probiótica/Atlhetica) não têm reconhecimento nem gap de curiosidade, e saem no slot morto das 20h.
- **der_carga_carbo_erros (122):** família campeã, hook de LISTA fraco. Boa ideia, hook errado → reteste com hook contrarian+numérico (`der_carga_carbo_erros_v2` na fila).
- **Série card_* (estático, med 110):** padrão do antigo estático. **Sob observação por diretriz do Victor** — não re-pausar antes de ≥4 semanas.

## Decisões para o próximo ciclo
1. **Consistência acima de tudo.** Nenhum blackout. Escalado ao Victor: investigar a parada de 14d da rotina diária e garantir publicação diária contínua. Esta é a alavanca nº 1 para reverter a queda de seguidores.
2. **Versus:** aposentar commodity de nicho. Só marcas **mainstream** (Gatorade/Powerade/Red Bull/Coca) ou **fórmulas de fato distintas** (hidrogel × gel comum). E mover para o **slot 14h**, nunca 20h.
3. **Horário:** tudo que importa no slot **14–15h UTC**. Parar de jogar conteúdo relevante em 19–22h (mortos). Nunca carrossel na sexta sem necessidade.
4. **Hook:** contrarian+numérico como padrão de produção.
5. **Fila `der_*`:** consumir antes de criar tema novo (restam `der_mouth_rinse`, `der_carga_carbo_curta` + os 2 novos). Aplicar foto + hook numérico.
6. **Claim-check:** publicar o 1º (`claim_001`, Maurten) no slot técnico — pendência da rotina diária.
7. **Meta do ciclo:** voltar o crescimento de seguidores ao positivo via consistência + curadoria; recuperar a mediana de carrossel para 350+ concentrando a publicação em 14–15h e cortando o lixo de 20h.

## Pendências de dados / execução
- **Blackout de publicação (CRÍTICO):** a rotina diária ficou 14d sem rodar. Causa desconhecida (token do Mac? cron? Actions?). Maior suspeito da queda de seguidores. Escalado.
- **Token do Mac expirado (26/08):** `INSTAGRAM_ACCESS_TOKEN` em `SFN/Instagram Agent/.env` expirado — bloqueia demografia + texto de comentários para análise local. O token de Página vive só como Secret do Actions (bootstrap funciona por lá). Regerar destrava o banco de perguntas da audiência.
- **follows/reach por post:** segue cego na Graph API — conversão não otimizável no nível do post.
- **Demografia/comentários:** falta instrumentar passo no Actions que commite `data/audience_demographics.json` e `data/comments_recent.json`.

## Regras imutáveis
Integridade científica, sem engajamento falso, sem gasto sem aprovação, rastreabilidade completa: ideia → pesquisa → criativo → publicação → métricas → aprendizado.
