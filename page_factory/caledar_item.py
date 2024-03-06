import allure

from page_factory.component import Component


class CalendarItem(Component):
    @property
    def type_of(self) -> str:
        return 'Calendar item'

    def click_month(self, period) -> None:
        with allure.step(f'Clicking {self.type_of} month with name "{self.name}" on {period} month section'):
            self.locator.click()
    def get_text_month_period(self, period) -> str:
        with allure.step(f'Retrieve text on active {self.type_of} on {period} month section '):
            text = self.locator.inner_text()
            return text