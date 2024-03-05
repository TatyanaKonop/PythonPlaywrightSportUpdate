import time

from playwright.sync_api import Page

from components.modals.calendar import Calendar
from page_factory.button import Button
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class EventCalendar:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator

    def filter(self, list_filter: list):
        self.button_show = Button(self.root_locator.page.locator("//div[button[contains(text(), 'SHOW')]][1]/button"),
                                  name='button show')
        self.button_show.click()
        for type_filter in list_filter:
            for event_type, list_checkbox in type_filter.items():
                self.event_type_button = Button(self.root_locator.locator(f"//div[label[contains(text(), '{event_type}')]]"),
                                                name=f'event type filter {event_type}')
                self.event_type_button.click()
                global item_ckeckbox
                for checkbox_item in list_checkbox:
                    item_ckeckbox = ListItem(self.root_locator.page.locator(
                        f"//li[contains(@class, 'MuiMenuItem-root')and text()= '{checkbox_item}']"), name='checkbox items')
                    item_ckeckbox.click()
                item_ckeckbox.send_keys('Escape')

    def retrieve_text_filtered_items(self):
        list = []
        self.sesult_filter_result_roots = self.root_locator.page.locator("//ul[contains(@class ,'MuiPaper-root')]/li").all()
        for filtered_item in self.sesult_filter_result_roots:
            button_text = Button(filtered_item, name=f'result filter {filtered_item}').get_text()
            list.append(button_text)
        list.pop()
        return list



        # Button(self.root_locator.page.locator("//*[@data-testid='ArrowForwardIcon']"), name='arrow calendar')
        #
        # self.calendar = Calendar("//div[contains(@class,'MuiPaper-root')]/div[contains(@class,'MuiBox-root')]")


