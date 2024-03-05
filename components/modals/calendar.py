import time

from playwright.sync_api import Page
from page_factory.button import Button
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class Calendar:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator






