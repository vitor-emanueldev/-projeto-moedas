import logging
from datetime import datetime

def configurar_logger():
    """
    Configura o sistema de logging para registrar mensagens em arquivo e no console.

    O logger salva os logs em um arquivo na pasta `logs/`, com o nome no formato 
    `log_YYYYMMDD.log`, e também imprime as mensagens no console. O nível de log 
    padrão é INFO.

    Returns:
        logging.Logger: Instância do logger configurado.
    """
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