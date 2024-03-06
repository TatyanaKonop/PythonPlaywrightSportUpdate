import allure
from playwright.sync_api import expect
from page_factory.component import Component


class FilterInput(Component):

    @property
    def type_of(self) -> str:
        return 'Filter input'

    def fill_field(self, value: str,  validate_value=False):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            self.locator.fill(value)
            if validate_value:
                self.should_have_value(value)

    def should_have_value(self, value: str):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            expect(self.locator).to_have_value(value)


