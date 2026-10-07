"""
render_provocativo.py — Carrossel "provocativo com imagens" (1080x1350).

Formato nascido do post "Se carboidrato de performance fosse carro" (10/09/2026,
maior shares/reach da conta): fundo creme, serifada, imagem grande, frase curta.
Humor com fato por tras — o ultimo slide SEMPRE entrega a evidencia.

Uso: python3 render_provocativo.py <post.json> <out_dir>

Tipos de slide (campo "type"):
  cover   headline + ate 2 itens (imagem+rotulo) + "arrasta"
  pair    headline + 2 itens lado a lado + tagline          (a analogia)
  single  headline + 1 item grande + tagline
  versus  headline + 2 itens com "vs" no meio + tagline
  fact    label + headline + body + source                  (o fato; obrigatorio no fim)

Item: {"image": "<caminho local>", "label": "...", "mode": "cutout|multiply|photo"}
   ou {"pot": "CREATINA", "pot_sub": "opcional", "label": "..."}  -> pote generico SFN
      desenhado em SVG (sem marca). Use para suplemento/ingrediente sem foto boa.
  cutout    PNG com transparencia (saida do fetch_image.py cutout)
  multiply  foto com fundo BRANCO — o branco some no creme (packshot de produto)
  photo     foto comum, enquadrada com cantos arredondados
Imagem ausente/ilegivel -> o slide sai so com o rotulo em destaque. Nunca quebra.
"""
import base64, json, mimetypes, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

W, H = 1080, 1350


def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def nl(t):
    return esc(t).replace("\n", "<br>")


def data_uri(path, base):
    if not path: return None
    p = Path(path)
    if not p.is_absolute():
        # tenta: cwd, pasta do JSON, raiz do repo (JSON fica em content/approved/)
        for b in (Path.cwd(), base, base.parent.parent):
            if (b / path).exists(): p = b / path; break
    if not p.exists(): return None
    mime = mimetypes.guess_type(str(p))[0] or "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@400;500;600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px}
body{background:VAR_BG;color:VAR_INK;font-family:Lora,Georgia,'Times New Roman',serif;
 -webkit-font-smoothing:antialiased;position:relative;overflow:hidden}
.wrap{position:absolute;inset:0;padding:96px 64px 150px;display:flex;flex-direction:column;
 align-items:center;justify-content:center;text-align:center;gap:calc(64px*var(--k,1))}
.hl{font-weight:700;font-size:calc(var(--hs)*var(--k,1));line-height:1.13;letter-spacing:-.012em;max-width:940px}
.items{display:flex;justify-content:center;align-items:flex-end;gap:36px;width:100%}
.item{display:flex;flex-direction:column;align-items:center;gap:30px;flex:1;min-width:0}
.item.pot{flex:0 0 330px}
.box{width:100%;height:calc(var(--bh)*var(--k,1));display:flex;align-items:center;justify-content:center}
.box img{max-width:100%;max-height:100%;object-fit:contain}
.cutout img{filter:drop-shadow(0 22px 22px rgba(40,30,15,.20))}
.multiply img{mix-blend-mode:multiply}
.photo .box{border-radius:28px;overflow:hidden;box-shadow:0 18px 40px rgba(40,30,15,.16)}
.photo .box img{width:100%;height:100%;max-width:none;max-height:none;object-fit:cover}
.noimg .box{border:3px solid VAR_INK;border-radius:28px;font-size:54px;font-weight:700;padding:30px;line-height:1.15}
.lb{font-size:calc(40px*var(--k,1));font-weight:500;line-height:1.2}
.sub{font-family:Inter,Arial,sans-serif;font-size:calc(26px*var(--k,1));font-weight:500;color:VAR_INK2;margin-top:-14px}
.vs{font-style:italic;font-size:54px;color:VAR_INK2;align-self:center;flex:0 0 auto;padding-bottom:70px}
.tag{font-style:italic;font-weight:400;font-size:calc(48px*var(--k,1));line-height:1.3;max-width:920px}
.swipe{font-family:Inter,Arial,sans-serif;font-size:26px;font-weight:600;letter-spacing:.16em;
 text-transform:uppercase;color:VAR_INK2}
.fact{align-items:flex-start;text-align:left;padding:110px 84px 160px;gap:calc(40px*var(--k,1))}
.kicker{font-family:Inter,Arial,sans-serif;font-size:25px;font-weight:700;letter-spacing:.18em;
 text-transform:uppercase;color:VAR_ACCENT}
