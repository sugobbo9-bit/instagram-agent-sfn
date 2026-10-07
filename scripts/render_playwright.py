"""
render_playwright.py — Gera slides PNG 1080x1350 usando Playwright (cloud container).

Carrossel tecnico SFN (preto + lima). Desde 2026-10-06 aceita FOTO:

  slide["image"] = "caminho/da/foto.jpg"            (ou {"path": "...", "focus": "center 30%"})

  - no slide type "hook": a foto vira fundo da capa (escurecida), headline embaixo,
    "kicker" opcional em etiqueta lima no topo (ex.: "MITO", "O ERRO", "TESTE").
  - nos demais: a foto vira uma faixa no topo do slide e o texto desce.
  - sem "image": o slide sai exatamente como antes (so texto).

Foto ausente/ilegivel nunca quebra o render — o slide sai so com texto.
O texto se auto-ajusta: se nao couber, a fonte encolhe ate 70% e o script avisa.
"""
import base64, json, mimetypes, sys, re, os
from pathlib import Path
from playwright.sync_api import sync_playwright

W, H = 1080, 1350

def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def data_uri(img, base):
    if not img: return None, None
    path, focus = (img.get("path"), img.get("focus", "center")) if isinstance(img, dict) else (img, "center")
    if not path: return None, None
    p = Path(path)
    if not p.is_absolute():
        for b in (Path.cwd(), base, base.parent.parent):
            if (b / path).exists(): p = b / path; break
    if not p.exists(): return None, None
    mime = mimetypes.guess_type(str(p))[0] or "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode(), focus

def fmt_body(text):
    if not text: return ""
    out = []
    for ln in text.split("\n"):
        s = ln.strip()
        if not s:
            out.append('<div class="sp"></div>'); continue
        bullet = None
        if s.startswith("•"): bullet, s = "•", s[1:].strip()
        elif s.startswith("→"): bullet, s = "→", s[1:].strip()
        s = esc(s)
        s = re.sub(r'(\d+[\d.,:–\-]*\s?(?:g/h(?:ora)?|g|mg/kg|%|min|h|horas|minutos)?\b)', r'<b>\1</b>', s)
        if bullet:
            out.append(f'<div class="li"><span class="bl">{bullet}</span><span>{s}</span></div>')
        else:
            out.append(f'<div class="p">{s}</div>')
    return "".join(out)

TPL = """<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px}}
body{{background:{bg};color:{fg};font-family:Inter,'Helvetica Neue',Arial,sans-serif;
 -webkit-font-smoothing:antialiased;position:relative;overflow:hidden}}
.wrap{{position:absolute;inset:0;padding:{pad}px {pad}px 150px;display:flex;
 flex-direction:column;justify-content:center}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;
 background:radial-gradient(circle,{accent}1F 0%,transparent 68%);top:-320px;right:-300px}}
.label{{font-size:23px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
 color:{accent};margin-bottom:30px}}
.hl{{font-size:calc({hsize}px*var(--k,1));font-weight:800;line-height:1.09;letter-spacing:-.028em;
 margin-bottom:{hmb}px;max-width:900px}}
.rule{{width:96px;height:6px;background:{accent};border-radius:4px;margin:0 0 40px}}
.body{{font-size:calc({bsize}px*var(--k,1));font-weight:400;line-height:1.52;letter-spacing:-.008em;
 opacity:.93;max-width:880px}}
.p{{margin-bottom:22px}} .p:last-child{{margin-bottom:0}} .sp{{height:14px}}
.li{{display:flex;gap:20px;margin-bottom:20px;align-items:baseline}}
.bl{{color:{accent};font-weight:700;flex-shrink:0}}
.body b{{font-weight:700;color:{accent}}}
.foot{{position:absolute;left:{pad}px;bottom:64px;font-size:24px;font-weight:600;
 letter-spacing:.04em;opacity:.42}}
.num{{position:absolute;right:{pad}px;bottom:64px;font-size:22px;font-weight:700;
 letter-spacing:.1em;opacity:.3}}
.bar{{position:absolute;left:0;bottom:0;height:8px;width:{prog}%;background:{accent};opacity:.85}}
/* --- foto de fundo (capa) --- */
.bgimg{{position:absolute;inset:0;background-size:cover;background-position:{focus};filter:saturate(.9) contrast(1.05)}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.38) 0%,rgba(10,10,10,.30) 30%,rgba(10,10,10,.86) 66%,rgba(10,10,10,.97) 100%)}}
.photo-hook .wrap{{justify-content:flex-end;padding-bottom:210px}}
.photo-hook .hl{{text-shadow:0 2px 24px rgba(0,0,0,.55)}}
.photo-hook .foot,.photo-hook .num{{opacity:.7}}
.kicker{{position:absolute;left:{pad}px;top:{pad}px;background:{accent};color:#0A0A0A;font-size:26px;
 font-weight:800;letter-spacing:.16em;text-transform:uppercase;padding:14px 22px;border-radius:8px}}
.swipe{{font-size:24px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{accent};margin-top:36px}}
/* --- faixa de foto no topo (miolo) --- */
.band{{position:absolute;left:0;top:0;width:100%;height:{bandh}px;background-size:cover;background-position:{focus};
 filter:saturate(.9) contrast(1.05)}}
.bandfade{{position:absolute;left:0;top:0;width:100%;height:{bandh}px;
 background:linear-gradient(180deg,rgba(10,10,10,.10) 0%,rgba(10,10,10,.25) 55%,{bg} 100%)}}
.photo-band .wrap{{padding-top:{bandpad}px;justify-content:center}}
</style></head><body class="{bodycls}">{under}
<div class="wrap">{content}</div>{over}
<div class="foot">{user}</div><div class="num">{num}</div><div class="bar"></div>
</body></html>"""

