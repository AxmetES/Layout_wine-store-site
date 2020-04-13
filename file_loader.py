import pandas as pd


def loader():
    data = pd.read_excel('files/wine.xlsx', force_ascii=False)
    page_data = data.to_dict(orient='records')
    return page_data
