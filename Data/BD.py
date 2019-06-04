
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
    __wine_data = None
    __province_data = None
    __country__data = None

    @staticmethod
    def inst():
        if BD.__instance is None:
            BD.__instance = BD()
        return BD.__instance

    def __init__(self):
        print('BD created')

    def provide_wine_data(self):
        if BD.__wine_data is None:
            BD.__wine_data = {}
            data_csv = pandas.read_csv(os.getcwd()+'\\Wine info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                BD.__wine_data[index] = {
                    'Province id': row['province'],
                    'Points': row['points'],
                    'Taster': row['taster_name'],
                    'Variety': row['variety'],
                    'Year': row['year'],
                    'Description': row['description'],
                    'Name': row['title'],
                    'Price': row['price']
                }
        return BD.__wine_data

    def provide_province_data(self, province_id):
        if BD.__province_data is None:
            BD.__province_data = {}
            data_csv = pandas.read_csv(os.getcwd()+'\\Province info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                BD.__province_data[index] = {
                    'Province': row['province'],
                    'Country id': row['id country']
                }
        return BD.__province_data[province_id]

    def provide_country_data(self, country_id):
        if BD.__country__data is None:
            BD.__country__data = {}
            data_csv = pandas.read_csv(os.getcwd()+'\\Country info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                BD.__country__data[index] = row['countries']
        return BD.__country__data[country_id]

    def provide_entry_by_id(self, entry_id):
        return BD.__wine_data[entry_id]

    def add_new_wine_entry(self, new_entry):
        data_csv = pandas.read_csv(os.getcwd()+'\\Wine info.csv', encoding='utf-8')
        data_csv = data_csv.append(pandas.DataFrame({len(data_csv.index): new_entry})
                                   .transpose(), axis=1)
        data_csv.to_csv(os.getcwd()+'\\Wine info', encoding='utf-8')

