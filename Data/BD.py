
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
    """
    Синглтон отвечающий за работу базы данных
    Автор Вальков М.Д. БИВ185
    """
    __instance = None
    __wine_data = None
    __province_data = None
    __country__data = None
    f = open(os.path.dirname(os.path.realpath(__file__))[:-4]+'Params.txt', 'r')
    data = f.read().split('\n')
    __country_path, __province_path, __wine_path = data[0], data[1], data[2]

    @staticmethod
    def inst():
        """
        Реализует сиглтон поведение класса
        :return: обьект класса BD
        Автор Вальков М.Д. БИВ185
        """
        if BD.__instance is None:
            BD.__instance = BD()
        return BD.__instance

    def __init__(self):
        print('BD created')

    def provide_wine_data(self):
        """
        Загружает все записи о винах
        :return: словарь с записями
        Авторв Вальков М.Д. БИВ185
        """
        if self.__wine_data is None:
            self.__wine_data = {}
            data_csv = pandas.read_csv(self.__wine_path, encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__wine_data[index] = {
                    'Province id': row['Province id'],
                    'Points': row['Points'],
                    'Taster': row['Taster'],
                    'Variety': row['Variety'],
                    'Year': row['Year'],
                    'Description': row['Description'],
                    'Name': row['Name'],
                    'Price': row['Price']
                }
        return self.__wine_data

    def provide_specific_province(self, province_id):
        """
        Возвращает информацию о конкретной провинции из базы данных
        :param province_id: номер провинции, которую надо вернуть из базы данных
        :return: словарь из одной записи о провинции
        Автора Вальков М.Д.
        """
        if self.__province_data is None:
            self.__province_data = {}
            data_csv = pandas.read_csv(self.__province_path, encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__province_data[index] = {
                    'Province': row['Province'],
                    'Country id': row['Country id']
                }
        return self.__province_data[province_id]

    def provide_all_provinces(self):
        """
        Возвращает данные о всех провинциях из базы данных
        :return: словарь содержащий все провинции
        Автор Кабисов Г.Ч. БИВ185
        """
        data_csv = pandas.read_csv(self.__province_path, encoding='utf-8')
        return list(data_csv['Province'])

    def provide_specific_country(self, country_id):
        """
        Возвращает данные о конкретной стране из базы данных
        :param country_id: номер искомой страны
        :return: строку содержащую название конкретной страны
        Автор Кабисов Г.Ч. БИВ185
        """
        if self.__country__data is None:
            self.__country__data = {}
            data_csv = pandas.read_csv(self.__country_path, encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__country__data[index] = row['Countries']
        return self.__country__data[country_id]

    def provide_all_countries(self):
        """
        Возвращает данные обо всех странах из базы данных
        :return: словарь содержащий данные обо всех странах
        Автор Кабисов Г.Ч. БИВ185
        """
        if self.__country__data is None:
            return set(pandas.read_csv(self.__country_path, encoding='utf-8')['countries'])
        else:
            return [i[1] for i in self.__country__data.items()]

    def provide_entry_by_id(self, entry_id):
        if self.__country__data is None:
            self.__country__data = {}
            data_csv = pandas.read_csv(self.__country_path, encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__country__data[index] = row['Countries']
        return self.__wine_data[entry_id]

    def provide_last_entry(self):
        """
        Возвращает последнюю запись о вине
        :return: словарь содержащий последнюю запись о вине
        Автор Вальков М.Д. БИВ185
        """
        if self.__country__data is None:
            self.__country__data = {}
            data_csv = pandas.read_csv(self.__country_path, encoding='utf-8')
            for index, row in data_csv.iterrows():
                self.__country__data[index] = row['Countries']
        last_entry_id = list(self.__wine_data.keys())[-1]
        return self.__wine_data[last_entry_id], last_entry_id

    def add_new_wine_entry(self, new_entry):
        """
        Добавляет запись о вине в базу данных
        :param new_entry: словарь, содержащий информацию о вине
        :return: -
        Автор Кабисов Г.Ч. БИВ185
        """
        last_wine_entry = list(self.__wine_data.keys())[-1] + 1
        self.__wine_data[last_wine_entry] = {'Province id': new_entry['Province id'],
                                             'Points': new_entry['Points'],
                                             'Taster': new_entry['Taster'],
                                             'Variety': new_entry['Variety'],
                                             'Year': new_entry['Year'],
                                             'Description': new_entry['Description'],
                                             'Name': new_entry['Name'],
                                             'Price': new_entry['Price']}
        pandas.read_csv(self.__wine_path, encoding='utf-8')\
            .append(pandas.DataFrame({last_wine_entry: new_entry}).transpose())\
            .drop('Unnamed: 0', axis=1).to_csv(self.__wine_path, encoding='utf-8')

    def add_new_country(self, new_country):
        """
        Добавляет запись о новой стране в базу данных
        :param new_country: строка, содержащая название страны, которую нужно добавить
        :return: -
        Автор Кабисов Г.Ч. БИВ185
        """
        last_country_index = list(self.__country__data.keys())[-1] + 1
        self.__country__data[last_country_index] = new_country
        pandas.read_csv(self.__country_path, encoding='utf-8')\
            .append(pandas.DataFrame({'Countries': {last_country_index: new_country}}, columns=['Countries']))\
            .drop('Unnamed: 0', axis=1).to_csv(self.__wine_path, encoding='utf-8')

    def add_new_province(self, new_province):
        """
        Добавляет запись о новой провинции в базу данных
        :param new_province: словарь, содрежащий информацию о новой провинции
        :return: -
        Автор Кабисов Г.Ч. БИВ185
        """
        last_province_index = list(self.__province_data.keys())[-1] + 1
        self.__province_data[last_province_index] = new_province
        pandas.read_csv(self.__province_path, encoding='utf-8')\
            .append(pandas.DataFrame({last_province_index: new_province}).transpose())\
            .drop('Unnamed: 0', axis=1).to_csv(self.__wine_path, encoding='utf-8')

    def edit_wine_entry(self, entry_id, new_data):
        """
        Изменяет запись о вине из базы данных
        :param entry_id: индекс записи
        :param new_data: новые данные
        :return: -
        Атор Вальков М.Д. БИВ185
        """
        self.__wine_data[entry_id] = new_data
        pandas.DataFrame(self.__wine_data).transpose().to_csv(self.__wine_path, encoding='utf-8')

    def delete_wine_entry(self, entry_id):
        """
        Удаляет запись о вине из базы данных
        :param entry_id: индекс записи
        :return: -
        Автор Вальков М.Д. БИВ185
        """
        del self.__wine_data[entry_id]
        pandas.read_csv(self.__wine_path, encoding='utf-8')\
            .drop(entry_id, axis=0).drop('Unnamed: 0', axis=1).to_csv(self.__wine_path, encoding='utf-8')
