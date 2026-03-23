#Вывод в файд
import logging

logger = logging.getLogger("logger_file")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename="my_lg.log",mode="w",encoding="utf-8")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("Это INFO сообщение")
logger.critical("Это CRITICAL сообщение")
