"""
fetch_image.py — Busca fotos de LICENCA LIVRE para os carrosseis SFN.

So aceita licencas que permitem uso comercial e adaptacao sem "share-alike":
  cc0 (dominio publico), pdm (public domain mark), by (atribuicao).
Nunca usa by-sa, by-nc, by-nd.

Provedores (--provider):
  stock    (padrao, roda na NUVEM) bancos CC0 de qualidade de stock via Openverse:
           StockSnap, rawpixel, WordPress Photos, nappy; completa com Flickr.
           Bom para comida, objetos, cenas de esporte, carro generico.
  flickr   (NUVEM) so Flickr — amador, use como ultimo recurso.
  commons  (roda no MAC via device_bash; a nuvem leva 429) Wikimedia Commons.
           Bom para coisa ESPECIFICA: modelo de carro, objeto com nome proprio.

Uso:
  python3 fetch_image.py search "<termo em ingles>" <out_dir> [--n 8] [--provider stock]
      Baixa ate N candidatas em <out_dir>/cand_XX.jpg, grava candidates.json
      (titulo, autor, licenca, URL de origem) e monta sheet.jpg — uma folha de
      contato numerada para o agente olhar UMA vez com a ferramenta Read.

  python3 fetch_image.py cutout <entrada> <saida.png>
      Recorta o fundo (rembg) e apara as margens. Use para objetos/produtos que
      vao sobre o fundo creme do formato provocativo. Sempre confira o PNG com
      Read: recorte ruim -> use a foto original em modo "photo".

Regras (nao negocie):
  - Toda imagem usada vai para "image_credits" no JSON do post (rastreabilidade).
  - Licenca "by" exige credito na legenda: "Fotos: Autor (CC BY), ...".
  - Nunca use foto com rosto identificavel (o script marca "ROSTO" nas candidatas
    com rosto de frente detectado; silhueta, costas e borrao podem). O detector
    nao pega tudo: confira no olho tambem.
  - Descarte no olho: anuncio/revista escaneada, print de tela, foto com marca
    d'agua ou com logotipo dominante — "CC BY" no Flickr nao garante que quem
    subiu era o dono. Na duvida, nao use.
  - Falhou a busca? Publique o slide sem foto. Foto nunca bloqueia publicacao.
"""
import io, json, re, sys, time, argparse, urllib.parse, urllib.request
from pathlib import Path

UA = "SFN-content-agent/1.0 (+https://www.instagram.com/sofatosnutricao)"
API = "https://api.openverse.org/v1/images/"
OK_LICENSES = {"cc0", "pdm", "by"}


def _get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _faces(path):
    """Conta rostos (ver face_check.py). None = nao foi possivel verificar."""
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from face_check import count_faces
        return count_faces(path)
    except Exception:
        return None


def _openverse(term, sources=None):
    q = {"q": term, "license": ",".join(sorted(OK_LICENSES)), "page_size": 20, "mature": "false"}
    if sources: q["source"] = sources
    data = json.loads(_get(f"{API}?{urllib.parse.urlencode(q)}"))
    out = []
    for r in data.get("results", []):
        if r.get("license") not in OK_LICENSES: continue
        lic = r["license"].upper() + (f" {r.get('license_version')}" if r.get("license_version") else "")
        out.append({"url": r["url"], "title": r.get("title"), "creator": r.get("creator") or "autor desconhecido",
                    "license": ("CC " + lic) if r["license"] == "by" else lic, "license_url": r.get("license_url"),
                    "source_url": r.get("foreign_landing_url"), "provider": r.get("source"), "w": r.get("width") or 0})
    return out


