
# catalog = {1: {'Country': 'Itally',
#                'Province': 'Rosso',
#                'Points': 80,
#                'Taster': 'Michael Schachner',
#                'Variety': 'White',
#                'Description': 'This is ripe and fruity, a wine that is smooth while still structured. Firm tannins '
#                               'are filled out with juicy red berry fruits and freshened with acidity. It\'s  already '
#                               'drinkable, although it will certainly be better from 2016',
#                'Name': 'Quinta dos Avidagos 2011 Avidagos Red (Douro)',
#                'Price': 15}}
import pandas
import os


class BD(object):
    __instance = None
    __data = {}

    @staticmethod
    def inst():
        if BD.__instance is None:
            BD.__instance = BD()
        return BD.__instance

    def __init__(self):
        print('works')

    @staticmethod
    def prepared_data():
        data_csv = pandas.read_csv(os.getcwd()+'\\data1', encoding='utf-8')
        for index, row in data_csv.iterrows():
            BD.__data[index] = {
                'Country': row['country'],
                'Province': row['province'],
                'Points': row['points'],
                'Taster': row['taster_name'],
                'Variety': row['variety'],
                'Year': row['year'],
                'Description': row['description'],
                'Name': row['title'],
                'Price': row['price']
            }
        return BD.__data

    @staticmethod
    def add_new_entry(a, *args):
        data_csv = pandas.read_csv(os.getcwd()+'\\data1', encoding='utf-8')
        data_csv = data_csv.append(pandas.DataFrame({len(data_csv.index): a})
                                   .transpose()).drop(['Unnamed: 0'], axis=1)
        data_csv.to_csv(os.getcwd()+'\\data1', encoding='utf-8')