FIT_JS = """() => {
  const w = document.querySelector('.wrap'); let k = 1;
  const over = () => {
    const cs = getComputedStyle(w);
    const avail = w.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
    const kids = [...w.children]; if (!kids.length) return false;
    const top = Math.min(...kids.map(e => e.getBoundingClientRect().top));
    const bot = Math.max(...kids.map(e => e.getBoundingClientRect().bottom));
    return (bot - top) > avail + 1;
  };
  while (over() && k > 0.70) { k -= 0.03; document.body.style.setProperty('--k', k.toFixed(2)); }
  return {k: +k.toFixed(2), overflow: over()};
}"""

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


def build(slide, d, num, user, prog, base=Path(".")):
    t = slide.get("type","")
    uri, focus = data_uri(slide.get("image"), base)
    bodycls, under, over = "", '<div class="glow"></div>', ""
    bandh = 430
    c = ""
    if uri and t == "hook":
        bodycls = "photo-hook"
        under = f'<div class="bgimg" style="background-image:url({uri})"></div><div class="shade"></div>'
        if slide.get("kicker"): over = f'<div class="kicker">{esc(slide["kicker"])}</div>'
    elif uri:
        bodycls = "photo-band"
        under = f'<div class="band" style="background-image:url({uri})"></div><div class="bandfade"></div>'
    if slide.get("label"):    c += f'<div class="label">{esc(slide["label"])}</div>'
    if slide.get("headline"): c += f'<div class="hl">{esc(slide["headline"])}</div>'
    if slide.get("divider"):  c += '<div class="rule"></div>'
    if slide.get("body"):     c += f'<div class="body">{fmt_body(slide["body"])}</div>'
    if bodycls == "photo-hook": c += '<div class="swipe">arrasta →</div>'
    pad = d.get("padding",84)
    return TPL.format(W=W,H=H,bg=d.get("bg","#0A0A0A"),fg=d.get("text_color","#F5F5F0"),
        accent=d.get("accent","#D4FF00"),pad=pad,
        hsize=(96 if bodycls=="photo-hook" else 92) if t=="hook" else (74 if t=="cta" else (58 if bodycls else 62)),
        bsize=37 if bodycls=="photo-band" else 40,
        hmb=0 if (t=="hook" and not slide.get("body")) else 34,
        focus=focus or "center", bandh=bandh, bandpad=bandh+30,
        bodycls=bodycls, under=under, over=over,
        content=c,user=esc(user),num=num,prog=prog)

def build_cover(post, d, base=Path(".")):
    """Gera HTML para a capa do artigo 1200x630 (usa a foto do slide hook, se houver)."""
    hook = esc(post.get("hook",""))
    topic = esc(post.get("topic","").upper())
    user = esc(post.get("username",""))
    accent = d.get("accent","#D4FF00")
    bg = d.get("bg","#0A0A0A")
    fg = d.get("text_color","#F5F5F0")
    hook_slide = next((s for s in post.get("slides", []) if s.get("type") == "hook"), {})
    uri, focus = data_uri(hook_slide.get("image"), base)
    photo = (f'<div style="position:absolute;inset:0;background:url({uri}) {focus or "center"}/cover"></div>'
             f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,10,10,.94) 0%,rgba(10,10,10,.80) 55%,rgba(10,10,10,.35) 100%)"></div>'
             ) if uri else '<div class="glow"></div>'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1200px;height:630px;background:{bg};color:{fg};
 font-family:Inter,'Helvetica Neue',Arial,sans-serif;overflow:hidden;position:relative}}
