import time

from playwright.sync_api import Locator

from page_factory.list_item import ListItem


class SideBar:
    def __init__(self, root_locator: Locator) -> None:
        self.root_locator = root_locator


    def navigate_to_section(self, sections_text: list) -> None:
        current_locator = self.root_locator
        for section_text in sections_text:
            xpath_query = "//ul/li[contains(., '{}')]".format(section_text)
            section_locator = current_locator.locator(xpath_query)
            ListItem(section_locator, name=f'{section_text.lower()}').click()
            current_locator = section_locator


