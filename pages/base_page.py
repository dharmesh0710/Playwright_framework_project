from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
    
    def click_element(self, selector: str):
        self.page.locator(selector).click()

    def fill_text(self, selector: str, text: str):
        self.page.locator(selector).fill(text)  

    def wait_for_element(self, selector: str):
        self.page.locator(selector).wait_for(state="visible")