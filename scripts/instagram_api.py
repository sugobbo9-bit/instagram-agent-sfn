"""
instagram_api.py — Wrapper para a Instagram Graph API
Cobre: publicação de posts/reels/carrosséis e coleta de insights
"""
import requests
import json
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config import (
    INSTAGRAM_BUSINESS_ACCOUNT_ID,
    INSTAGRAM_ACCESS_TOKEN,
    INSTAGRAM_GRAPH_API_BASE,
)


class InstagramAPI:
    def __init__(self):
        self.account_id = INSTAGRAM_BUSINESS_ACCOUNT_ID
        self.token = INSTAGRAM_ACCESS_TOKEN
        self.base = INSTAGRAM_GRAPH_API_BASE
        self.session = requests.Session()

    def _get(self, path, params=None):
        params = params or {}
        params["access_token"] = self.token
        r = self.session.get(f"{self.base}/{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()

    def _post(self, path, data=None):
        data = data or {}
        data["access_token"] = self.token
        r = self.session.post(f"{self.base}/{path}", data=data, timeout=60)
        r.raise_for_status()
        return r.json()

    # ── Conta ──────────────────────────────────────────────────────────
    def get_account_info(self):
        """Retorna informações básicas da conta."""
        return self._get(
            self.account_id,
            {"fields": "id,name,username,followers_count,media_count,biography,website"}
        )

    # ── Publicação de imagem única / estático ───────────────────────────
    def upload_static(self, image_url: str, caption: str) -> dict:
        """Cria container de imagem e publica."""
        container = self._post(f"{self.account_id}/media", {
            "image_url": image_url,
            "caption": caption,
        })
        container_id = container["id"]
        self._wait_for_container(container_id)
        return self._post(f"{self.account_id}/media_publish", {"creation_id": container_id})

    # ── Publicação de carrossel ─────────────────────────────────────────
    def upload_carousel(self, image_urls: list, caption: str) -> dict:
        """Cria containers de cada slide e publica como carrossel."""
        child_ids = []
        for url in image_urls:
            c = self._post(f"{self.account_id}/media", {
                "image_url": url,
                "is_carousel_item": True,
            })
            child_ids.append(c["id"])
            time.sleep(1)

        container = self._post(f"{self.account_id}/media", {
            "media_type": "CAROUSEL",
            "children": ",".join(child_ids),
            "caption": caption,
        })
        container_id = container["id"]
        self._wait_for_container(container_id)
        return self._post(f"{self.account_id}/media_publish", {"creation_id": container_id})

    # ── Publicação de Reel ──────────────────────────────────────────────
    def upload_reel(self, video_url: str, caption: str, cover_url: str = None) -> dict:
        """Cria container de Reel e publica."""
        data = {
            "media_type": "REELS",
            "video_url": video_url,
            "caption": caption,
            "share_to_feed": True,
        }
        if cover_url:
            data["cover_url"] = cover_url
        container = self._post(f"{self.account_id}/media", data)
        container_id = container["id"]
        self._wait_for_container(container_id, max_wait=120)
        return self._post(f"{self.account_id}/media_publish", {"creation_id": container_id})

    def _wait_for_container(self, container_id: str, max_wait: int = 60):
        """Aguarda o container estar pronto para publicação."""
        for _ in range(max_wait // 5):
            status = self._get(container_id, {"fields": "status_code"})
            code = status.get("status_code", "")
            if code == "FINISHED":
                return
            if code in ("ERROR", "EXPIRED"):
                raise RuntimeError(f"Container {container_id} falhou com status: {code}")
            time.sleep(5)
        raise TimeoutError(f"Container {container_id} não ficou pronto em {max_wait}s")

    # ── Insights ────────────────────────────────────────────────────────
    def get_media_insights(self, media_id: str, media_type: str = "carousel") -> dict:
        """Coleta métricas de um post publicado."""
        base_metrics = "reach,impressions,likes,comments,shares,saved,follows,profile_visits"
        if media_type == "reel":
            metrics = base_metrics + ",plays,total_plays,ig_reels_avg_watch_time,ig_reels_video_view_total_time"
        else:
            metrics = base_metrics

        try:
            data = self._get(f"{media_id}/insights", {"metric": metrics, "period": "lifetime"})
            result = {item["name"]: item["values"][0]["value"] for item in data.get("data", [])}
            return result
        except Exception as e:
            return {"error": str(e)}

    def get_recent_posts(self, limit: int = 50) -> list:
        """Retorna posts recentes da conta com campos de análise."""
        data = self._get(f"{self.account_id}/media", {
            "fields": "id,timestamp,media_type,caption,permalink,thumbnail_url,media_url",
            "limit": limit,
        })
        return data.get("data", [])

    def get_account_insights(self, days: int = 30) -> dict:
        """Retorna insights agregados da conta."""
        metrics = "reach,impressions,profile_views,follower_count,accounts_engaged"
        try:
            data = self._get(f"{self.account_id}/insights", {
                "metric": metrics,
                "period": "day",
                "since": int(time.time()) - (days * 86400),
                "until": int(time.time()),
            })
            return data.get("data", {})
        except Exception as e:
            return {"error": str(e)}


if __name__ == "__main__":
    api = InstagramAPI()
    if not api.account_id or not api.token:
        print("⚠️  Configure o arquivo .env com INSTAGRAM_BUSINESS_ACCOUNT_ID e INSTAGRAM_ACCESS_TOKEN")
        sys.exit(1)
    info = api.get_account_info()
    print(json.dumps(info, indent=2, ensure_ascii=False))
