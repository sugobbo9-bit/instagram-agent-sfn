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
