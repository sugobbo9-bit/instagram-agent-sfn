# Estratégia Atual — @sofatosnutricao
_Atualizado: 2026-09-27, revisão estratégica semanal_
_Base: 9.418 seguidores (+152 na semana — melhor semana registrada) | 160 publicações com métricas reais (Graph API, coletadas 27/09)_

## O que os dados dizem agora

### Medianas por formato (amostra completa, normalizado)
| formato | n | alcance mediano | p90 | p75 | p25 | shares/reach | saves/reach |
|---|---|---|---|---|---|---|---|
| **carrossel** | 65 | **474** | 1.232 | 838 | 197 | 0,0095 | 0,0177 |
| reel | 77 | 256 | 515 | 381 | 168 | 0,0000 | 0,0052 |
| estático | 18 | 206 | 377 | 313 | 155 | 0,0083 | 0,0116 |

### Janela recente (o que saiu de fato)
- **Últimos 7 dias:** 4 carrosséis (mediana 296) + 5 estáticos (mediana 150) + 0 Reels.
- **Últimos 14 dias:** 9 carrosséis (mediana 320) + 11 estáticos (mediana 181) + 0 Reels.
- O alcance recente do carrossel está **abaixo do baseline** (320 vs 474). Os grandes carrosséis do início de setembro saíram da janela; os recentes são majoritariamente medianos/fracos.

## Conclusões

### 1 — Crescimento de seguidores acelerou, mesmo com alcance fraco.
+152 seguidores na semana (9.266 → 9.418), a melhor semana já registrada, apesar do alcance recente abaixo do baseline. A conta está **convertendo melhor por alcance** — provável efeito dos poucos carrosséis de alto salvamento (carga de carbo: saves/reach 0,039). Como a Graph API ainda não entrega follows/reach por post, a conversão não é otimizável no nível do post; o agregado, porém, está saudável. **Não sacrificar qualidade por alcance bruto.**

### 2 — DUAS decisões da revisão anterior seguem SEM implementação (3ª semana).
Esta é a descoberta dominante do ciclo e um problema de **execução, não de estratégia**:
- **Estáticos NÃO foram pausados.** Saíram 11 estáticos em 14 dias, um por dia às 20h UTC, todos no fundo (109–242). É a mesma ineficiência apontada em 20/09 e 23/09.
- **Horário NÃO mudou.** Carrosséis seguem saindo às **11h UTC (08h BRT)** — janela fraca (mediana 317) — em vez de 15h UTC (mediana 828). O publisher **ignora `scheduled_for`** e publica o próximo item `approved` por prioridade quando é dispachado; quem define o horário são os dispatches da rotina DIÁRIA (workflow_dispatch ~11h para carrossel e ~20h para estático) e o cron do publish.yml.
- **NÃO foi possível corrigir via automação:** o token (PAT) não tem escopo `workflow`, então o loop semanal **não consegue** alterar `.github/workflows/publish.yml` (o push é rejeitado). A mudança do cron `0 12`→`0 15` UTC precisa ser feita pelo Victor. E, de qualquer modo, a maior parte das publicações vem dos dispatches da rotina diária, fora do alcance do loop semanal. → escalado ao Victor.

### 3 — Myth-busting + protocolo prático seguem sendo o padrão vencedor.
Vencedores do ciclo: **carga de carboidrato/depleção (918, saves/reach 0,039)** — maior valor de salvamento do ciclo — e **cafeína (975)**. Ambos derrubam uma crença e entregam algo acionável. Os maiores alcances históricos continuam sendo carrosséis de ruptura (lactato 2.450/1.516, sono 2.437, carbo/intestino 1.426, creatina 1.249).

### 4 — Comparação de produto continua sendo o motor de compartilhamento.
Recordes de shares/reach são comparações concretas (hidrogel 0,130; "Uno vs Ferrari" 0,045). Mantida no topo da fila (der_comparacao_gel_bebida).

### 5 — Bom tópico morre com hook/execução fraca.
**Extensão de sono (178)** é o alerta do ciclo: sono é o tópico de MAIOR alcance mediano da conta (1.164), mas o derivado fez 178 — hook mole ('a maioria acha que dorme o suficiente', sem número) + horário ruim (11h UTC). Diagnóstico: hook + timing, não tópico. **Reteste enfileirado** com hook de número na janela de 15h UTC (experimento controlado).

### 6 — Tópicos de nicho reconfirmados no fundo.
Cetonas exógenas (168, 0 share/0 save) e janela anabólica (271, saturada) no fundo. Suplemento de nicho e mitos já muito batidos têm teto baixo. Reduzir.

### 7 — Horário e dia (reconfirmado com base ampliada).
Melhor horário: **15h UTC (12h BRT) mediana 828**; 18h UTC (15h BRT) 762. Piores: 11–12h UTC (~317) e 16–17h UTC (158–212). Pior dia: **sexta** (n=31, mediana 256) vs segunda (682), terça (630), quinta (610).

## Decisões para o próximo ciclo

1. **Carrossel = formato padrão** (mantido). Reel só como experimento de conteúdo intrinsecamente visual.
2. **Pausar de fato a série estática.** O estático fica reservado a um único dado/gráfico excepcional. *Requer ação na rotina diária — ver Pendências.*
3. **Publicar às 15h UTC (12h BRT).** Nunca às 11–12h nem 16–17h UTC. Nunca carrossel na sexta. *Requer ação do Victor: cron do publish.yml (token sem escopo workflow) e dispatches da rotina diária — ver Pendências.*
4. **Explorar a família vencedora "carga de carboidrato":** 2 derivados enfileirados (passo a passo; erros que sabotam).
5. **Retestar sono** com hook de número + horário certo (experimento exp_sono_hook_timing).
6. **Priorizar** myth-busting prático em fueling/periodização, hidratação, sono, cafeína e comparação de produto. **Reduzir** nicho (cetonas, BCAA, antioxidantes) e mitos saturados (janela anabólica).
7. **Meta do ciclo:** recuperar o alcance mediano do carrossel para 500+ ligando a janela de 15h UTC (cron + dispatches diários); concluir o experimento de sono.

## Pendências de dados / execução
- **CRÍTICO (3ª semana): a rotina DIÁRIA precisa (a) parar de produzir/publicar estáticos e (b) dispachar carrosséis às 15h UTC (não 11h).** O loop semanal ajusta estratégia e fila, mas não controla os `workflow_dispatch` diários. Sem essa correção na rotina diária, as duas maiores alavancas continuarão desligadas.
- **CRÍTICO: dar escopo `workflow` ao PAT (ou mudar o cron manualmente).** O token atual não permite editar `.github/workflows/` — o loop semanal tentou mover o cron `0 12`→`0 15` UTC e o push foi rejeitado. Enquanto isso, o cron segue em `0 12` (09h BRT, janela fraca).
- follows/reach e visitas ao perfil ainda não vêm no import da Graph API — otimização por conversão em seguidor segue cega no nível do post.
- Demografia da audiência e online_followers: token da Página válido e não expira; puxar no próximo ciclo para validar a janela de horário com dados de audiência online.

## Regras imutáveis
Integridade científica, sem engajamento falso, sem gasto sem aprovação, rastreabilidade completa: ideia → pesquisa → criativo → publicação → métricas → aprendizado.
