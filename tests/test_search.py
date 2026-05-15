import pytest
from playwright.sync_api import Page, expect


# Tagging this as a critical "smoke" test
@pytest.mark.smoke
def test_search_for_hammer(custom_page_setup):
    page = custom_page_setup
    page.goto("https://practicesoftwaretesting.com/")
    page.get_by_placeholder("Search").fill("Hammer")
    page.get_by_role("button", name="Search").click()

    expect(page.locator(".card-title").first).to_contain_text("Hammer")


# Tagging this as a standard "regression" test
@pytest.mark.regression
def test_search_for_pliers(page: Page):
    page.goto("https://practicesoftwaretesting.com/")
    page.get_by_placeholder("Search").fill("Pliers")
    page.get_by_role("button", name="Search").click()

    expect(page.locator(".card-title").first).to_contain_text("Pliers")
