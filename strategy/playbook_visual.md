# Playbook visual — marca x marca (17h) e fotos no carrossel técnico (12h)

_Criado em 2026-10-06 a pedido do Victor. As rotinas diárias leem este arquivo. A revisão de domingo pode e deve reescrevê-lo quando os dados mandarem._

## Por que isso existe

O post "Se carboidrato de performance fosse carro" (10/09/2026) teve alcance 762 e **34 compartilhamentos — shares/reach de 4,5%**, a maior taxa da conta no período. Os carrosséis técnicos da mesma janela ficaram em 1–2 shares. Era o único post com **foto** e o único com **humor**.

É **um** post. Trate como hipótese forte, não como lei. As primeiras 10 peças `prov_*` são o teste.

## 1. O carrossel das 17h: marca X vs. marca Y (`vs_NNN`, só Instagram)

### Diretriz do Victor (09/10/2026)

As analogias "Se X fosse Y" (`prov_001` a `prov_003`) **ficaram exageradas** e foram encerradas. O slot das 17h passa a ser **dois produtos reais, lado a lado, só com o que está no rótulo — sem julgamento de valor**. Nada de nota, vencedor, "melhor", "pior", "vale a pena" ou piada às custas de um produto. Quem tira a conclusão é o leitor.

O quality gate reprova palavras de julgamento (`melhor`, `pior`, `vence`, `ganha`, `perde`, `superior`, `inferior`, `vale a pena`, `ruim`, `ótimo`...) e post sem fonte de rótulo datada.

### Como escolher a dupla

1. **Mesma categoria e porção comparável:** gel com gel, creatina com creatina, isotônico com isotônico. Compare por unidade de uso (sachê, dose, scoop) e diga qual.
2. **Os dois vendidos no Brasil** e com rótulo acessível no site oficial do fabricante. Sem rótulo oficial legível → troque a dupla.
3. **Rodízio:** não repita a categoria do post anterior; não repita uma marca em 3 posts seguidos.
4. **Z2:** pode entrar, com o mesmo rigor de dados e o mesmo tratamento neutro de qualquer marca (decisão do Victor, 09/10/2026). No máximo 1 vez por semana, para a série não parecer girar em torno de uma marca.
5. Marque `"category:<categoria>"` e `"pair:<marca-a>-<marca-b>"` nas tags.

Categorias para girar: gel de carboidrato · bebida de carboidrato em pó · isotônico pronto · cápsula/pastilha de eletrólito · creatina · whey · cafeína (cápsula, gel ou goma) · barra de endurance · beta-alanina · nitrato/beterraba.

### Os dados (a parte que não pode errar)

- **Fonte:** só o rótulo e o site **oficial** do fabricante. Nunca loja, blog ou review. Abra a página e o painel de informação nutricional; se o painel for imagem, olhe a imagem (Read) e transcreva.
- **Registre** em cada produto: `label_source: {url, consulted: "AAAA-MM-DD", notes}`. Anote em `notes` de onde saiu cada número.
- **Faixa quando varia:** se o número muda com o sabor/versão, mostre a faixa e escreva "varia com o sabor". Nunca escolha o sabor que favorece um lado.
- **Versão:** se o rótulo consultado for estrangeiro, diga na legenda e no slide final que a versão vendida no Brasil pode ter diferenças.
- **Não informado** é dado: escreva "não informado" em vez de deduzir.
- **Preço:** só se estiver no site oficial no dia, com a data; senão, deixe fora.

### Estrutura (modelo: `content/approved/vs_001.json`)

1. `cover` com `"vs": true`: headline curta ("Dois géis.\nSó o rótulo."), as duas embalagens, tagline "Sem nota. Sem vencedor."
2. 4 a 6 slides `metric`: uma métrica por slide, os dois valores com o mesmo tamanho e a mesma cor. `note` curta embaixo do valor quando precisar ("varia com o sabor"). `footnote` opcional no pé.
3. `fact` no fim: "O que o rótulo não diz" — a ciência que ajuda a **ler** os números (quanto carbo por hora, quanto sódio se perde no suor, que dose de creatina tem evidência), com fonte. Explica, não escolhe.

