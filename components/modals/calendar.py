import allure

from page_factory.caledar_item import CalendarItem



class Calendar:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator
        self.selector_month = "//div[h6[contains(text(),'{} month')]]//button[contains(text(),'{}')]"

    def check_calendar_automatically_change_end_month_if_start_data_ahead(self, month):
        start_selector_month = self.selector_month.format("Start", month)
        self.month_button_start = CalendarItem(self.root_locator.locator(start_selector_month), name=f"{month} ")
        self.month_button_start.click_month('Start')
        name_month_start = self.month_button_start.get_text_month_period('start')
        end_selector_month = self.selector_month.format("End", month)
        self.month_button_end = CalendarItem(self.root_locator.locator(end_selector_month), name=" end month")
        name_month_end = self.month_button_end.get_text_month_period('end')
        with allure.step(f'Checking that end month name changed to start month name"'):
            assert name_month_start == name_month_end  # Check that when start data is ahead of  end data that end data will be changed automatically
