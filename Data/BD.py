
# catalog = {1: {'Country': 'Itally',
#                'Province': 'Rosso',
#                'Points': 80,
#                'Taster': 'Michael Schachner',
#                'Variety': 'White',
#                'Price': 15}}
import pandas
import os


def prepared_data():
    data_csv = pandas.read_csv(os.getcwd()+'\\data.csv', encoding='utf-8')
    data = {}
    for index, row in data_csv.iterrows():
        data[row['Unnamed: 0']] = {
            'Country': row['country'],
            'Province': row['province'],
            'Points': row['points'],
            'Taster': row['taster_name'],
            'Variety': row['variety'],
            'Price': row['price'],
        }
    return data

