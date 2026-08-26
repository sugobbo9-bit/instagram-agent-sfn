"""
analytics_collector.py — Coleta e normaliza métricas dos posts publicados
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import DIRS
from instagram_api import InstagramAPI


def load_db():
    db_path = DIRS["data"] / "posts_db.json"
    with open(db_path) as f:
        return json.load(f)

def save_db(db):
    db_path = DIRS["data"] / "posts_db.json"
    with open(db_path, "w") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def hours_since(iso_date: str) -> float:
    dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    return (now - dt).total_seconds() / 3600

def determine_checkpoint(post: dict) -> str | None:
    """Retorna qual checkpoint deve ser coletado agora, ou None."""
    pub_date = post.get("publication_date")
    if not pub_date:
        return None
    hours = hours_since(pub_date)
    metrics = post.get("metrics", {})
    if hours >= 24 and "24h" not in metrics:
        return "24h"
    if hours >= 72 and "72h" not in metrics:
        return "72h"
    if hours >= 168 and "7d" not in metrics:
        return "7d"
    if hours >= 720 and "30d" not in metrics:
        return "30d"
    return None

def compute_ratios(raw: dict, reach: int) -> dict:
    """Calcula ratios normalizados por reach."""
    if not reach:
        return {}
    return {
        "shares_per_reach": round(raw.get("shares", 0) / reach, 4),
        "saves_per_reach": round(raw.get("saved", 0) / reach, 4),
        "follows_per_reach": round(raw.get("follows", 0) / reach, 4),
        "profile_visits_per_reach": round(raw.get("profile_visits", 0) / reach, 4),
        "comments_per_reach": round(raw.get("comments", 0) / reach, 4),
        "likes_per_reach": round(raw.get("likes", 0) / reach, 4),
    }

def classify_performance(db: dict):
    """Recalcula performance_tier para todos os posts com dados de 7d."""
    by_format = {"carousel": [], "reel": [], "static": []}
    for post in db["posts"]:
        metrics_7d = post.get("metrics", {}).get("7d", {})
        reach = metrics_7d.get("reach", 0)
        if reach:
            fmt = post.get("format", "carousel")
            by_format[fmt].append((post["post_id"], reach))

    for fmt, items in by_format.items():
        if len(items) < 4:
            continue
        items.sort(key=lambda x: x[1])
        n = len(items)
        top10_threshold = items[int(n * 0.90)][1]
        top25_threshold = items[int(n * 0.75)][1]
        bottom25_threshold = items[int(n * 0.25)][1]

        for post in db["posts"]:
            if post.get("format") != fmt:
                continue
            reach = post.get("metrics", {}).get("7d", {}).get("reach", 0)
            if not reach:
                continue
            if reach >= top10_threshold:
                post["performance_tier"] = "top10"
            elif reach >= top25_threshold:
                post["performance_tier"] = "top25"
            elif reach >= bottom25_threshold:
                post["performance_tier"] = "median"
            else:
                post["performance_tier"] = "bottom25"

def run():
    api = InstagramAPI()
    if not api.account_id or not api.token:
        print("⚠️  Credenciais não configuradas. Abortando coleta.")
        return

    db = load_db()
    collected = 0
    errors = 0

    for post in db["posts"]:
        checkpoint = determine_checkpoint(post)
        if not checkpoint:
            continue

        print(f"  Coletando {checkpoint} para post {post['post_id']}...")
        raw = api.get_media_insights(post["post_id"], post.get("format", "carousel"))
        if "error" in raw:
            print(f"  ⚠️  Erro: {raw['error']}")
            errors += 1
            continue

        reach = raw.get("reach", 0)
        ratios = compute_ratios(raw, reach)
        post["metrics"][checkpoint] = {
            "collected_at": datetime.now(timezone.utc).isoformat(),
            **raw,
            **ratios,
        }
        collected += 1
        time.sleep(1)

    classify_performance(db)
    save_db(db)

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "checkpoints_collected": collected,
        "errors": errors,
    }
    log_path = DIRS["logs"] / "analytics.jsonl"
    with open(log_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print(f"✅ Analytics: {collected} checkpoints coletados, {errors} erros.")

if __name__ == "__main__":
    run()
