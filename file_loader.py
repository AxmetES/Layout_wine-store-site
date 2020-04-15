import pandas as pd
import collections
import pprint


def loader():
    data = pd.read_excel('files/wine2.xlsx', force_ascii=False, na_values=['N/A', 'NA'], keep_default_na=False)
    page_data = data.to_dict(orient='records')

    wines = {}
    for data in page_data:
        key = data['Категория']
        if key in wines:
            wines[key].append(data)
        else:
            wines[key] = [data]

    for wine in wines:
        for j in wines[wine]:
            print(j['Название'])
    return wines


loader()
