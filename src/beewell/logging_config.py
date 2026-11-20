"""Logging setup for BeeWell using Loguru"""

import inspect
import logging
import sys

from loguru import logger


class InterceptHandler(logging.Handler):
    """Send standard library log records (NiceGUI, uvicorn, SQLAlchemy) to Loguru"""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            level: str | int = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # find the code that made the logging call, so Loguru shows the right line and file
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

    def setup_logging(level: str = "INFO", debug: bool = False) -> None:
        """Configure Loguru and send all library logs through it.

        Parameters
        ----------
        level : str, optional
            Lowest level to show, e.g. ``"DEBUG"`` or ``"INFO"``.
        debug : bool, optional
            Show variable values in tracebacks. Only use this locally: it can
            expose passwords or health data.
        """
        logger.remove()
        logger.add(sys.stderr, level=level, backtrace=debug, diagnose=debug)

        logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
        logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
        