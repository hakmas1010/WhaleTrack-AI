# Placeholder – real implementation private.
from pathlib import Path
import json


class AlertManager:
    def __init__(self):
        self._settings = self._load_settings()

    def _load_settings(self) -> dict:
        try:
            root = Path(__file__).resolve().parents[2]
            settings_path = root / "settings.json"
            if settings_path.exists():
                with settings_path.open("r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return {}

    def send_alert(self, message: str):
        # Always echo to console in the demo
        print(f"ALERT: {message}")

        try:
            alerts_cfg = self._settings.get("alerts", {})
            if alerts_cfg.get("write_to_file"):
                root = Path(__file__).resolve().parents[2]
                rel_path = alerts_cfg.get("file_path", "data/alerts.log")
                log_path = (root / rel_path).resolve()
                log_path.parent.mkdir(parents=True, exist_ok=True)
                with log_path.open("a", encoding="utf-8") as f:
                    f.write(message + "\n")
        except Exception:
            # Swallow errors in placeholder
            pass
