import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def custom_page_setup():
    # --- SETUP: Runs BEFORE the test ---
    playwright = sync_playwright().start()
    
    # We are hardcoding headless=False here so we don't need the terminal flag anymore
    browser = playwright.chromium.launch(headless=False) 
    context = browser.new_context()
    page = context.new_page()

    # yield hands the 'page' over to the actual test script
    yield page

    # --- TEARDOWN: Runs AFTER the test finishes ---
    context.close()
    browser.close()
    playwright.stop()