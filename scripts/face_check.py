"""
face_check.py — Detecta rosto em foto (YuNet/OpenCV). Trava em codigo da regra
"nada de rosto identificavel" dos carrosseis SFN.

Por que existe: foto CC0/CC BY resolve direito autoral, nao direito de imagem
de quem aparece. Publicando sem revisao humana, a regra precisa estar no codigo.
Na 1a execucao automatica com foto (07/10/2026) entrou uma largada de corrida
com corredores de frente — o prompt sozinho nao segurou.

count_faces(path) -> int | None      (None = nao foi possivel verificar)
Conta rostos com largura >= MIN_PX. Silhueta, costas, borrao e multidao
distante passam; rosto de frente em primeiro/segundo plano nao.
Modelo: scripts/models/face_detection_yunet_2023mar.onnx (OpenCV Zoo, MIT).
"""
import sys, subprocess
from pathlib import Path

MODEL = Path(__file__).parent / "models" / "face_detection_yunet_2023mar.onnx"
MODEL_URL = ("https://media.githubusercontent.com/media/opencv/opencv_zoo/main/models/"
             "face_detection_yunet/face_detection_yunet_2023mar.onnx")
MIN_PX, SCORE = 16, 0.70
_det = None


def _cv2():
    try:
        import cv2
        return cv2
    except Exception:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "opencv-python-headless",
                            "--break-system-packages"], timeout=240, capture_output=True)
            import cv2
            return cv2
        except Exception:
            return None


def count_faces(path):
    global _det
    cv2 = _cv2()
    if cv2 is None or not hasattr(cv2, "FaceDetectorYN"): return None
    try:
        if not MODEL.exists():
            import urllib.request
            MODEL.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(MODEL_URL, MODEL)
        if _det is None:
            _det = cv2.FaceDetectorYN.create(str(MODEL), "", (320, 320), SCORE, 0.3, 5000)
        img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
        if img is None: return None
        if img.ndim == 2: img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        if img.shape[2] == 4:                      # PNG recortado: cola sobre branco
            a = img[:, :, 3:4].astype("float32") / 255.0
            img = (img[:, :, :3].astype("float32") * a + 255.0 * (1 - a)).astype("uint8")
        h, w = img.shape[:2]
        if max(h, w) > 1600:
            k = 1600 / max(h, w); img = cv2.resize(img, (int(w * k), int(h * k))); h, w = img.shape[:2]
        _det.setInputSize((w, h))
        _, found = _det.detect(img)
        if found is None: return 0
        return sum(1 for f in found if f[2] >= MIN_PX)
    except Exception:
        return None


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(p, count_faces(p))
