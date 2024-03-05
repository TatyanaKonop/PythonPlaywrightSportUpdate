from playwright.sync_api import Page

from components.modals.search_modal import SearchModal
from components.navigation.navbar import Navbar
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.navbar = Navbar(page.locator("//nav"))
        self.search = SearchModal(page.locator("//div[@class='search_icon']//img"))

