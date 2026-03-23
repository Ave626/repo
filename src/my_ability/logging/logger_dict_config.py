import os
import logging
import logging.config

def get_dev_config():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "dev": {
                "format": "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
                "datefmt": "%H:%M:%S",
            }
        },
        "handlers": {
            "console_debug": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "dev",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            "app": {
                "level": "DEBUG",
                "handlers": ["console_debug"],
                "propagate": False,
            }
        },
        "root": {
            "level": "WARNING",
            "handlers": ["console_debug"]
        }
    }

def get_prod_config(log_dir="logs"):
    os.makedirs(log_dir, exist_ok=True)
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "prod_info": {
                "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "prod_error": {
                "format": "%(asctime)s %(levelname)s %(name)s [%(filename)s:%(lineno)d]: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "file_info_rotating": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "prod_info",
                "filename": os.path.join(log_dir, "app.info.log"),
                "maxBytes": 5_000_000,
                "backupCount": 5,
                "encoding": "utf-8",
            },
            "file_error_rotating": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "prod_error",
                "filename": os.path.join(log_dir, "app.error.log"),
                "maxBytes": 5_000_000,
                "backupCount": 5,
                "encoding": "utf-8",
            }
        },
        "loggers": {
            "app": {
                "level": "INFO",
                "handlers": ["file_info_rotating", "file_error_rotating"],
                "propagate": False,
            }
        },
        "root": {
            "level": "WARNING",
            "handlers": ["file_error_rotating"]
        }
    }

def configure_logging(env: str = "dev"):
    if env == "prod":
        logging.config.dictConfig(get_prod_config())
    else:
        logging.config.dictConfig(get_dev_config())

if __name__ == "__main__":
    env = os.getenv("APP_ENV", "dev")
    configure_logging(env)

    logger = logging.getLogger("app.main")
    logger.info("Система запущена в режиме: %s", env)
    
    try:
        logger.debug("Проверка ресурсов...")
        raise ValueError("Пример ошибки")
    except Exception:
        logger.exception("Произошла непредвиденная ошибка")