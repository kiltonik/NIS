
# catalog = {1: {'Country': 'Itally',
#                'Province': 'Rosso',
#                'Points': 80,
#                'Taster': 'Michael Schachner',
#                'Variety': 'White',
#                'Name': 'Quinta dos Avidagos 2011 Avidagos Red (Douro)
#                'Price': 15}}
import pandas
import os


def prepared_data():
    data_csv = pandas.read_csv(os.getcwd()+'\\data.csv', encoding='utf-8')
    data = {}
    for index, row in data_csv.iterrows():
        data[index] = {
            'Country': row['country'],
            'Province': row['province'],
            'Points': row['points'],
            'Taster': row['taster_name'],
            'Variety': row['variety'],
            'Description': row['description'],
            'Name': row['title'],
            'Price': row['price']
        }
    return data


def add_new_entry(a = {}, *args):
    data_csv = pandas.read_csv(os.getcwd()+'\\data.csv', encoding='utf-8')
    data_csv = data_csv.append(pandas.DataFrame({len(data_csv.index): a})
                               .transpose()).drop(['Unnamed: 0'], axis=1)
    data_csv.to_csv(os.getcwd()+'\\data.csv', encoding='utf-8')
