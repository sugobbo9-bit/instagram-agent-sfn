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
