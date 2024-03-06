import time

from playwright.sync_api import Page
from components.modals.search_modal import SearchModal
from page_factory.button import Button
from page_factory.input import Input
from page_factory.link import Link


class Navbar:

    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator
        self.main_menu_root = self.root_locator.locator("//ul[@id='menu-main-menu']")
        self.top_menu_root = self.root_locator.locator("//ul[contains(@class, 'top_menu')]")

    def navigate_to_section_on_main_menu(self, sections_text: list) -> None:
        xpath_query_on_main = f"//li/a[text()=('{sections_text[0]}')]"
        section_locator = self.main_menu_root.locator(xpath_query_on_main)
        Button(section_locator, name=f'section_{sections_text[0].lower()}').click()
        xpath_query_on_submenu = f"//..//ul[@class='sub-menu']//li/a[text()=('{sections_text[1]}')]"
        submenu_locator = section_locator.locator(xpath_query_on_submenu)
        Button(submenu_locator, name=f'{sections_text[1].lower()}').click()

    def navigate_to_section_on_top_menu(self, sections_text: list) -> None:
        xpath_query_on_top = f"//a[text()=('{sections_text[0]}')]"
        with self.top_menu_root.page.expect_popup() as page1_info:  # Switch to side url
            section_locator = self.top_menu_root.locator(xpath_query_on_top)
            Button(section_locator, name=f'{sections_text[0].lower()}').click()
        page = page1_info.value
        return page
