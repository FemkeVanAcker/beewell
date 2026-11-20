"""Smoke tests: check that the basic setup works."""
from loguru import logger

from beewell.config import settings
from beewell.logging_config import setup_logging


def test_settings_load() -> None:
    assert settings.log_level


def test_logging_setup_runs_twice(capsys) -> None:
    """Calling setup_logging() twice must not print every log line twice."""
    setup_logging()
    setup_logging()
    logger.info("logging works")
    assert capsys.readouterr().err.count("logging works") == 1
