import logging
#Применяется в простых скриптах(можно задать сохранение в файл,настройка глобальная)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s")

def enroll_student(student_id,course_name,payment_status,has_email):
    logging.info(f"Запрос на запись студента {student_id} на курс '{course_name}'")
    logging.debug(f"Начинаем проверку статуса транзакции для ID {student_id}...")

    if payment_status == "api_timeout":
        logging.critical("Сервер банка не отвечает! Оплаты полностью остановились!")
        return False

    if payment_status == "declined":
        logging.error(f"Оплата отклонена. Студент {student_id} не добавлен.")
        return False
    
    logging.debug("Оплата успешна подтверждена банком")

    if not has_email:
        logging.warning(f"У студента {student_id} нет email. Он не получит ссылку на личный кабинет.")
    
    logging.info(f"Успех! Студент {student_id} зачислен на курс '{course_name}'.")
    return True

enroll_student(student_id=101, course_name="Основы FastAPI", payment_status="success", has_email=True)
print()
enroll_student(student_id=102, course_name="Алгоритмы", payment_status="success", has_email=False)
print()
enroll_student(student_id=103, course_name="Базы данных", payment_status="declined", has_email=True)
print()
enroll_student(student_id=104, course_name="Docker", payment_status="api_timeout", has_email=True)

