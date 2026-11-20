"""BeeWell entry point.

While coding (auto-reload):    uv run python -m beewell.main
"""

from loguru import logger
from nicegui import app, ui

from beewell.config import settings
from beewell.logging_config import setup_logging

setup_logging(settings.log_level, settings.debug)


@ui.page("/")
def index() -> None:
    """Temporary hello world page, dashboard later"""
    ui.label("BeeWell")


app.on_startup(lambda: setup_logging(settings.log_level, settings.debug))

if __name__ in {"__main__", "__mp_main__"}:
    logger.info("Starting BeeWell (debug={})", settings.debug)
    ui.run(title="BeeWell", favicon="🐝")
