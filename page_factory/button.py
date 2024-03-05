import allure
from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'button'

    def double_click(self):
        with allure.step(f'Double clicking {self.type_of} with name "{self.name}"'):
            self.locator.dblclick()
