"""
render_carousel.py — Gera slides PNG 1080x1350 a partir de um draft JSON.
HTML/CSS -> PNG via Puppeteer (Chrome headless).
"""
import json, sys, re, subprocess, os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import DIRS

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

TPL = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
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

NODE = """
const puppeteer=require('puppeteer'),fs=require('fs'),path=require('path');
(async()=>{
 const slides=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
 const out=process.argv[3];
 const b=await puppeteer.launch({headless:'new',args:['--no-sandbox']});
 const pg=await b.newPage();
 await pg.setViewport({width:1080,height:1350,deviceScaleFactor:2});
 for(let i=0;i<slides.length;i++){
  await pg.setContent(slides[i],{waitUntil:'networkidle0'});
  await new Promise(r=>setTimeout(r,400));
  const p=path.join(out,`slide_${String(i+1).padStart(2,'0')}.png`);
  await pg.screenshot({path:p});
  console.log('ok '+path.basename(p));
 }
 await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
"""

def render(src):
    post = json.load(open(src))
    lid  = post["local_id"]
    out  = DIRS["content"]/"drafts"/lid
    out.mkdir(parents=True, exist_ok=True)
    d, user = post.get("design",{}), post.get("username","")
    slides = post["slides"]; n=len(slides)
    htmls = [build(s,d,f"{i+1}/{n}",user,round((i+1)/n*100)) for i,s in enumerate(slides)]
    tmp = out/"_slides.json"; tmp.write_text(json.dumps(htmls))
    js = DIRS["scripts"]/"_render.js"; js.write_text(NODE)
    r = subprocess.run(["node",str(js),str(tmp),str(out)],capture_output=True,text=True,
        cwd=str(DIRS["scripts"]),env={**os.environ,"NODE_PATH":str(DIRS["scripts"]/"node_modules")})
    if r.returncode!=0:
        print("ERRO:",r.stderr[:400]); return []
    print(r.stdout.strip())
    tmp.unlink(missing_ok=True)
    pngs=sorted(str(p) for p in out.glob("slide_*.png"))
    pass
    # grava creative_files de volta no draft
    post["creative_files"]=pngs
    json.dump(post,open(src,"w"),indent=2,ensure_ascii=False)
    print(f"  -> {len(pngs)} slides em {out}")
    return pngs

if __name__=="__main__":
    for a in sys.argv[1:]: render(a)
