import allure

from page_factory.component import Component


class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'

    def select_item_value(self, value: str, **kwargs) -> None:
        with allure.step(f'Select in {self.type_of} item with name "{self.name}"'):
            self.locator.select_option(value)