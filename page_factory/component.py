from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator,  expect




class Component(ABC):
    def __init__(self,  locator: Locator, name: str) -> None:
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'

    def hover_click(self) -> None:
        self.hover()
        self.click()

    def click(self) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.name}"'):
            self.locator.click()

    def should_be_visible(self) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            expect(self.locator).to_be_visible()

    def should_have_text(self, text: str) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            expect(self.locator).to_have_text(text)

    def hover(self) -> None:
        with allure.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            self.locator.hover()

    def send_keys(self, key) -> None:
        with allure.step(f'Press {self.type_of} with name "{self.name}"'):
            self.locator.press(key)
    def get_text(self) -> str:
        with allure.step(f'Retrieve text on {self.type_of} with name "{self.name}"'):
            text = self.locator.inner_text()
            return text