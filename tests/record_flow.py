import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.locator("[data-test=\"search-query\"]").click()
    page.locator("[data-test=\"search-query\"]").fill("hammer")
    page.locator("[data-test=\"search-query\"]").press("Enter")
    page.locator("[data-test=\"brand-01KPAHECK1M0SKKQ7FW8YXG3QS\"]").check()
    page.locator("[data-test=\"product-01KPAHECYF3R1KKW5D01SFQS2T\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
