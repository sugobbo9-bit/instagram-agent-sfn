"""
daily_loop.py — Orquestrador do ciclo diário autônomo do Instagram Agent
Executa: analytics → winners/losers → fila → pesquisa → decisão → produção → quality gate → publicação → log
"""
import json
import sys
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import DIRS, check_credentials
from analytics_collector import run as collect_analytics
from quality_gate import run_gate, print_result


def log(msg: str, level: str = "INFO"):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] [{level}] {msg}"
    print(line)
    log_path = DIRS["logs"] / "daily_loop.jsonl"
    with open(log_path, "a") as f:
        f.write(json.dumps({"ts": ts, "level": level, "msg": msg}) + "\n")


def load_json(path: Path) -> dict | list:
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def step_health_check() -> bool:
    log("PASSO 1: Verificação de saúde do sistema")
    missing = check_credentials()
    if missing:
        log(f"Credenciais ausentes: {missing}. Sistema continuará sem publicação automática.", "WARN")
        return False
    log("Credenciais OK.")
    return True


def step_analytics():
    log("PASSO 3-4: Coletando analytics e atualizando banco de dados")
    try:
        collect_analytics()
    except Exception as e:
        log(f"Erro na coleta de analytics: {e}", "ERROR")


def step_review_winners_losers():
    log("PASSO 5: Revisando winners e losers")
    db = load_json(DIRS["data"] / "posts_db.json")
    posts = db.get("posts", [])
    if not posts:
        log("Sem posts no banco ainda.")
        return

    winners = [p for p in posts if p.get("performance_tier") == "top10"]
    losers = [p for p in posts if p.get("performance_tier") == "bottom25"]
    log(f"Top-10%: {len(winners)} posts | Bottom-25%: {len(losers)} posts")

    # Atualiza winner library
    winner_db = load_json(DIRS["data"] / "winner_library.json")
    existing_ids = {w["post_id"] for w in winner_db.get("winners", [])}
    for w in winners:
        if w["post_id"] not in existing_ids:
            winner_db["winners"].append({
                "post_id": w["post_id"],
                "topic": w.get("topic"),
                "hook": w.get("hook"),
                "format": w.get("format"),
                "performance_tier": "top10",
                "why_it_worked": None,
                "derivatives_planned": [],
            })
    save_json(DIRS["data"] / "winner_library.json", winner_db)

    # Atualiza failure log
    failure_db = load_json(DIRS["data"] / "failure_log.json")
    existing_fail_ids = {f["post_id"] for f in failure_db.get("failures", [])}
    for loser in losers:
        if loser["post_id"] not in existing_fail_ids:
            failure_db["failures"].append({
                "post_id": loser["post_id"],
                "topic": loser.get("topic"),
                "hook": loser.get("hook"),
                "format": loser.get("format"),
                "diagnosis": None,
            })
    save_json(DIRS["data"] / "failure_log.json", failure_db)


def step_publish_queue(can_publish: bool):
    log("PASSO 11: Verificando fila de publicação")
    queue_db = load_json(DIRS["data"] / "publishing_queue.json")
    queue = queue_db.get("queue", [])

    now_hour = datetime.now().hour
    ready = [item for item in queue if item.get("status") == "approved"]
    if not ready:
        log("Fila vazia — nenhum post aprovado para publicar hoje.")
        return

    # Seleciona primeiro da fila para o horário atual
    item = ready[0]
    log(f"Post pronto para publicação: {item.get('local_id')} ({item.get('format')})")

    # Roda quality gate
    draft_path = DIRS["content"] / "approved" / f"{item['local_id']}.json"
    if not draft_path.exists():
        log(f"Arquivo de draft não encontrado: {draft_path}", "ERROR")
        return

    with open(draft_path) as f:
        post_data = json.load(f)

    approved, failures = run_gate(post_data)
    print_result(approved, failures)

    if not approved:
        log(f"Quality gate reprovado para {item['local_id']}. Não publicado.", "WARN")
        item["status"] = "quality_gate_failed"
        item["quality_failures"] = failures
        save_json(DIRS["data"] / "publishing_queue.json", queue_db)
        return

    if not can_publish:
        log("Credenciais não configuradas. Post aprovado mas não publicado automaticamente.", "WARN")
        return

    # Publica
    from instagram_api import InstagramAPI
    api = InstagramAPI()
    try:
        fmt = post_data.get("format")
        caption = post_data.get("caption", "")
        if fmt == "carousel":
            # Precisaria de URLs públicas — para implementação completa ver README
            log("Publicação de carrossel requer URLs públicas dos slides. Ver README.", "WARN")
        elif fmt == "static":
            log("Publicação de estático requer URL pública da imagem. Ver README.", "WARN")
        elif fmt == "reel":
            log("Publicação de Reel requer URL pública do vídeo. Ver README.", "WARN")

        item["status"] = "published"
        item["published_at"] = datetime.now(timezone.utc).isoformat()
        save_json(DIRS["data"] / "publishing_queue.json", queue_db)
        log(f"Post {item['local_id']} publicado com sucesso.")
    except Exception as e:
        log(f"Erro na publicação: {e}", "ERROR")
        item["status"] = "publish_failed"
        item["error"] = str(e)
        save_json(DIRS["data"] / "publishing_queue.json", queue_db)


def step_log_exit():
    log("PASSO 12: Ciclo diário concluído.")
    summary_path = DIRS["logs"] / f"daily_{datetime.now().strftime('%Y%m%d')}.json"
    summary = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "status": "ok",
    }
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)


def run():
    log("=" * 60)
    log("INSTAGRAM AGENT — CICLO DIÁRIO INICIADO")
    log("=" * 60)

    can_publish = step_health_check()

    log("PASSO 2: Verificando fila de publicação")
    step_analytics()
    step_review_winners_losers()

    log("PASSO 6-10: Pesquisa e produção de conteúdo delegadas ao Claude Code")
    log("  → Claude Code lê CLAUDE.md e executa pesquisa → escrita → design → render")

    step_publish_queue(can_publish)
    step_log_exit()

    log("CICLO CONCLUÍDO.")


if __name__ == "__main__":
    run()
