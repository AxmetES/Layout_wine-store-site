from collections import defaultdict
import pandas as pd

import argparse

parser = argparse.ArgumentParser(description='wine information file')
parser.add_argument('directory', type=str, help='Input file directory')
args = parser.parse_args()


def get_load(args):
    data = pd.read_excel(args.directory + '/wine.xlsx', force_ascii=False, na_values=['N/A', 'NA'],
                         keep_default_na=False)
    drinks = data.to_dict(orient='records')

    wines = defaultdict(list)
    for value in drinks:
        key = value['Категория']
        wines[key].append(value)

    return wines


if __name__ == '__main__':
    print(get_load(args=args))
