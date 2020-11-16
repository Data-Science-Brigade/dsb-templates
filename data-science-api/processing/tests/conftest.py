import sys
import pytest
import subprocess

from api.v0_1.logging import logging, logger, format_record


def pytest_configure(config):
    if config.option.verbose == 0:
        logger.configure(
            handlers=[
                {"sink": sys.stdout, "level": logging.CRITICAL, "format": format_record}
            ]
        )
    elif config.option.verbose == 1:

        logger.configure(
            handlers=[{"sink": sys.stdout, "level": "INFO+", "format": format_record}]
        )
    else:
        logger.configure(
            handlers=[
                {"sink": sys.stdout, "level": logging.DEBUG, "format": format_record}
            ]
        )
