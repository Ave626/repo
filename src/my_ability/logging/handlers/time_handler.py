#новый файл каждые 10 секунд(максимум 3)
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = TimedRotatingFileHandler(
    "test.log",
    when="S",          
    interval=10,       
    backupCount=3,     
    encoding="utf-8"
)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

for i in range(50):
    logger.debug(f"Сообщение номер {i}")
    time.sleep(2)
