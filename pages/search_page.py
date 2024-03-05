from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, page: Page, search_data: str=None) -> None:
        super().__init__(page)

        formatted_selector = f'//span[text()="Search results for \'{search_data}\'"]'
        self.result_title = Title(page.locator(formatted_selector), name='Search title')

    def text_search_present(self, text):
        self.result_title.should_be_visible()
        self.result_title.should_have_text(text)
