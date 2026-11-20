"""BeeWell entry point.

While coding (auto-reload):    uv run python -m beewell.main
"""

from loguru import logger
from nicegui import ui

from beewell.config import settings
from beewell.logging_config import setup_logging

setup_logging(settings.log_level, settings.debug)


@ui.page("/")
def index() -> None:
    """Temporary hello world page, dashboard later"""
    ui.label("BeeWell")


if __name__ in {"__main__", "__mp_main__"}:
    logger.info("Starting BeeWell (debug={})", settings.debug)
    # log_config=None: uvicorn keeps its hands off logging, so its logs go through Loguru too
    ui.run(title="BeeWell", favicon="🐝", log_config=None)
