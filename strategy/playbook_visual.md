# Playbook visual — carrossel provocativo (17h) e fotos no carrossel técnico (12h)

_Criado em 2026-10-06 a pedido do Victor. As rotinas diárias leem este arquivo. A revisão de domingo pode e deve reescrevê-lo quando os dados mandarem._

## Por que isso existe

O post "Se carboidrato de performance fosse carro" (10/09/2026) teve alcance 762 e **34 compartilhamentos — shares/reach de 4,5%**, a maior taxa da conta no período. Os carrosséis técnicos da mesma janela ficaram em 1–2 shares. Era o único post com **foto** e o único com **humor**.

É **um** post. Trate como hipótese forte, não como lei. As primeiras 10 peças `prov_*` são o teste.

## 1. O carrossel provocativo (`prov_NNN`, só Instagram, diário ~17h BRT)

### O que "provocativo" quer dizer na SFN

Provoca **uma crença, um hábito ou um claim de marketing** — nunca uma pessoa, um profissional ou um grupo. Humor seco, frase curta, zero grito. A piada precisa ser **verdadeira**: cada slide engraçado tem que sobreviver à pergunta "isso está certo?". O último slide sempre entrega o fato e a fonte.

Reação que queremos: "kkk é isso mesmo" → manda pro parceiro de treino. Reação que não queremos: "que exagero" ou "isso é propaganda".

### O conceito é um só: "Se X fosse Y" (diretriz do Victor, 07/10/2026)

O Victor aprovou o piloto e fechou a direção: **pegar o conceito do post dos carros e criar ideias novas dentro dele** — não inventar formatos diferentes. Todo `prov_*` é uma analogia "Se X fosse Y" com par de imagens (`series: "se-fosse"`). O que muda de um dia para o outro é o X, o Y e a piada.

**Como montar uma boa:**

1. **X é uma família de 5 ou 6 coisas entre as quais o atleta realmente escolhe** — fontes de carbo, suplementos, proteínas, bebidas, estratégias de prova.
2. **Y é um universo que todo mundo conhece e em que cada membro tem "personalidade"** — carros, carros antigos brasileiros, ferramentas, instrumentos, bichos, peças de xadrez, eletrodomésticos, estradas.
3. **Cada par carrega uma propriedade verdadeira** (custo, velocidade, confiabilidade, efeito colateral, onde funciona). Escreva a propriedade primeiro e só depois procure o Y. Se o par não ensina nada, troque.
4. **Ordem:** abre com o par mais reconhecível, fecha com a virada — o barato que funciona ou o bonito que não entrega.
5. **Último slide:** o fato e a fonte, sempre.

**Rodízio:** não repita o universo Y dos 2 posts anteriores. Carro é o universo comprovado — pode voltar até 2 vezes por semana, sempre com um X novo.

**Versão comparativa (marcas reais):** o post original comparava produtos de verdade. Isso continua possível como variação do mesmo conceito, no máximo **1 vez por semana**, com `"comparativo": true`, dados de rótulo oficial conferidos no dia (anote a data em `notes`) e foto de embalagem do site do fabricante. Descreva característica, nunca insulte produto. A Z2 pode aparecer aqui se o critério técnico justificar, nunca sozinha no topo e nunca como "a melhor". Fora da versão comparativa, **nenhuma marca de suplemento** — e a palavra "Z2" reprova no quality gate.

### Banco de ideias

Use a primeira ideia da lista que ainda não saiu (confira a tag `idea:<id>` nos `prov_*.json` de `content/approved/`) e marque a sua com essa tag. As âncoras de evidência são **ponto de partida, não citação pronta**: abra cada uma e confirme antes de escrever; se não confirmar, ajuste o post ao que a fonte diz ou pule a ideia. Banco acabou → crie ideias novas pelas regras acima e acrescente aqui.

