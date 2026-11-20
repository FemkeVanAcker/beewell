"""Shared pytest setup."""

# NiceGUI's test tool: gives tests a `user` that can open pages without a real browser
pytest_plugins = ["nicegui.testing.user_plugin"]
