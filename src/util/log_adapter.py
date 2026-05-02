import os
import logging

def setup_logger():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # INFO logs
    info_handler = logging.FileHandler("logs/info.log")
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    # WARNING logs
    warning_handler = logging.FileHandler("logs/warning.log")
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)

    # ERROR + EXCEPTION logs
    error_handler = logging.FileHandler("logs/error.log")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)

    # console handler for werkzeug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(message)s")
    )
    
    # remove file logging for werkzeug
    werkzeug_logger = logging.getLogger("werkzeug")
    werkzeug_logger.propagate = False

    werkzeug_logger.addHandler(console_handler)