.glow{{position:absolute;width:800px;height:800px;border-radius:50%;
 background:radial-gradient(circle,{accent}22 0%,transparent 68%);top:-300px;right:-200px}}
.wrap{{position:absolute;inset:0;padding:80px;display:flex;flex-direction:column;justify-content:center}}
.tag{{font-size:18px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{accent};margin-bottom:28px}}
.hl{{font-size:58px;font-weight:900;line-height:1.08;letter-spacing:-.03em;max-width:900px}}
.bar{{position:absolute;left:0;bottom:0;height:8px;width:100%;background:{accent};opacity:.7}}
.foot{{position:absolute;left:80px;bottom:32px;font-size:22px;font-weight:600;letter-spacing:.04em;opacity:.4}}
</style></head><body>
{photo}
<div class="wrap">
  <div class="tag">{topic}</div>
  <div class="hl">{hook}</div>
</div>
<div class="foot">{user}</div>
<div class="bar"></div>
</body></html>"""

def render_draft(src_path, out_dir):
    src_path = Path(src_path)
    post = json.load(open(src_path))
    lid  = post["local_id"]
    d    = post.get("design", {})
    user = post.get("username", "")
    slides = post["slides"]
    n = len(slides)
    base = src_path.parent

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    htmls = [build(s, d, f"{i+1}/{n}", user, round((i+1)/n*100), base) for i, s in enumerate(slides)]
    cover_html = build_cover(post, d, base)

    pngs, warns = [], []
    for i, s in enumerate(slides):
        if s.get("image") and not data_uri(s["image"], base)[0]:
            warns.append(f"slide {i+1}: foto nao encontrada ({s['image']}) — saiu so com texto")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()

        # Render slides 1080x1350
        page.set_viewport_size({"width": W, "height": H})
        for i, html in enumerate(htmls):
            page.set_content(html, wait_until="networkidle")
            page.wait_for_timeout(500)
            fit = page.evaluate(FIT_JS)
            if fit["overflow"]:
                warns.append(f"slide {i+1}: texto NAO coube mesmo a 70% — encurte o texto ou tire a foto")
            elif fit["k"] < 0.85:
                warns.append(f"slide {i+1}: texto reduzido para {int(fit['k']*100)}% — considere encurtar")
            png_path = out_dir / f"slide_{str(i+1).zfill(2)}.png"
            page.screenshot(path=str(png_path))
            pngs.append(str(png_path))
            print(f"  ok slide_{str(i+1).zfill(2)}.png (escala {fit['k']})")

        # Render cover 1200x630
        page.set_viewport_size({"width": 1200, "height": 630})
        page.set_content(cover_html, wait_until="networkidle")
        page.wait_for_timeout(400)
        cover_path = out_dir / "cover.png"
        page.screenshot(path=str(cover_path))
        print(f"  ok cover.png")

        browser.close()

    used = []
    for s in slides:
        im = s.get("image")
        pth = (im.get("path") if isinstance(im, dict) else im) if im else None
        if pth:
            pp = Path(pth)
            if not pp.is_absolute():
                for bdir in (Path.cwd(), base, base.parent.parent):
                    if (bdir / pth).exists(): pp = bdir / pth; break
            if pp.exists(): used.append(pp)
    post["face_check"] = _face_report(used)
    for f in post["face_check"]["with_faces"]:
        warns.append(f"ROSTO detectado em {f['file']} ({f['faces']}) — troque a foto; o quality gate vai reprovar")

    # Update draft JSON with creative_files
    post["creative_files"] = pngs
    post["status"] = "rendered"
    json.dump(post, open(src_path, "w"), indent=2, ensure_ascii=False)
    for w in warns: print("AVISO:", w)
    print(f"-> {len(pngs)} slides em {out_dir}")
    return pngs

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python render_playwright.py <draft.json> <output_dir>")
        sys.exit(1)
    render_draft(sys.argv[1], sys.argv[2])
