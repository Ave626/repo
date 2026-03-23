import logging
logger = logging.getLogger(__name__)

def save_record(record : dict):
    logger.debug("Сохранение записи: %r", record)
    try:
        if "id" not in record:
            raise ValueError("Нет поля 'id'")
        logger.info("Запись %s сохранена", record["id"])
    except Exception as exc:
        logger.error("Ошибка при сохранении: %s", exc)
        raise