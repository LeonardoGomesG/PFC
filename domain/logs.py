import logging


def configure_logs():
    logger = logging.getLogger("LOG")

    # Create handlers
    file_handler = logging.FileHandler(filename='domain/logs/logs.log', mode='a')
    stream_handler = logging.StreamHandler()
    
    file_formatter = logging.Formatter(fmt='%(asctime)s -- %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    stream_formatter = logging.Formatter(fmt='%(message)s')

    file_handler.setFormatter(file_formatter)
    stream_handler.setFormatter(stream_formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)

    log_start()

def log_start():
    logger = logging.getLogger("LOG")
    logger.info("---------------------------")
    logger.info("LOG START")

def log_end():
    logger = logging.getLogger("LOG")
    logger.info("LOG END")
    logger.info("---------------------------")
