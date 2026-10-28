# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo. SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-10-28 (6ª execução)_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida por dado próprio** (idade, gênero, país/cidade, `online_followers` seguem **desconhecidos**). O bloqueio mudou de forma nesta rodada: **agora existe um `.env` no Mac** (`SFN/Instagram Agent/.env`) com um `INSTAGRAM_ACCESS_TOKEN` de 306 chars — mas ele está **EXPIRADO desde 26/08/2026** (Graph API devolve OAuthException 190, "Session has expired"). O token válido continua vivendo só como **Secret do GitHub Actions**. E **não há arquivo de demografia/comentários commitado** no repo (`data/` não tem `audience_demographics.json` nem `comments_recent.json` — reconfirmado). Ver "Demografia — bloqueio".
- **Base: 9.516 seguidores** (snapshot do bootstrap de 11/10). A série semanal: 9.266 → 9.418 (+152) → 9.529 (+111) → **9.516 (−13)**. A **1ª semana não-positiva** segue sendo o dado mais recente — **não há coleta nova desde 11/10** para confirmar se virou tendência ou ruído. Conta `sofatosnutricao`, IG id `17841472609243044`.
- Perfil presumido pelo nicho (hipótese, **não medido**): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 178 posts com métricas reais; coleta única "import" de 11/10/2026; 185 posts no total)
- **O carrossel domina — padrão forte e repetido em 6 coletas (16/09 → 11/10).**

  | formato | n | alcance mediano | p90 | p75 | p25 | média saves/r | média shares/r | média likes/r | média comments/r |
  |---|---|---|---|---|---|---|---|---|---|
  | **carrossel** | 79 | **366** | 1.245 | 764 | 197 | 0,0189 | 0,0143 | 0,0421 | 0,0011 |
  | reel | 77 | 256 | 520 | 381 | 168 | 0,0068 | 0,0040 | 0,0135 | 0,0010 |
  | estático | 22 | 226 | 359 | 326 | 171 | 0,0122 | 0,0069 | 0,0323 | 0,0017 |

  O top 10% de alcance da conta é quase todo carrossel (900–2.450); o fundo (bottom 25%) é dominado por Reels (incluindo os Reels em inglês de abr/2026, pré-pivô) e carrosséis de versus/commodity. Baseline do carrossel **estável em 366** vs. a coleta de 04/10.
- **Estrutura vencedora reconfirmada:** os maiores alcances derrubam uma crença aceita + entregam protocolo. Campeões (mai–jul): lactato (2.450 / 1.516), privação de sono→composição (2.441), cafeína (1.558), intestino treinado 60g/h (1.426), creatina (1.249), hidrogel comparado (1.245), janela de 30 min (1.212), RED-S (1.180), magnésio/sono (1.164). **Único vencedor novo de grande alcance:** o breakout de **carga de carbo (1.661, 07/10, saves/r 0,049 — o maior da conta)**.
- **NOVO ACHADO (hook): contrarian > myth genérico.** Com os posts agente-era já medidos:
  - `hook:contrarian` (**n=7**): alcance mediano **424**, saves/r mediano **0,018**. Inclui carga-carbo 1.661, periodização 951, bicarbonato 424.
  - `hook:myth` (**n=16**): alcance mediano **312**, saves/r mediano **0,011**. Backbone estável (cafeína 979, proteína 683, cãibra 656, jejum 627), mas teto e densidade de save menores que o contrarian.
  - Leitura: enquadrar como "o protocolo que quase todo mundo faz errado" (contrarian) rende mais save que "esse mito diz X" (myth). Amostra ainda modesta, mas a direção é consistente com os campeões all-time.

### O que eles comentam
- **A audiência salva e compartilha, mas quase não comenta** — idêntico em todas as coletas. **91 comentários** somando 178 posts; apenas **38 posts com ≥1**; **mediana 0 por post**. Comentar não é o comportamento dominante.
- Maior ímã de comentário (contagem): **Reel de nitrato (16 comentários)**, muito acima de tudo; depois um pelotão de ~3–5 em **comparação de produto** (maltodextrina 5, ranking carbo em pó 5, hidrogel 5, "15 g carbo/h" 5, melhor-café humor 4, gel 4) e no carrossel de **magnésio/sono (4)**. Hipótese estável (ainda só por contagem): perguntas "serve pra mim?" concentram-se em **comparação de produto** — exatamente o terreno do futuro banco de respostas.
- **Texto dos comentários: ainda não lido** — depende de token válido + escopo `instagram_manage_comments`. O `posts_db.json` guarda só a contagem.

