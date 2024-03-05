import csv
import json
import os
from data import dir_global
from data.dir_global import CSV_PATH


class CVSParser:
    def __init__(self, file_name):
        if not os.path.exists(CSV_PATH):
            os.makedirs(CSV_PATH)
        self.cvs_path = os.path.join(CSV_PATH, file_name)

    def write_in_cvs(self, data_list):
        with open(self.cvs_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data_list)

    def read_from_cvs(self):
        data_list = []
        with open(self.cvs_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.append(row)
        return data_list

    def read_from_cvs_column(self, name_column):
        column_name  = name_column
        column_data = []
        with open(self.cvs_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            column_index = headers.index(column_name)
            for row in reader:
                if row and len(row) > column_index:
                    column_data.append(row[column_index])
        return column_data
