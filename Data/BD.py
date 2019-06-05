
# wine = {1: {'Province id': 1,
#                'Points': 80,
#                'Taster': 'Michael Schachner',
#                'Variety': 'White',
#                'Description': 'This is ripe and fruity, a wine that is smooth while still structured. Firm tannins '
#                               'are filled out with juicy red berry fruits and freshened with acidity. It\'s  already '
#                               'drinkable, although it will certainly be better from 2016',
#                'Name': 'Quinta dos Avidagos 2011 Avidagos Red (Douro)',
#                'Price': 15}}
# province = {1:{'Province': название процинции,
#               'Country id': 1}}
# country = {1: 'France'}

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
        if self.__wine_data is None:
            self.__wine_data = {}
            data_csv = pandas.read_csv(os.getcwd()+'\\Wine info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__wine_data[index] = {
                    'Province id': row['province'],
                    'Points': row['points'],
                    'Taster': row['taster_name'],
                    'Variety': row['variety'],
                    'Year': row['year'],
                    'Description': row['description'],
                    'Name': row['title'],
                    'Price': row['price']
                }
        return self.__wine_data

    def provide_specific_province(self, province_id):
        if self.__province_data is None:
            self.__province_data = {}
            data_csv = pandas.read_csv(os.getcwd()+'\\Province info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__province_data[index] = {
                    'Province': row['province'],
                    'Country id': row['id country']
                }
        return self.__province_data[province_id]

    def provide_all_provinces(self):
        data_csv = pandas.read_csv(os.getcwd() + '\\Province info.csv', encoding='utf-8')
        return list(data_csv['province'])

    def provide_specific_country(self, country_id):
        if self.__country__data is None:
            self.__country__data = {}
            data_csv = pandas.read_csv(os.getcwd()+'\\Country info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__country__data[index] = row['countries']
        return self.__country__data[country_id]

    def provide_all_countries(self):
        if self.__country__data is None:
            return set(pandas.read_csv(os.getcwd() + '\\Country info.csv', encoding='utf-8')['countries'])
        else:
            return [i[1] for i in self.__country__data.items()]

    def provide_entry_by_id(self, entry_id):
        if self.__country__data is None:
            self.__country__data = {}
            data_csv = pandas.read_csv(os.getcwd() + '\\Country info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__country__data[index] = row['countries']
        return self.__wine_data[entry_id]

    def provide_last_entry(self):
        if self.__country__data is None:
            self.__country__data = {}
            data_csv = pandas.read_csv(os.getcwd() + '\\Country info.csv', encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__country__data[index] = row['countries']
        last_entry_id = list(self.__wine_data.keys())[-1]
        return self.__wine_data[last_entry_id], last_entry_id

    def add_new_wine_entry(self, new_entry):
        last_wine_entry = list(self.__wine_data.keys())[-1] + 1
        self.__wine_data[last_wine_entry] = {'Province id': new_entry['province'],
                    'Points': new_entry['points'],
                    'Taster': new_entry['taster_name'],
                    'Variety': new_entry['variety'],
                    'Year': new_entry['year'],
                    'Description': new_entry['description'],
                    'Name': new_entry['title'],
                    'Price': new_entry['price']}
        pandas.read_csv(os.getcwd()+'\\Wine info.csv', encoding='utf-8')\
            .append(pandas.DataFrame({last_wine_entry: new_entry}).transpose())\
            .drop('Unnamed: 0', axis=1).to_csv(os.getcwd()+'\\Wine info.csv', encoding='utf-8')

    def add_new_country(self, new_country):
        last_country_index = list(self.__country__data.keys())[-1] + 1
        self.__country__data[last_country_index] = new_country
        pandas.read_csv(os.getcwd() + '\\Country info.csv', encoding='utf-8')\
            .append(pandas.DataFrame({'countries': {last_country_index: new_country}}, columns=['countries']))\
            .drop('Unnamed: 0', axis=1).to_csv(os.getcwd()+'\\Country info.csv', encoding='utf-8')

    def add_new_province(self, new_province):
        last_province_index = list(self.__province_data.keys())[-1] + 1
        self.__province_data[last_province_index] = new_province
        pandas.read_csv(os.getcwd() + '\\Province info.csv', encoding='utf-8')\
            .append(pandas.DataFrame({last_province_index: new_province}).transpose())\
            .drop('Unnamed: 0', axis=1).to_csv(os.getcwd()+'\\Province info.csv', encoding='utf-8')

    def delete_wine_entry(self, entry_id):
        del self.__wine_data[entry_id]
