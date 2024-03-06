import allure
from playwright.sync_api import Page, Response
from data.environment import host

class BasePage:
    def __init__(self, page: Page):
        self.page = page


    def open(self, uri) -> Response | None:
        with allure.step(f'Open website with URL {host.get_base_url()}{uri} '):
            return self.page.goto(f'{host.get_base_url()}{uri}', wait_until='domcontentloaded')

    def reload(self, uri) :
        with allure.step(f'Reloading page with url "{host.get_base_url()}{uri}"'):
            return self.page.reload(wait_until='domcontentloaded')
