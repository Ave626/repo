import logging

logger = logging.getLogger(__name__)

def handle_request(user_id : int):
    logger.info("Обработка запроса пользователя")
    if user_id <= 0:
        logger.warning("Неккоректный user_id")
    return {"status":"ok"}

