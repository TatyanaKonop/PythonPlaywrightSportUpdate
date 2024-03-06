import allure
from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def double_click(self):
        with allure.step(f'Double clicking {self.type_of} with name "{self.name}"'):
            self.locator.dblclick()

    def get_text_in_serch_result_block(self) -> str:
        with allure.step(f'Retrieve text on {self.type_of} in search result block'):
            text = self.locator.inner_text()
            return text