Métricas que costumam caber: tamanho da porção · nutriente principal por porção (carbo, proteína, creatina, cafeína) · fonte/tipo (ex.: glicose + frutose; whey concentrado/isolado) · sódio · cafeína · o que mais vem dentro · selo de terceira parte (só se estiver no rótulo/site).

### Imagens

Foto oficial da embalagem, do site do fabricante, sem alterar o rótulo, com fundo branco (`"mode": "multiply"`; PNG transparente → compor sobre branco antes). Crédito em `image_credits` com `"kind": "packshot"`. As fotos dos produtos ficam em `products[].image` e aparecem em todos os slides `metric`.

### Legenda

Abre com "Lado a lado, só com o que está no rótulo. Sem nota e sem vencedor." → resumo dos números de cada produto → a fonte e a data da consulta (e a ressalva de versão, se houver) → "Que dupla você quer ver lado a lado?" → referências científicas do slide final → "Imagens: fotos de produto dos sites oficiais" → hashtags.

### Histórico: "Se X fosse Y" (07–08/10/2026, encerrado)

`prov_001` (suplemento/carro), `prov_002` (proteína/banda) e `prov_003` (eletrólito/xadrez) seguem no ar. O banco de ideias foi aposentado a pedido do Victor ("ficou exagerado"). Não gere novos `prov_*`.

## 2. Fotos e hook no carrossel técnico (`draft_NNN` / `der_*`, ~12h BRT)

- **Capa:** slide `hook` com `"image"` (foto escura/contrastada funciona melhor sob o texto) e `"kicker"` de 1–3 palavras em etiqueta lima: "O mito", "O erro", "O número", "Teste". A headline da capa fica em até ~45 caracteres; o resto do argumento vai para o slide 2.
- **Miolo:** `"image"` em 2 ou 3 slides (nunca em todos — o respiro de texto puro é parte do ritmo). Slide com foto comporta menos texto: até ~55 palavras no body. O render avisa se encolheu a fonte; se avisar abaixo de 85%, corte texto.
- `"image"` aceita `{"path": "...", "focus": "center 40%"}` para ajustar o enquadramento.
- A capa do artigo no Ghost (`cover.png`) herda a foto do hook automaticamente.
- Mesmas regras de licença e `image_credits`. CC0 dispensa crédito na legenda.

### Hook mais afiado — checklist

1. Tem **tensão**? (algo que o leitor faz/acredita × o que o dado mostra)
2. Tem **número ou consequência concreta**? ("rouba seu sono", "3% mais rápido", "24h, não 6 dias")
3. Cabe em uma respirada? Corte advérbio e subordinada.
4. É **verdadeiro sem asterisco**? Se precisa de "em alguns casos", o hook está errado, não incompleto.

Vencedores para estudar: "Cafeína 6 horas antes de dormir ainda rouba seu sono. Sem você notar." (979) · "Você não precisa de 6 dias pra encher o glicogênio. Bastam 24h." (950) · "Lactato foi o vilão…" (2.450).

## 3. Horário — o que os dados realmente sustentam

A regra "15h UTC rende 3x" **está confundida**: 8 dos 17 posts de 15h UTC saíram no mesmo dia (03/07, lote de alto alcance) e as faixas "ruins" de 16h e 17h UTC são quase inteiras o lote de 07/08 (17 posts no mesmo dia). O 11h UTC (n=13, 13 dias distintos, mediana 269) é o único dado limpo, e coincide com a fase de carrossel só-texto.

Conclusão honesta: **meio-dia BRT é um teste razoável, não um fato medido.** A partir de 07/10 o técnico sai ~12h BRT com a tag `time:12brt`. Compare com os 13 posts de 11h UTC só depois de ≥10 posts, e lembre que foto e hook mudaram junto — o efeito do horário sozinho não será isolável.

## 4. Como medir

- Tags obrigatórias no marca x marca: `template:versus`, `series:marca-vs-marca`, `category:<categoria>`, `pair:<a>-<b>`. No técnico com foto: `visual:foto`, `time:12brt`.
- Métrica principal do marca x marca: **saves/reach e shares/reach** (baseline do técnico recente ≈ 1,1% e 0,8%). Compare também com os 3 `prov_*`.
- Métrica principal do técnico: **saves/reach** e alcance mediano (meta: voltar a 500+).
- Depois de 10 `vs_*`: quais categorias seguram saves/shares acima da mediana do técnico? Dobre nelas.
