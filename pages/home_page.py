from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = "[data-test=\"search-query\"]"
        self.search_button= "[data-test=\"search-button\"]"

    def search_for_product(self, product_name):
        self.fill_text(self.search_input, product_name)
        self.click_element(self.search_button)