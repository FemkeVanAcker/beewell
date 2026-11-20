"""Page tests: open a page like a user would and check what is on screen."""

from nicegui.testing import User


async def test_home_page_shows_beewell(user: User) -> None:
    await user.open("/")
    await user.should_see("BeeWell")
