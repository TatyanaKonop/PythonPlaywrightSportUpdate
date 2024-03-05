from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage

class ThreeSearchFormatPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.result_title = Title(page.locator("//div[@class='container']/div/span[last()]"), name='Search title')

    def text_search_present(self, text):
        self.result_title.should_be_visible()
        self.result_title.should_have_text(text)
