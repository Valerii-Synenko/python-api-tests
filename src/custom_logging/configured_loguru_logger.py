import sys

import loguru
from loguru import logger


def get_configured_loguru_logger() -> loguru.logger:
    logger.remove()  # need for removing loguru loger with standard settings
    logger.add(
        sys.stdout,
        format="\n<green>{time:DD/MM/YY HH:mm}</green>"
        " \n<level>[{level}]</level> -> <level>{message}</level>",
        colorize=True,
    )
    return logger


loguru_logger = get_configured_loguru_logger()