### Novos formatos (agente-era) — AGORA com métrica (coleta 11/10), mas amostras pequenas
- **Técnico com foto (`visual:foto`, n=3):** 1.661 / 272 / 226. O breakout foi **UM post** — e era a **família campeã (carga de carbo)**. Os outros dois posts com foto (sono 272, ice-slurry 226) foram medianos. **A foto NÃO é a alavanca isolada** — ela andou junto do tópico campeão. Não declarar "foto = padrão vencedor" com n=3; medir ≥10.
- **Provocativo / "se fosse" (`prov_*`/`se-fosse`, n=3):** 484 → 253 → 164, saves/shares baixíssimos. **Confirma a decisão de ENCERRAR** (o Victor já encerrou). A curiosidade não se sustenta após o 1º.
- **Versus "marca vs marca" (`vs_*`, n=2):** 436 (gel diferenciado Maurten×GU) vs **109 (creatina commodity, 0 shares)**. **Confirma a hipótese:** versus só rende quando os produtos **diferem de fato**. (Nota: `vs_005` beta-alanina Max×Atlhetica foi publicado 27/10 — ainda sem métrica; vai testar de novo a regra "só produtos distintos".)
- **hook:number (n=2):** 272/226 — fraco até agora, amostra mínima.

### Implicação de conteúdo (o que os dados sustentam)
Otimizar para **salvável/compartilhável** (carrossel de **mito/contrarian + comparação de produto que diferem**), não para "pergunta no fim pedindo comentário". Priorizar fueling / hidratação / sono / cafeína / **carga de carbo (família campeã)** / comparação de produto distinto; **reduzir suplemento de nicho** (pillar supplements n=12: alcance 234, shares/r só 0,004 — o fundo). Preferir hook **contrarian** ("quase todo mundo faz errado + número + protocolo") ao hook myth genérico.

### Janelas de publicação (carrossel, UTC) — com correção de LOTE (dias distintos)
Reconfirmado sobre o dataset de 11/10:

| janela UTC | nPosts | medPost | dias distintos | med/dia | leitura |
|---|---|---|---|---|---|
| **18h** | 10 | 696 | 7 | **630** | **melhor janela limpa** |
| 19h | 8 | 504 | 6 | 459 | boa |
| **14h** | 6 | 449 | 6 | **449** | boa (o breakout saiu aqui, 14h48) |
| 11h | 15 | 300 | 15 | 300 | **fraca, limpa e grande — e é onde a automação publica** |
| 20h | 4 | 454 | 4 | 454 | ok |
| 15h | 17 | 828 | 5 | 973 | **ainda confundida por lote — NÃO usar como âncora** |
| 16h / 17h | 6 / 7 | 158 / 213 | 2 / 2 | — | confundidas (poucos dias) |

**Dia da semana (dias distintos):** ter **552** (melhor) > qua 484 > qui 449 > seg 364 > **sex 331 (pior, 9 dias distintos)**. Fim de semana sem amostra. _(Nota: a seg caiu de 654→364 na recontagem por dias distintos desta rodada — não tratar seg como janela forte sem reteste.)_

**Janela recente:** últimos 10 carrosséis mediana **262** (05–10/10); últimos 20 = **267**. **Segue bem abaixo do baseline 366** — o problema recente é de alcance, não de formato.

---

## Demografia — bloqueio (agora: token do Mac EXPIRADO)
- Existe um `.env` no Mac (`SFN/Instagram Agent/.env`) com `INSTAGRAM_ACCESS_TOKEN` — porém **expirado em 26/08/2026** (OAuthException 190). Testado nesta rodada via `debug_token` e `GET /{ig-id}`: inválido.
- O token válido da Página segue como **Secret do GitHub Actions** (`secrets.INSTAGRAM_ACCESS_TOKEN`), write-only, inalcançável a esta rotina que roda no Mac.
- **Não há arquivo de demografia/comentários commitado** no repo (reconfirmado).
- Nenhuma chamada a `follower_demographics`/`engaged_audience` (breakdown age/gender/city/country), `online_followers` ou `{media-id}/comments` é possível a partir daqui.

**Para desbloquear (decisão do Victor):**
- **(preferida)** Passo no **GitHub Actions** que puxe `follower_demographics`/`online_followers` **e o texto dos comentários** dos ~15 posts recentes e **commite** `data/audience_demographics.json` + `data/comments_recent.json`. Aí esta rotina lê dado próprio sem token no Mac.
- **(rápida p/ já)** Regerar o token de longa duração e atualizar o `.env` do Mac (com `instagram_manage_insights` + `instagram_manage_comments`) — duplica credencial fora do Actions, mas destrava demografia E comentários imediatamente para o estudo.
- Métricas vigentes: `follower_demographics`/`engaged_audience` com `breakdown` age/gender/city/country; `online_followers` p/ horários. Requisito mínimo de seguidores (9,5k) costuma ser atendido; confirmar escopo ao instrumentar.

---

## Comentários — PENDENTE de token válido + escopo `instagram_manage_comments`
O estudo do **texto** dos comentários segue **não executado**: (1) token do Mac expirado; (2) ler/responder comentário exige **`instagram_manage_comments`** — o mesmo escopo necessário para responder no futuro. O embrião do **banco de respostas** (sentimento + perguntas/objeções mais frequentes) fica parado. Só por contagem: volume baixíssimo (91 comentários / 178 posts, mediana 0), concentrado em **comparação de produto** e no **Reel de nitrato**.

---

