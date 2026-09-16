# Inteligência de Audiência — @sofatosnutricao (SFN)
_Documento vivo mantido pela rotina semanal de estudo (quarta-feira). SOMENTE análise — não publica, não comenta, não interage._
_Última execução: 2026-09-16_

---

## PERFIL ATUAL DA AUDIÊNCIA
_(resumo que evolui a cada semana — leia isto primeiro)_

### Quem são
- **Demografia ainda NÃO medida.** A Graph API não pôde ser consultada nesta rodada porque o **token de acesso expirou em 26/08/2026** (OAuth code 190, subcode 463). Faixa etária, gênero, país/cidade e horários de atividade dos seguidores seguem **desconhecidos por dados próprios** até o token ser renovado.
- Base declarada no projeto: **9.129 seguidores** (performance_history.json, snapshot de 09/09/2026), conta `sofatosnutricao`, ~114–144 posts.
- Perfil presumido pelo nicho (hipótese, não medido): público brasileiro de endurance (corrida, ciclismo, triatlo) interessado em nutrição esportiva baseada em evidência.

### O que engaja (medido em 135 posts com métricas, fev–set/2026)
- **O carrossel domina.** Alcance mediano **483** vs **256** dos Reels (+89%); saves/reach **0,019 vs 0,0052** (3,6x); shares/reach **0,0093 vs 0,000**. Dos 13 posts de maior alcance da conta, **12 são carrosséis**. Dos 25% de menor alcance, a maioria (21 de 33) são Reels. Padrão forte e repetido — não é ruído de amostra.
- **Temas que mais engajam (carrosséis, normalizado):**
  - **Sono/recuperação** — alcance mediano **1.164** (n=9): de longe o tema de maior alcance. Puxado por posts de mito ("privação de sono e composição corporal").
  - **Timing/janela** — mediano **630**, saves/reach **0,027** (n=11).
  - **Comparação/ranking** — mediano **515**, o **maior shares/reach** entre temas de volume (0,0127, n=23). Comparação de produto viaja.
  - **Hidratação/eletrólitos** — saves/reach **0,027** e shares/reach **0,026** (n=8): pouco volume, mas alta densidade de save+share.
  - **Mito/desmistificação** — mediano **466**, shares/reach **0,014** (n=26): estrutura vencedora recorrente ("X não é o vilão").
  - Mais fraco: **saúde hormonal** (mediano 155, n=5).
- **Estrutura vencedora confirmada:** os maiores alcances derrubam uma crença aceita (lactato não é vilão 2.450/1.516; sono e composição 2.437; cafeína não desidrata 1.558; janela de 30 min 1.212; detox é marketing 1.046).

### O que eles comentam
- **Volume de comentários é baixíssimo:** 81 comentários somando 135 posts, **mediana de 0 por post**. Comentar não é o comportamento dominante desta audiência — ela **salva e compartilha** muito mais do que comenta.
- O maior ímã de comentários foi um **Reel sobre nitrato** (16 comentários) e Reels de comparação (maltodextrina, ranking de carboidrato). Hipótese fraca (poucos casos): perguntas de "serve pra mim?" aparecem mais em Reels de comparação de produto.
- **Análise temática dos textos dos comentários: PENDENTE** — depende da Graph API (ver abaixo).

### Lacunas de dados (o que ainda não conseguimos medir)
- Demografia dos seguidores (idade/gênero/local) e **horários de atividade dos seguidores** (`online_followers`) — bloqueado pelo token expirado.
- **follows/reach** e profile_visits por post — o `posts_db.json` não guarda esses campos; não medível a partir do dado atual.
- Texto/sentimento dos comentários — ver seção pendente.

---

## Comentários — PENDENTE (token expirado + escopo)
O estudo do texto dos comentários dos posts recentes **não foi executado**. Dois bloqueios encadeados:
1. **Token expirado (26/08/2026):** nenhuma chamada à Graph API funciona hoje, nem `{media-id}/comments`.
2. Mesmo com token válido, ler comentários exige o escopo **`instagram_manage_comments`** no token — o mesmo escopo necessário para **responder** comentários no futuro. Confirmar que ele está presente ao renovar.
Enquanto isso, a leitura de sentimento e o levantamento das perguntas/objeções mais frequentes (embrião do futuro banco de respostas) ficam parados.

---

## HISTÓRICO POR EXECUÇÃO

### 2026-09-16 (1ª execução desta rotina)
**O que foi feito:** primeira montagem do documento. Análise de engajamento a partir de `posts_db.json` (135 posts com métricas). Tentativa de puxar demografia e comentários via Graph API.

**Bloqueio principal:** token de acesso **expirado em 26/08/2026**. Sem demografia própria e sem comentários nesta rodada. Victor foi notificado (push) para renovar o token de longo prazo e reconfirmar o escopo `instagram_manage_comments` no `.env`.

**Achados novos (dado local):**
1. Confirmação, agora com n maior (52 carrosséis, 77 Reels, 135 no total), do que a estratégia já suspeitava: **carrossel > Reel em todas as métricas**. Reforça a decisão de tornar carrossel o formato padrão.
2. **Sono/recuperação** é o tema de maior alcance mediano (1.164, n=9) — acima de suplemento, endurance e mito genérico. Hipótese acionável: **família de conteúdo sobre sono/recuperação** tem espaço para crescer.
3. **Janela de publicação:** carrosséis publicados na **sexta-feira** (n=29, o maior volume) têm o **pior alcance mediano (256)**; segunda (764), quinta (854) e o horário das **15h e 18h UTC (12h/15h BRT)** rendem muito mais. Hipótese: **parar de concentrar carrossel na sexta**. (Correlação, não causa — confirmar deslocando publicações para início/meio de semana.)
4. **A audiência salva e compartilha, quase não comenta** (mediana 0 comentários/post). Implicação para conteúdo: otimizar para "salvável/compartilhável" (listas, comparações, rankings, mitos) — não para pergunta-no-fim que peça comentário.

**A confirmar na próxima execução:**
- Renovar token → puxar demografia real (idade/gênero/local) e `online_followers` para validar/derrubar as janelas de horário achadas no dado local.
- Ler comentários (com escopo) → mapear perguntas/objeções recorrentes.
- Testar se deslocar carrossel da sexta para seg–qui sobe o alcance mediano.
