from playwright.sync_api import Page
from components.navigation.sidebar import SideBar
from pages.base_page import BasePage



class OrientInternal(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.sidebar = SideBar(page.locator("//div[ul[@class='page_menu']]"))