## Lacunas de dados (o que ainda não conseguimos medir)
- Demografia (idade/gênero/local) e `online_followers` — token do Mac expirado; sem arquivo próprio.
- **follows/reach** e `profile_visits` por post — o snapshot `import` do `posts_db.json` não traz esses campos; conversão em seguidor segue **cega no nível do post**.
- Texto/sentimento dos comentários — ver acima.
- **Coleta de métricas parada em 11/10 (~17 dias atrás).** O agente seguiu publicando até 27/10 (cards informativos `card_*`, `der_cafeina_dose_timing`, `vs_005`), mas **nada depois de 10/10 foi medido** (5 posts de 26–27/10 sem métrica). Toda a safra pós-11/10 — inclusive a nova série `card_*` de 19h30 — está **invisível** até a próxima coleta.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-10-28 (6ª execução)
**O que foi feito:** 1ª análise de audiência sobre a **coleta de 11/10** (178 posts medidos / 185 no total). Teste direto do token agora presente no `.env` do Mac (resultado: **expirado 26/08**). Reconfirmação de que não há arquivo de demografia/comentários no repo. Reanálise de engajamento por formato, hook, pillar, janela (dias distintos) e contagem de comentários. Novos formatos agente-era medidos pela 1ª vez.

**O que mudou desde a última execução (07/10):**
- **Coleta nova (11/10):** de 168→**178 posts medidos** (185 total). Todos com checkpoint único `import`, `collected_at = 11/10`. Post medido mais recente: **10/10**.
- **Novos formatos finalmente têm número:** foto (n=3), provocativo (n=3), versus (n=2), hook:number (n=2) — ver seção "Novos formatos". Principais leituras: **o breakout da foto foi 1 post de família campeã (não a foto isolada)**; provocativo e versus-commodity confirmados como fracos.
- **Novo achado de hook:** **contrarian (n=7, med 424, saves/r 0,018) > myth genérico (n=16, med 312, saves/r 0,011)** — direção consistente; adicionado a `learnings.md`.
- **Seguidores:** série fechou em **9.516 (−13)**, 1ª semana não-positiva — e **sem dado novo desde 11/10** para confirmar tendência.
- **Token do Mac:** antes "vazio/sem .env"; agora **há .env, mas token expirado** — refinamento do bloqueio (regerar o token destrava tudo imediatamente).
- **Janelas reconfirmadas por dias distintos:** 18h UTC melhor limpa (630); 15h ainda confundida por lote; seg caiu para 364 na recontagem.

**Achados reconfirmados (estáveis em 6 coletas):** carrossel domina (366 vs 256 vs 226); myth/contrarian + protocolo vence; comparação de produto gera compartilhamento e concentra os poucos comentários; suplemento de nicho no fundo; audiência salva/compartilha e quase não comenta (mediana 0, Reel de nitrato outlier); alcance recente de carrossel (262) abaixo do baseline.

**Bloqueios que persistem:** demografia e texto de comentários **não medíveis** (token do Mac expirado, sem arquivo próprio commitado). **Coleta de métricas parada em 11/10** — a safra pós-11/10 (cards, novos der_*, vs_005) está invisível.

**A confirmar na próxima execução:**
- Se houve **coleta nova após 11/10** — destrava medir a série `card_*` (19h30), `vs_005` beta-alanina, `der_cafeina_dose_timing` e confirmar se o −13 virou tendência.
- Se o token do Mac foi **regerado** (ou se entrou o passo de Actions que commita demografia/comentários) — aí iniciar demografia + análise temática de comentários.
- Reteste do hook **contrarian > myth** com mais posts; e da foto como alavanca (≥10 posts com foto).

### 2026-10-07 (5ª execução)
Reanálise sobre a coleta de 04/10 (168 posts / 171 total). Reconfirmou bloqueios de token/demografia/comentários no Mac (à época: token vazio, sem `.env`). Baseline carrossel recomputado 474→418. Base 9.418→9.529 (+111). Incorporou correção de integridade das janelas (confundimento por lote; só 8h BRT era sinal limpo).

### 2026-09-30 (4ª execução)
Reanálise (160 posts / 163 total; coleta 27/09). Quadro idêntico ao ciclo 27/09. Base 9.266→9.418 (+152). Carrossel domina; myth-busting vence; comparação compartilha; nicho no fundo; mediana 0 de comentário.

### 2026-09-23 (3ª execução)
Reanálise (151 posts). Diagnóstico do bloqueio de demografia mudou de "token expirado" para **arquitetural** (token só no Actions). Registrados achados operacionais: horário publica ~08h BRT; estático não pausado.

### 2026-09-16 (1ª execução)
Primeira montagem do documento; 135 posts. Graph API falhou por token expirado (26/08). Achados: carrossel > Reel; sono/recuperação maior alcance mediano (1.164); sexta pior dia; audiência salva/compartilha e quase não comenta.

_(As revisões estratégicas e decisões — pausa/enforce do estático, proibição de sexta, famílias vencedoras, retestes, formatos prov_*/foto/versus, volta do card informativo 19h30 — estão em `current_strategy.md` e `learnings.md`.)_
