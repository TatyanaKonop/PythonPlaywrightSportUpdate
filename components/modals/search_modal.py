from playwright.sync_api import Page
from page_factory.button import Button
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class SearchModal:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator
        self.search_button = Button(self.root_locator, name='Search')
        self.search_input_locator = self.root_locator.page.get_by_role("search")
        self.search_input = Input(self.search_input_locator.locator("//input[@placeholder='Search']"), name='Search')
        self.submit_button = Button(self.search_input_locator.locator("//button[@id='searchsubmit']"), name='Submit')

    def find_result(self, search_data: str) -> None:
        self.search_button.should_be_visible()
        self.search_button.click()
        self.search_input.fill_field(search_data, validate_value=True)
        self.submit_button.click()