.fact .hl{font-size:calc(82px*var(--k,1));max-width:none}
.rule{width:96px;height:6px;background:VAR_ACCENT;border-radius:4px}
.body{font-family:Inter,Arial,sans-serif;font-size:calc(42px*var(--k,1));line-height:1.48;font-weight:400;color:VAR_INK}
.body p{margin-bottom:calc(22px*var(--k,1))} .body p:last-child{margin-bottom:0}
.body b{font-weight:700}
.src{font-family:Inter,Arial,sans-serif;font-size:calc(25px*var(--k,1));line-height:1.45;color:VAR_INK2}
.cta{font-style:italic;font-size:calc(50px*var(--k,1));line-height:1.3}
.handle{position:absolute;right:70px;bottom:62px;font-style:italic;font-size:32px}
.num{position:absolute;left:70px;bottom:66px;font-family:Inter,Arial,sans-serif;font-size:24px;
 font-weight:600;letter-spacing:.1em;color:VAR_INK2;opacity:.75}
"""


def pot_svg(name, sub=""):
    """Pote generico de suplemento (desenho proprio, sem marca). Rotulo lima SFN."""
    name = esc((name or "").upper()); sub = esc(sub or "")
    lines = name.split(" ") if len(name) > 11 and " " in name else [name]
    longest = max(len(l) for l in lines)
    fs = min(46, int(228 / max(longest, 1) / 0.66))
    if len(lines) == 1:
        txt = f'<text x="150" y="{232 if sub else 240}" font-size="{fs}">{lines[0]}</text>'
    else:
        txt = (f'<text x="150" y="{214 if sub else 222}" font-size="{fs}">{lines[0]}</text>'
               f'<text x="150" y="{214 + fs if sub else 222 + fs}" font-size="{fs}">{" ".join(lines[1:])}</text>')
    subt = f'<text x="150" y="{278 if len(lines)==1 else 290}" class="s">{sub}</text>' if sub else ""
    return f"""<svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg" style="height:100%;width:auto;filter:drop-shadow(0 22px 20px rgba(40,30,15,.22))">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".22" stop-color="#fff" stop-opacity=".03"/><stop offset=".8" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>
