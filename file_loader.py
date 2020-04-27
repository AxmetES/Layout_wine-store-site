from collections import defaultdict
import pandas as pd
import os

import argparse

parser = argparse.ArgumentParser(description='wine information file')
parser.add_argument('directory', type=str, help='Input file directory')
args = parser.parse_args()
directory = args.directory


def get_load(file_directory):
    data = pd.read_excel(os.path.join(file_directory, 'wine.xlsx'), force_ascii=False, na_values=['N/A', 'NA'],
                         keep_default_na=False)
    drinks = data.to_dict(orient='records')

    wines = defaultdict(list)
    for drink in drinks:
        key = drink['Категория']
        wines[key].append(drink)
    return wines


if __name__ == '__main__':
    get_load(directory)
