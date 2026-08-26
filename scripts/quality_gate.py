"""
quality_gate.py — Validação automática antes de qualquer publicação
Retorna True se aprovado, False + lista de falhas se reprovado.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import CAROUSEL_DIMENSIONS, REEL_DIMENSIONS


def check_carousel(post: dict) -> tuple[bool, list]:
    """Valida um rascunho de carrossel."""
    failures = []

    # CIENTÍFICO
    if not post.get("scientific_sources"):
        failures.append("CIENTÍFICO: nenhuma fonte científica listada")
    for src in post.get("scientific_sources", []):
        if not src.get("doi") and not src.get("url"):
            failures.append(f"CIENTÍFICO: fonte '{src.get('title', '?')}' sem DOI ou URL verificável")

    # EDITORIAL
    hook = post.get("hook", "").strip()
    if not hook:
        failures.append("EDITORIAL: hook vazio")
    elif len(hook) > 80:
        failures.append(f"EDITORIAL: hook muito longo ({len(hook)} chars, máx recomendado 80)")

    slides = post.get("slides", [])
    if len(slides) < 3:
        failures.append(f"EDITORIAL: carrossel com apenas {len(slides)} slides (mínimo 3)")
    if len(slides) > 12:
        failures.append(f"EDITORIAL: carrossel com {len(slides)} slides (máximo recomendado 10)")

    caption = post.get("caption", "").strip()
    if not caption:
        failures.append("EDITORIAL: legenda vazia")

    # CRIATIVO
    creative_files = post.get("creative_files", [])
    if not creative_files:
        failures.append("CRIATIVO: nenhum arquivo criativo gerado")
    for f in creative_files:
        p = Path(f)
        if not p.exists():
            failures.append(f"CRIATIVO: arquivo não encontrado: {f}")

    # ORIGINALIDADE
    if not post.get("post_id_is_unique", True):
        failures.append("ORIGINALIDADE: ID duplicado detectado")

    # PLATAFORMA
    if "watermark" in post.get("notes", "").lower():
        failures.append("PLATAFORMA: possível marca d'água de outra plataforma")

    return len(failures) == 0, failures


def check_reel(post: dict) -> tuple[bool, list]:
    """Valida um rascunho de Reel."""
    failures = []

    if not post.get("scientific_sources"):
        failures.append("CIENTÍFICO: nenhuma fonte listada")

    hook = post.get("hook", "").strip()
    if not hook:
        failures.append("EDITORIAL: hook vazio")

    video_file = post.get("video_file", "")
    if not video_file or not Path(video_file).exists():
        failures.append(f"TÉCNICO: arquivo de vídeo não encontrado: {video_file}")

    caption = post.get("caption", "").strip()
    if not caption:
        failures.append("EDITORIAL: legenda vazia")

    return len(failures) == 0, failures


def check_static(post: dict) -> tuple[bool, list]:
    """Valida um post estático."""
    failures = []

    if not post.get("creative_files"):
        failures.append("CRIATIVO: nenhum arquivo gerado")

    caption = post.get("caption", "").strip()
    if not caption:
        failures.append("EDITORIAL: legenda vazia")

    return len(failures) == 0, failures


def run_gate(post: dict) -> tuple[bool, list]:
    """Ponto de entrada principal."""
    fmt = post.get("format", "carousel")
    if fmt == "carousel":
        return check_carousel(post)
    elif fmt == "reel":
        return check_reel(post)
    elif fmt == "static":
        return check_static(post)
    else:
        return False, [f"TÉCNICO: formato desconhecido '{fmt}'"]


def print_result(approved: bool, failures: list):
    if approved:
        print("✅ QUALITY GATE: aprovado para publicação")
    else:
        print("❌ QUALITY GATE: reprovado")
        for f in failures:
            print(f"   • {f}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python quality_gate.py <caminho_para_post.json>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        post = json.load(f)
    approved, failures = run_gate(post)
    print_result(approved, failures)
    sys.exit(0 if approved else 1)
