import allure

from page_factory.table_item import TableItem
from utils.api import retrieve_values_from_list_with_dict
from utils.cvs_parser import CVSParser


class Table:
    def __init__(self, root_locator) -> None:
        self.root_locator = root_locator
        self.header = self.root_locator.locator("//th[@class='header']")
        self.body = self.root_locator.locator("//tbody")
        self.row = self.body.locator("//tr")
        self.csv = CVSParser('table_data_filtered.csv')

    def parce_data_in_cell_table(self):  # Parsing data from cell
        list_row = []
        for row in self.row.all():
            list_cell_text = []
            for cell in row.locator("//td").all():
                text_on_cell = TableItem(cell, name='cell').get_text()
                list_cell_text.append(text_on_cell)
            list_cell_text.pop()  # Delete last header (icon)
            list_row.append(list_cell_text)
        return list_row

    def parce_data_header_table(self):  # Parsing data from headers
        list_headers = []
        for header in self.header.all():
            text_on_cell = TableItem(header, name='headers').get_text()
            list_headers.append(text_on_cell)
        return list_headers

    def check_data_from_table_with_filtered_item(self, data_list, column_name):
        list_filtered_items = retrieve_values_from_list_with_dict(data_list)  # Retrieve  values of checkbox items from data_list
        list_headers = self.parce_data_header_table()
        list_row = self.parce_data_in_cell_table()
        list_row.insert(0, list_headers)  # Input headers for creation csv file
        self.csv.write_in_cvs(list_row)
        data_list = self.csv.read_from_cvs_column(column_name)  # Read data from csv file data for column name
        with allure.step(f'Checking that data in column {column_name} present in filtered data'):
            for row in data_list:
                assert row in list_filtered_items