| id | hook | X (esquerda) | Y (direita) | o fato por trás | âncoras para conferir |
|---|---|---|---|---|---|
| `raiz-carro-antigo` | Se comida raiz de prova fosse carro antigo. | rapadura, bananada, batata cozida, mel, banana, paçoca | Fusca, Kombi, Brasília, Chevette, Variant | Carbo de comida comum sustentou o desempenho como gel em estudos; o que muda é praticidade, fibra e gordura (a paçoca anda, mas pesada) | Nieman 2012 (banana, PLoS One); Salvador 2019 (batata, J Appl Physiol) |
| `proteina-banda` | Se proteína fosse instrumento de banda. | whey, caseína, ovo, soja, colágeno | guitarra, baixo, bateria, teclado, triângulo | Velocidade de digestão e teor de leucina mudam o papel de cada uma; colágeno não estimula síntese muscular como whey | Boirie 1997 (PNAS); Oikawa 2020 (Am J Clin Nutr); Jäger 2017 (ISSN position stand) |
| `eletrolito-xadrez` | Se eletrólito fosse peça de xadrez. | sódio, cloreto, potássio, cálcio, magnésio | rainha, torre, bispo, cavalo, peão | O sódio é de longe o que mais se perde no suor; magnésio para cãibra não tem suporte | Baker 2017 (Sports Med); Garrison 2020 (Cochrane) |
| `intestino-transito` | Se o seu intestino na prova fosse trânsito. | 30, 60, 90 e 120 g de carbo por hora | rua de bairro, avenida, rodovia de pista dupla, engarrafamento | Glicose sozinha satura perto de 60 g/h; glicose + frutose usam transportadores diferentes; o intestino é treinável | Jeukendrup 2014 (Sports Med); Cox 2010 (J Appl Physiol) |
| `recuperacao-eletro` | Se recuperação fosse eletrodoméstico. | sono, comida (carbo + proteína), banho de gelo, massagem, bota de compressão | geladeira, fogão, ar-condicionado, ventilador, luminária | Sono e comida fazem o grosso; água fria alivia, mas pode atenuar adaptação de força; massagem reduz a dor percebida | Roberts 2015 (J Physiol); Dupuy 2018 (Front Physiol) |
| `cafeina-bicho` | Se fonte de cafeína fosse bicho. | café coado, cápsula, gel com cafeína, chiclete, energético | bichos de velocidades diferentes | Café e cafeína anidra renderam igual; chiclete absorve mais rápido; a dose importa mais que a fonte | Hodgson 2013 (PLoS One); Kamimori 2002 (Int J Pharm); Guest 2021 (ISSN) |
| `formato-ferramenta` | Se gel, bebida, barra e goma fossem ferramentas. | gel, bebida, barra, goma, comida de verdade | ferramentas de uma caixa | Com a mesma composição, a oxidação do carbo é parecida entre os formatos — a escolha é logística | Pfeiffer 2010 (Med Sci Sports Exerc, dois artigos) |
| `queimador-acessorio` | Se "queimador de gordura" fosse acessório de carro. | cafeína, chá verde, L-carnitina, CLA, cetona de framboesa | turbo pequeno, adesivo, aerofólio, neon, aromatizante | Efeito pequeno ou nulo na perda de gordura para quase todos; só a cafeína tem algum respaldo | Jeukendrup & Randell 2011 (Obes Rev) |
| `pre-prova-transporte` | Se o seu café pré-prova fosse meio de transporte. | pão com geleia, banana, ovo com bacon, açaí com granola, só café preto | metrô, bicicleta, caminhão de mudança, ônibus lotado, ir a pé | 1 a 4 g/kg de carbo, 1 a 4 h antes; gordura e fibra demais atrasam o estômago | Burke 2011 (J Sports Sci); Thomas 2016 (ACSM) |
| `pos-treino-carro` | Se bebida pós-treino fosse carro. | leite achocolatado, shake de whey, isotônico, água, cerveja | carros (X novo, universo comprovado) | Leite achocolatado recupera tão bem quanto bebida comercial; álcool atrapalha a síntese proteica | Amiri 2019 (Eur J Clin Nutr); Parr 2014 (PLoS One) |
| `bebida-carbo-carro` (comparativo) | Se bebida de carbo fosse carro. | 5 ou 6 bebidas de carboidrato do mercado nacional | carros | Compare por g de carbo por porção, razão glicose:frutose, sódio e preço por 30 g | rótulos oficiais conferidos no dia; Jeukendrup 2014 |

### Estrutura

