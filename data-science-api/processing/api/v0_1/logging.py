"""
Adapted from https://github.com/tiangolo/fastapi/issues/1276#issuecomment-615877177
"""

import stackprinter
import asyncio
import logging
import sys
from datetime import date, datetime
from pprint import pformat

from loguru import logger
from loguru._defaults import LOGURU_FORMAT

stackprinter.set_excepthook(style="darkbg2")


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def format_record(record: dict) -> str:
    """
    Custom format for loguru loggers.
    Uses pformat for log any data like request/response body during debug.
    Works with logging if loguru handler it.

    Example:
    >>> payload = [{"users":[{"name": "Nick", "age": 87, "is_active": True}, {"name": "Alex", "age": 27, "is_active": True}], "count": 2}]
    >>> logger.bind(payload=).debug("users payload")
    >>> [   {   'count': 2,
    >>>         'users': [   {'age': 87, 'is_active': True, 'name': 'Nick'},
    >>>                      {'age': 27, 'is_active': True, 'name': 'Alex'}]}]
    """
    format_string = LOGURU_FORMAT + "\n"

    if record["extra"].get("payload") is not None:
        record["extra"]["payload"] = pformat(
            record["extra"]["payload"], indent=2, compact=True, width=120
        )
        format_string += "\n<level>{extra[payload]}</level>"

    if record["exception"] is not None:
        record["extra"]["stack"] = stackprinter.format(record["exception"])
        format_string += "{extra[stack]}\n"

    return format_string


"""
CONFIGURE logger OBJECT
"""

# set loguru format for root logger
logging.getLogger().handlers = [InterceptHandler()]

# set format
logger.configure(handlers=[{"sink": sys.stdout, "level": logging.INFO, "format": format_record}])

logger.level("INFO+", no=15, color="<cyan><italic>", icon="@")


# works with uvicorn==0.11.6
loggers = (
    logging.getLogger(name)
    for name in logging.root.manager.loggerDict
    if name.startswith("uvicorn.")
)
for uvicorn_logger in loggers:
    uvicorn_logger.handlers = []
