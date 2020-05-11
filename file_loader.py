from collections import defaultdict
import pandas as pd
import os

import argparse


def get_dir():
    parser = argparse.ArgumentParser(description='wine information file')
    parser.add_argument('directory', type=str, help='Input file directory')
    args = parser.parse_args()
    return args.directory


def get_load(file_directory):
    data = pd.read_excel(os.path.join(file_directory, 'wine.xlsx'), force_ascii=False, na_values=['N/A', 'NA'],
                         keep_default_na=False)
    drinks = data.to_dict(orient='records')

    drinks_on_page = defaultdict(list)
    for drink in drinks:
        category = drink['Категория']
        drinks_on_page[category].append(drink)
    return drinks_on_page


if __name__ == '__main__':
    get_dir()
    get_load()
