import logging #именованные логгеры для модулей, программа должна выбрасывать Traceback!!!
from api import handle_request
from db import save_record

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    db_logger = logging.getLogger("app.db")
    db_logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    configure_logging()
    logging.getLogger(__name__).info("Приложение стартует")  
    handle_request(42)
    try:
        save_record({"name": "test"})  
    except Exception:
        logging.getLogger(__name__).exception("Исключение на верхнем уровне")