def _commons(term):
    """Wikimedia Commons. So responde a partir do Mac (device_bash) — a nuvem leva 429."""
    q = {"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
         "gsrsearch": f"{term} filetype:bitmap", "gsrlimit": 40, "prop": "imageinfo",
         "iiprop": "url|extmetadata|size", "iiurlwidth": 1600}
    data = json.loads(_get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(q)))
    pages = sorted((data.get("query") or {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata") or {}
        lic = (m.get("LicenseShortName") or {}).get("value", "")
        l = lic.lower().replace("-", " ")
        free = l.startswith("cc0") or l.startswith("public domain") or l == "pd" or (l.startswith("cc by ") and "sa" not in l and "nc" not in l and "nd" not in l)
        if not free: continue
        artist = re.sub(r"<[^>]+>", "", (m.get("Artist") or {}).get("value", "")).strip() or "autor desconhecido"
        out.append({"url": ii.get("thumburl") or ii.get("url"), "title": p.get("title", "").replace("File:", ""),
                    "creator": artist[:80], "license": lic, "license_url": (m.get("LicenseUrl") or {}).get("value"),
                    "source_url": ii.get("descriptionurl"), "provider": "wikimedia", "w": ii.get("thumbwidth") or ii.get("width") or 0})
    return out


def search(term, out_dir, n=8, min_width=700, provider="stock"):
    """provider: stock (bancos CC0: stocksnap/rawpixel/wordpress/nappy, completa com flickr),
    flickr (so flickr), commons (Wikimedia — rode no Mac)."""
    from PIL import Image, ImageDraw, ImageFont
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    found = []
    try:
        if provider == "commons":
            found = _commons(term)
        elif provider == "flickr":
            found = _openverse(term, "flickr")
        else:
            found = _openverse(term, "stocksnap,rawpixel,wordpress,nappy")
            if len(found) < n:
                time.sleep(0.4); found += _openverse(term, "flickr")
    except Exception as e:
        print(f"FALHA na busca ({e}). Siga sem foto neste slide.")
        if not found:
            json.dump([], open(out / "candidates.json", "w")); return []

    cands = []
    for r in found:
        if len(cands) >= n: break
        idx = len(cands) + 1
        dst = out / f"cand_{idx:02d}.jpg"
        try:
            raw = _get(r["url"])
            im = Image.open(io.BytesIO(raw)); im.load()
            if im.mode not in ("RGB", "RGBA"): im = im.convert("RGBA" if "A" in im.mode else "RGB")
            if im.mode == "RGBA":
                bg = Image.new("RGB", im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[3]); im = bg
            if im.width < min_width: continue
            im.thumbnail((1400, 1400))   # leve: as candidatas do Mac ficam na pasta do Victor
            im.save(dst, "JPEG", quality=86)
        except Exception as e:
            print(f"  pulei '{r.get('title')}' ({type(e).__name__})"); continue
        nf = _faces(dst)
        cands.append({"n": idx, "file": str(dst), "title": r["title"], "creator": r["creator"],
                      "license": r["license"], "license_url": r["license_url"], "source_url": r["source_url"],
                      "provider": r["provider"], "width": im.width, "height": im.height, "faces": nf})
        flag = f"  << ROSTO x{nf} — NAO USE" if nf else ("  (rosto: nao verificado)" if nf is None else "")
        print(f"  {idx:02d} {im.width}x{im.height} [{r['license']}] ({r['provider']}) {r['title']} — {r['creator']}{flag}")
        time.sleep(0.3)

    json.dump(cands, open(out / "candidates.json", "w"), indent=2, ensure_ascii=False)

    if cands:
        cell, cols = 420, 4
        rows = (len(cands) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * cell, rows * cell), (245, 245, 245))
        d = ImageDraw.Draw(sheet)
        try: font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
        except Exception: font = ImageFont.load_default()
        for i, c in enumerate(cands):
            t = Image.open(c["file"]); t.thumbnail((cell - 16, cell - 16))
            x = (i % cols) * cell + (cell - t.width) // 2
            y = (i // cols) * cell + (cell - t.height) // 2
            sheet.paste(t, (x, y))
            bx, by = (i % cols) * cell + 10, (i // cols) * cell + 10
            d.rectangle([bx, by, bx + 74, by + 58], fill=(10, 10, 10))
            d.text((bx + 10, by + 4), f"{c['n']:02d}", fill=(212, 255, 0), font=font)
            if c.get("faces"):
                d.rectangle([bx + 84, by, bx + 84 + 300, by + 58], fill=(200, 20, 20))
                d.text((bx + 94, by + 4), "ROSTO: NÃO", fill=(255, 255, 255), font=font)
        sheet.save(out / "sheet.jpg", "JPEG", quality=85)
        print(f"-> {len(cands)} candidatas. Olhe {out/'sheet.jpg'} com Read e escolha pelo numero.")
        if any(c.get("faces") for c in cands):
            print("   Marcadas com ROSTO tem rosto de frente detectado: NAO use (regra do playbook).")
        if any(c.get("faces") is None for c in cands):
            print("   Deteccao de rosto indisponivel aqui: confira no olho e descarte rosto identificavel.")
    else:
        print("-> nenhuma candidata com licenca livre. Tente outro termo (em ingles) ou siga sem foto.")
    return cands


def cutout(src, dst):
    from PIL import Image
    from rembg import remove, new_session
    # isnet-general-use: licenca Apache-2.0, ~170 MB. NAO troque pelo modelo padrao
    # do rembg (bria-rmbg: 1 GB e licenca nao-comercial).
    im = Image.open(src).convert("RGBA")
    im.thumbnail((1600, 1600))
    out = remove(im, session=new_session("isnet-general-use"))
    r, g, b, a = out.split()
    hist = a.histogram()
    solid, ghost = sum(hist[200:]), sum(hist[24:200])
    a = a.point(lambda v: 0 if v < 56 else v)          # limpa a franja fantasma
    out = Image.merge("RGBA", (r, g, b, a))
    bbox = a.getbbox()
    if bbox: out = out.crop(bbox)
    out.thumbnail((1000, 1000))
    cover = (sum(out.split()[3].histogram()[129:]) / (out.width * out.height)) if bbox else 0.0
    dirty = ghost / max(solid, 1)
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    out.save(dst, "PNG")
    print(f"-> {dst} {out.width}x{out.height} (objeto ocupa {cover:.0%} do recorte)")
    if cover < 0.15:
        print("AVISO: recorte quase vazio — provavelmente falhou. Use a foto original (modo photo).")
    if dirty > 0.18:
        print(f"AVISO: recorte sujo ({dirty:.0%} de pixels semitransparentes) — o fundo vazou. "
              "Confira com Read; se estiver ruim, use outra foto ou o modo photo.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("term"); s.add_argument("out_dir")
    s.add_argument("--n", type=int, default=8); s.add_argument("--min-width", type=int, default=700)
    s.add_argument("--provider", choices=["stock", "flickr", "commons"], default="stock")
    c = sub.add_parser("cutout"); c.add_argument("src"); c.add_argument("dst")
    a = ap.parse_args()
    if a.cmd == "search": search(a.term, a.out_dir, a.n, a.min_width, a.provider)
    else: cutout(a.src, a.dst)
