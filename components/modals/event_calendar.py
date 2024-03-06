from page_factory.button import Button
from page_factory.filter_input import FilterInput
from page_factory.checkbox_list_item import CheckboxListItem


class EventCalendar:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator

    def filter(self, list_filter: list):
        self.button_show = Button(self.root_locator.page.locator("//div[button[contains(text(), 'SHOW')]][1]/button"),
                                  name='show filters')  # Open extra filter input
        self.button_show.click()
        for type_filter in list_filter:  # Go throw list_filter
            for event_type, list_checkbox in type_filter.items():  # Pass name of filter input
                self.event_type_button = FilterInput(
                    self.root_locator.locator(f"//div[label[contains(text(), '{event_type}')]]"),
                    name=f'{event_type}')
                self.event_type_button.click()
                global item_ckeckbox
                for checkbox_item in list_checkbox:  # Pass name of checkbox items in filter input
                    item_ckeckbox = CheckboxListItem(self.root_locator.page.locator(
                        f"//li[contains(@class, 'MuiMenuItem-root')and text()= '{checkbox_item}']"),
                        name=f'{checkbox_item}')
                    item_ckeckbox.click()
                item_ckeckbox.send_keys('Escape')  # Close list checkbox of filter

    def retrieve_text_filtered_items(self):  # Retrieve text on displayed button  on search result block
        list = []
        self.sesult_filter_result_roots = self.root_locator.page.locator(
            "//ul[contains(@class ,'MuiPaper-root')]/li").all()
        for filtered_item in self.sesult_filter_result_roots:  # Create list of retrieve name of buttons
            button_text = Button(filtered_item, name=f'result filtered button').get_text_in_serch_result_block()
            list.append(button_text)
        list.pop()  # Delete last element (button "clear") in list
        return list

    def open_calendar(self):
        self.calendar = Button(self.root_locator.page.locator("//*[@data-testid='ArrowForwardIcon']"),
                               name='arrow calendar')
        self.calendar.click()
