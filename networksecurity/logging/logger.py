import logging
import os
from datetime import datetime

log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO
)