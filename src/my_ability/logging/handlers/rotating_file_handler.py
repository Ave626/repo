#вывод сначала в app.log пока он не достигнет maxbytes
#потом файл переименовывается в app.log.1 и создается новый
#файлов может быть = backupcount, потом 1 удаляется
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    "app.log",      
    maxBytes=500,   
    backupCount=3, 
    encoding="utf-8"
)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

for i in range(50):
    logger.debug(f"Сообщение номер {i}")
