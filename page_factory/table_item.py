import allure

from page_factory.component import Component


class TableItem(Component):
    @property
    def type_of(self) -> str:
        return 'table item'

    def select_item_value(self, value: str, **kwargs) -> None:
        with allure.step(f'Select in {self.type_of} item with name "{self.name}"'):
            self.locator.select_option(value)

    def get_text(self) -> str:
        with allure.step(f'Retrieve text   on {self.type_of}: {self.name}'):
            text = self.locator.inner_text()
            return text

