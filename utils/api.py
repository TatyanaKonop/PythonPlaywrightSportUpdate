import csv
import re


def extract_number(row_price: str):
    price = round(float(re.search(r'\b\d+\.\d+\b', row_price)[0]), 2)
    return price


def find_sum_elements(row_elements):
    sum = 0
    for i in row_elements:
        int_price = round(float(extract_number(i.text_content())), 2)
        sum += int_price
    return sum


def retrieve_values_from_list_with_dict(data_list):
    list_values = []
    for i in data_list:
        for value in i.values():
            list_values.extend(value)
    return list_values


