"""
render_didyouknow.py — Gera UM card estatico "Você sabia?" 1080x1350 (Playwright).
Formato leve e succinto para Instagram (sem carrossel, sem capa, sem Ghost).
Paleta INVERTIDA em relacao ao carrossel: fundo lima, texto preto.
Uso: python render_didyouknow.py <draft.json> <output_dir>
Campos usados do JSON: hook (fato principal), subtext (1 linha), source_line,
design{bg,text_color,ink2,padding}, username.
Escreve creative_files=[<card.png>] e status="rendered" de volta no JSON.
"""
import json, sys, re
from pathlib import Path
from playwright.sync_api import sync_playwright

W, H = 1080, 1350

def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def hl_numbers(s):
    # destaca numeros + unidades (ignora digitos colados a letras, ex.: SGLT1, GLUT5)
    return re.sub(
        r'(?<![A-Za-z])(~?\d+[\d.,:–\-]*\s?(?:g/h(?:ora)?|g/min|kcal|g|mg/kg|mg|%|min|h|horas|minutos|x)?)',
        r'<b>\1</b>', s)

TPL = """<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px}}
body{{background:{page};color:{ink};font-family:Inter,'Helvetica Neue',Arial,sans-serif;
 -webkit-font-smoothing:antialiased;position:relative;overflow:hidden}}
.glow{{position:absolute;width:1000px;height:1000px;border-radius:50%;
 background:radial-gradient(circle,{ink}14 0%,transparent 66%);top:-360px;right:-320px}}
.qmark{{position:absolute;right:-30px;bottom:-150px;font-size:660px;font-weight:900;
 line-height:1;color:{ink};opacity:.07;font-family:Inter,Arial,sans-serif}}
.wrap{{position:absolute;inset:0;padding:{pad}px {pad}px 150px;display:flex;
 flex-direction:column;justify-content:center}}
.badge{{display:inline-block;align-self:flex-start;background:{ink};color:{page};
 font-size:26px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
 padding:16px 30px;border-radius:999px;margin-bottom:48px}}
.fact{{font-size:{fsize}px;font-weight:800;line-height:1.14;letter-spacing:-.028em;
 max-width:920px}}
.fact b{{background:{ink};color:{page};font-weight:900;border-radius:8px;
 padding:0 .14em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.rule{{width:96px;height:6px;background:{ink2};border-radius:4px;margin:44px 0 34px}}
.sub{{font-size:38px;font-weight:500;line-height:1.5;letter-spacing:-.006em;
 color:{ink};opacity:.82;max-width:880px}}
.sub b{{color:{ink2};font-weight:800;opacity:1}}
.src{{position:absolute;left:{pad}px;bottom:118px;font-size:23px;font-weight:600;
 line-height:1.4;color:{ink};opacity:.55;max-width:920px}}
.foot{{position:absolute;left:{pad}px;bottom:60px;font-size:25px;font-weight:800;
 letter-spacing:.03em;color:{ink};opacity:.9}}
.bar{{position:absolute;left:0;bottom:0;height:8px;width:100%;background:{ink};opacity:.9}}
</style></head><body>
<div class="glow"></div><div class="qmark">?</div>
<div class="wrap">
  <div class="badge">Você sabia?</div>
  <div class="fact">{fact}</div>
  {rule}
  {sub}
</div>
{src}
<div class="foot">{user}</div>
<div class="bar"></div>
</body></html>"""

def render(src_path, out_dir):
    post = json.load(open(src_path))
    d = post.get("design", {})
    page = d.get("bg", "#D4FF00")          # fundo lima
    ink  = d.get("text_color", "#0A0A0A")  # texto preto
    ink2 = d.get("ink2", "#2E4B00")        # segunda tonalidade escura (verde profundo)
    user = post.get("username", "@sofatosnutricao")
    fact = hl_numbers(esc(post.get("hook", "")))
    sub_raw = post.get("subtext")
    sub = f'<div class="sub">{hl_numbers(esc(sub_raw))}</div>' if sub_raw else ""
    rule = '<div class="rule"></div>' if sub_raw else ""
    src_line = post.get("source_line")
    src = f'<div class="src">Fonte: {esc(src_line)}</div>' if src_line else ""
    n = len(post.get("hook", ""))
    fsize = 76 if n <= 90 else (66 if n <= 130 else 58)

    html = TPL.format(W=W, H=H, page=page, ink=ink, ink2=ink2, pad=d.get("padding", 80),
                      fsize=fsize, fact=fact, rule=rule, sub=sub, src=src, user=esc(user))

    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    card = out_dir / "card.png"
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = b.new_page()
        pg.set_viewport_size({"width": W, "height": H})
        pg.set_content(html, wait_until="networkidle")
        pg.wait_for_timeout(500)
        pg.screenshot(path=str(card))
        b.close()
    print(f"  ok card.png")

    post["creative_files"] = [str(card)]
    post["status"] = "rendered"
    json.dump(post, open(src_path, "w"), indent=2, ensure_ascii=False)
    print(f"-> card em {out_dir}")
    return [str(card)]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python render_didyouknow.py <draft.json> <output_dir>"); sys.exit(1)
    render(sys.argv[1], sys.argv[2])
