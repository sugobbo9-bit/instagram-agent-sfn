"""
render_playwright.py — Gera slides PNG 1080x1350 usando Playwright (cloud container).
Replica o mesmo HTML do render_carousel.py original.
"""
import json, sys, re, os
from pathlib import Path
from playwright.sync_api import sync_playwright

W, H = 1080, 1350

def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

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

# Font embedded as base64 alternative: use system fallback since we may not reach Google Fonts
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
.hl{{font-size:{hsize}px;font-weight:800;line-height:1.09;letter-spacing:-.028em;
 margin-bottom:{hmb}px;max-width:900px}}
.rule{{width:96px;height:6px;background:{accent};border-radius:4px;margin:0 0 40px}}
.body{{font-size:40px;font-weight:400;line-height:1.52;letter-spacing:-.008em;
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
</style></head><body><div class="glow"></div>
<div class="wrap">{content}</div>
<div class="foot">{user}</div><div class="num">{num}</div><div class="bar"></div>
</body></html>"""

def build(slide, d, num, user, prog):
    t = slide.get("type","")
    c = ""
    if slide.get("label"):    c += f'<div class="label">{esc(slide["label"])}</div>'
    if slide.get("headline"): c += f'<div class="hl">{esc(slide["headline"])}</div>'
    if slide.get("divider"):  c += '<div class="rule"></div>'
    if slide.get("body"):     c += f'<div class="body">{fmt_body(slide["body"])}</div>'
    return TPL.format(W=W,H=H,bg=d.get("bg","#0A0A0A"),fg=d.get("text_color","#F5F5F0"),
        accent=d.get("accent","#D4FF00"),pad=d.get("padding",84),
        hsize=92 if t=="hook" else (74 if t=="cta" else 62),
        hmb=0 if (t=="hook" and not slide.get("body")) else 34,
        content=c,user=esc(user),num=num,prog=prog)

def build_cover(post, d):
    """Gera HTML para a capa do artigo 1200x630."""
    hook = esc(post.get("hook",""))
    topic = esc(post.get("topic","").upper())
    user = esc(post.get("username",""))
    accent = d.get("accent","#D4FF00")
    bg = d.get("bg","#0A0A0A")
    fg = d.get("text_color","#F5F5F0")
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
<div class="glow"></div>
<div class="wrap">
  <div class="tag">{topic}</div>
  <div class="hl">{hook}</div>
</div>
<div class="foot">{user}</div>
<div class="bar"></div>
</body></html>"""

def render_draft(src_path, out_dir):
    post = json.load(open(src_path))
    lid  = post["local_id"]
    d    = post.get("design", {})
    user = post.get("username", "")
    slides = post["slides"]
    n = len(slides)

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    htmls = [build(s, d, f"{i+1}/{n}", user, round((i+1)/n*100)) for i, s in enumerate(slides)]
    cover_html = build_cover(post, d)

    pngs = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()

        # Render slides 1080x1350
        page.set_viewport_size({"width": W, "height": H})
        for i, html in enumerate(htmls):
            page.set_content(html, wait_until="networkidle")
            page.wait_for_timeout(500)
            png_path = out_dir / f"slide_{str(i+1).zfill(2)}.png"
            page.screenshot(path=str(png_path))
            pngs.append(str(png_path))
            print(f"  ok slide_{str(i+1).zfill(2)}.png")

        # Render cover 1200x630
        page.set_viewport_size({"width": 1200, "height": 630})
        page.set_content(cover_html, wait_until="networkidle")
        page.wait_for_timeout(400)
        cover_path = out_dir / "cover.png"
        page.screenshot(path=str(cover_path))
        print(f"  ok cover.png")

        browser.close()

    # Update draft JSON with creative_files
    post["creative_files"] = pngs
    post["status"] = "rendered"
    json.dump(post, open(src_path, "w"), indent=2, ensure_ascii=False)
    print(f"-> {len(pngs)} slides em {out_dir}")
    return pngs

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python render_playwright.py <draft.json> <output_dir>")
        sys.exit(1)
    render_draft(sys.argv[1], sys.argv[2])