<style>text{{font-family:Inter,Arial,sans-serif;font-weight:800;fill:#0A0A0A;text-anchor:middle;letter-spacing:-.5px}}.s{{font-size:19px;font-weight:600;letter-spacing:.6px}}</style></defs>
<rect x="34" y="8" width="232" height="70" rx="14" fill="#151513"/>
<g stroke="#2c2c28" stroke-width="3">{''.join(f'<line x1="{x}" y1="18" x2="{x}" y2="68"/>' for x in range(52, 260, 14))}</g>
<rect x="24" y="70" width="252" height="322" rx="26" fill="#1F1E1B"/>
<rect x="24" y="150" width="252" height="170" fill="#D4FF00"/>
<rect x="24" y="150" width="252" height="10" fill="#0A0A0A" opacity=".12"/>
{txt}{subt}
<rect x="24" y="70" width="252" height="322" rx="26" fill="url(#g)"/>
</svg>"""


def item_html(it, base):
    if it.get("pot"):
        lb = f'<div class="lb">{nl(it.get("label"))}</div>' if it.get("label") else ""
        sub = f'<div class="sub">{nl(it.get("sub"))}</div>' if it.get("sub") else ""
        return f'<div class="item pot"><div class="box">{pot_svg(it["pot"], it.get("pot_sub"))}</div>{lb}{sub}</div>'
    uri = data_uri(it.get("image"), base)
    mode = it.get("mode", "photo") if uri else "noimg"
    inner = f'<img src="{uri}">' if uri else esc(it.get("label", ""))
    lb = f'<div class="lb">{nl(it.get("label"))}</div>' if (it.get("label") and uri) else ""
    sub = f'<div class="sub">{nl(it.get("sub"))}</div>' if it.get("sub") else ""
    return f'<div class="item {mode}"><div class="box">{inner}</div>{lb}{sub}</div>'


def build(slide, d, num, user, base):
    t = slide.get("type", "pair")
    items = slide.get("items") or []
    hs = {"cover": 118, "pair": 92, "single": 92, "versus": 92}.get(t, 92)
    bh = 600 if (t == "single" or len(items) == 1) else 470
    if t == "fact":
        c = ""
        if slide.get("label"):    c += f'<div class="kicker">{esc(slide["label"])}</div>'
        if slide.get("headline"): c += f'<div class="hl">{nl(slide["headline"])}</div>'
        c += '<div class="rule"></div>'
        if slide.get("body"):
            ps = "".join(f"<p>{nl(p)}</p>" for p in slide["body"].split("\n\n") if p.strip())
            c += f'<div class="body">{ps}</div>'
        if slide.get("source"):   c += f'<div class="src">{nl(slide["source"])}</div>'
        if slide.get("cta"):      c += f'<div class="cta">{nl(slide["cta"])}</div>'
        wrap_cls = "wrap fact"
    else:
        c = ""
        if slide.get("headline"): c += f'<div class="hl">{nl(slide["headline"])}</div>'
        if items:
            parts = [item_html(i, base) for i in items[:2]]
            if t == "versus" and len(parts) == 2:
                parts.insert(1, '<div class="vs">vs</div>')
            c += f'<div class="items">{"".join(parts)}</div>'
        if slide.get("tagline"):  c += f'<div class="tag">{nl(slide["tagline"])}</div>'
        if t == "cover":          c += '<div class="swipe">arrasta →</div>'
        wrap_cls = "wrap"
    css = (CSS.replace("VAR_BG", d.get("bg", "#F1ECE4")).replace("VAR_INK2", d.get("ink2", "#6B665C"))
              .replace("VAR_INK", d.get("text_color", "#1F1E1B")).replace("VAR_ACCENT", d.get("accent", "#4F6B2A")))
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head>'
            f'<body style="--hs:{hs}px;--bh:{bh}px"><div class="{wrap_cls}"><div class="fit" style="display:contents">{c}</div></div>'
            f'<div class="num">{num}</div><div class="handle">{esc(user)}</div></body></html>')


def _face_report(paths):
    """Roda a deteccao de rosto nas fotos usadas e devolve o registro para o JSON."""
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from face_check import count_faces
    except Exception:
        return {"checked": 0, "unverified": [str(p) for p in paths], "with_faces": []}
    rep = {"checked": 0, "unverified": [], "with_faces": []}
    for p in paths:
        n = count_faces(p)
        if n is None: rep["unverified"].append(str(p))
        else:
            rep["checked"] += 1
            if n: rep["with_faces"].append({"file": str(p), "faces": n})
    return rep


FIT_JS = """() => {
  const w = document.querySelector('.wrap');
  let k = 1;
  const over = () => {
    const cs = getComputedStyle(w);
    const avail = w.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
    let h = 0; const kids = [...w.querySelectorAll('.fit > *')];
    if (!kids.length) return false;
    const top = Math.min(...kids.map(e => e.getBoundingClientRect().top));
    const bot = Math.max(...kids.map(e => e.getBoundingClientRect().bottom));
    h = bot - top;
    return h > avail + 1;
  };
  while (over() && k > 0.62) { k -= 0.03; document.body.style.setProperty('--k', k.toFixed(2)); }
  return {k: +k.toFixed(2), overflow: over()};
}"""


def render(src_path, out_dir):
    src_path = Path(src_path)
    post = json.load(open(src_path))
    d, user = post.get("design", {}), post.get("username", "@sofatosnutricao")
    slides = post["slides"]; n = len(slides)
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    base = src_path.parent
    pngs, warns = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page(viewport={"width": W, "height": H})
        for i, s in enumerate(slides):
            for it in (s.get("items") or []):
                if it.get("image") and not data_uri(it["image"], base):
                    warns.append(f"slide {i+1}: imagem nao encontrada ({it['image']}) — saiu so com rotulo")
            page.set_content(build(s, d, f"{i+1}/{n}", user, base), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(400)
            fit = page.evaluate(FIT_JS)
            if fit["overflow"]:
                warns.append(f"slide {i+1}: texto NAO coube mesmo reduzido — encurte o texto")
            elif fit["k"] < 0.85:
                warns.append(f"slide {i+1}: texto reduzido para {int(fit['k']*100)}% — considere encurtar")
            png = out_dir / f"slide_{i+1:02d}.png"
            page.screenshot(path=str(png))
            pngs.append(str(png)); print(f"  ok {png.name} (escala {fit['k']})")
        browser.close()
    used = []
    for s in slides:
        for it in (s.get("items") or []):
            if it.get("image"):
                pth = Path(it["image"])
                if not pth.is_absolute():
                    for bdir in (Path.cwd(), base, base.parent.parent):
                        if (bdir / it["image"]).exists(): pth = bdir / it["image"]; break
                if pth.exists(): used.append(pth)
    post["face_check"] = _face_report(used)
    for f in post["face_check"]["with_faces"]:
        warns.append(f"ROSTO detectado em {f['file']} ({f['faces']}) — troque a foto; o quality gate vai reprovar")
    post["creative_files"] = pngs
    post["status"] = "rendered"
    json.dump(post, open(src_path, "w"), indent=2, ensure_ascii=False)
    for w in warns: print("AVISO:", w)
    print(f"-> {len(pngs)} slides em {out_dir}")
    return pngs


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 render_provocativo.py <post.json> <out_dir>"); sys.exit(1)
    render(sys.argv[1], sys.argv[2])
