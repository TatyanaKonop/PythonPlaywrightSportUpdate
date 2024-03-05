from playwright.sync_api import Page

from components.modals.event_calendar import EventCalendar
from components.modals.table import Table
from page_factory.button import Button
from page_factory.title import Title
from pages.base_page import BasePage
from utils.api import retrieve_values_from_list_with_dict


class CalendarResultPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.event_calendar = EventCalendar(page.locator("//div[contains(@class, 'MuiGrid-root')]"))
        self.table = Table(page.locator("//table[contains(@class,'manualStriped')]"))

    def text_filtered_present(self, data_list):
        list_filtered_items = retrieve_values_from_list_with_dict(data_list)
        text_filtered_items = self.event_calendar.retrieve_text_filtered_items()
        for items in text_filtered_items:
           assert items in list_filtered_items



