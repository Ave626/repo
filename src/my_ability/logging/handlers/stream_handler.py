#Вывод в консоль
import logging

logger = logging.getLogger("logger_stream")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Это DEBUG сообщение")
logger.warning("Это WARNING сообщение")
