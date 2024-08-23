import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Сделать headless=True, если не нужно отображать браузер
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

