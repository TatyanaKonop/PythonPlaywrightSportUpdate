import time

from playwright.sync_api import Page
from page_factory.button import Button
from page_factory.cell import Cell
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title
from utils.api import retrieve_values_from_list_with_dict
from utils.cvs_parser import CVSParser


class Table:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator
        self.header = self.root_locator.locator("//th[@class='header']")
        self.body = self.root_locator.locator("//tbody")
        self.row = self.body.locator("//tr")


    def check_data_from_table_and_filtred_items(self, data_list, column_name):
        list_filtered_items = retrieve_values_from_list_with_dict(data_list)
        list_row = []
        for row in self.row.all():
            list_cell_text = []
            for cell in row.locator("//td").all():
                text_on_cell = Cell(cell, name='table_cell').get_text()
                list_cell_text.append(text_on_cell)
            list_cell_text.pop()
            list_row.append(list_cell_text)
        list_headers = []
        for header in self.header.all():
            text_on_cell = Cell(header, name='table_header').get_text()
            list_headers.append(text_on_cell)

        list_row.insert(0, list_headers)
        csv = CVSParser('table_data_filtered.csv')
        csv.write_in_cvs(list_row)
        data_list = csv.read_from_cvs_column(column_name)
        for row in data_list:
           assert row in list_filtered_items








