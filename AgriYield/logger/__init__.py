import logging
import os
from datetime import datetime

# === Project root (where demo.py is) ===
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # path of /AgriYield
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)  # one level up
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)  # two levels up

# === Logs folder and file ===
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_dir, exist_ok=True)

logs_path = os.path.join(log_dir, LOG_FILE)

# === Logging setup (file + console) ===
logging.basicConfig(
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler()
    ]
)

print(f"✅ Logging initialized at: {logs_path}")