6 a 8 slides: `cover` → 4 a 6 slides `pair` (use `single` quando o X não tiver imagem, como um número) → `fact` (obrigatório).

- **headline:** 2 linhas, até ~18 caracteres por linha. Use `\n` para quebrar onde a piada respira.
- **tagline:** 1 frase, até ~60 caracteres. É aqui que mora o fato disfarçado de piada.
- **fact:** `label` "O fato por trás da piada", headline curta, 2 parágrafos, `source` com autor/periódico/ano, `cta` em forma de pergunta.
- Hook (campo `hook`) ≤ 80 caracteres.

Modelo completo e aprovado no gate: `content/approved/prov_001.json`. Copie a estrutura, não o tema.

### Imagens — de onde vêm

1. **Pote genérico SFN** (`{"pot": "CREATINA"}`): desenho próprio em SVG, sem marca. Padrão para qualquer suplemento/ingrediente. Não procure foto de pote.
2. **Banco livre de qualidade (nuvem):** `python3 scripts/fetch_image.py search "<termo em inglês>" <dir>` → StockSnap, rawpixel, WordPress Photos (CC0). Bom para comida, objeto, cena de esporte.
3. **Wikimedia Commons (só pelo Mac):** `--provider commons`. Para coisa específica com nome próprio (modelo de carro, objeto). A nuvem leva 429; rode via `device_bash`, com saída em `$HOME/mnt/SFN/_agent_buffer/_img/<id>/<termo>/`, e traga `sheet.jpg` e a escolhida com `device_stage_files`. Termos curtos funcionam melhor ("Toyota Hilux", não "Toyota Hilux Revo front").
4. **Embalagem de marca:** só em `comparativo`, baixada do site oficial do fabricante, sem alterar o rótulo, com `{"kind": "packshot"}` no crédito. Fundo branco → `"mode": "multiply"`.

Sempre olhe a `sheet.jpg` com Read antes de escolher. Objeto isolado → `fetch_image.py cutout` e `"mode": "cutout"`; confira o PNG. Recorte sujo → outra foto, ou `"mode": "photo"`.

### Regras de imagem (o quality gate confere parte delas)

- Só licença **CC0, domínio público ou CC BY**. Nunca BY-SA, NC, ND.
- Toda imagem usada entra em `image_credits` (label, title, creator, license, source_url). CC BY exige o nome do autor **na legenda**.
- **Nada de rosto identificável** — em nenhum dos dois formatos. Licença livre resolve direito autoral, não direito de imagem de quem aparece. Silhueta, costas, borrão e multidão distante podem. Isso é verificado em código (`scripts/face_check.py`): a busca carimba "ROSTO" na candidata, o render grava `face_check` no JSON e o quality gate reprova. O detector não pega tudo — confira no olho também.
- Descarte anúncio escaneado, print de tela, marca d'água, logotipo dominante.
- Sem foto boa? O slide sai com pote ou só tipografia. **Foto nunca bloqueia publicação.**

### Legenda

1. Abre com `(Post de humor. A piada é nossa; os dados, não.)`
2. O contexto real em 3–6 linhas — o que o estudo diz, com as ressalvas que não couberam nos slides.
3. Pergunta de fechamento.
4. `Referências:` completas. 5. `Fotos:` créditos. 6. Hashtags (6–8).

Mantenha `Formato inspirado em @jessicathesportsrd` na legenda — o conceito veio de lá.

### Não negocie

Sem estudo inventado. Sem prescrição individual. Sem shaming alimentar. Sem atacar pessoa. Sem "compre isso". Dúvida entre a piada e a precisão → precisão.

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

- Tags obrigatórias no provocativo: `template:provocativo`, `series:se-fosse`, `idea:<id>`, `universe:<Y>`. No técnico com foto: `visual:foto`, `time:12brt`.
- Métrica principal do provocativo: **shares/reach** (baseline do carrossel técnico recente ≈ 0,5–1%; o post dos carros fez 4,5%). Secundárias: alcance, follows.
- Métrica principal do técnico: **saves/reach** e alcance mediano (meta: voltar a 500+).
- Depois de 10 `prov_*`: qual universo Y e qual família X seguram shares/reach acima de 2%? Dobre neles, aposente os piores.
