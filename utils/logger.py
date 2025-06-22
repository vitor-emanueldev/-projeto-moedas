import logging
from datetime import datetime

def configurar_logger():
    log_filename = f"logs/log_{datetime.now().strftime('%Y%m%d')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename, encoding="utf-8"),
            logging.StreamHandler()  # também exibe no console
        ]
    )

    return logging.getLogger()