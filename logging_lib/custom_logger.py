import logging

def logger() -> object:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    format_logs = logging.Formatter( 
        "%(asctime)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    handler_console = logging.StreamHandler()
    handler_console.setFormatter(format_logs)
    logger.addHandler(handler_console)

    file_handler = logging.FileHandler("logs2.log", mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(format_logs)
    logger.addHandler(file_handler)

    return logger

log = logger()

log.info("register info")
