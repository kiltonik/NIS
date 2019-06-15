import tkinter as tk
from Data.BD import BD


class SearchTypeWindowInteractor:
    __BD = BD.inst()
    __instance = None
    """
        Синглтон для обработки данных получаемых из базы данных и предоставления готовых данных в классы,
        отвечающие за интерфейс программы
        Автор: Соловьев М.М. БИВ185
    """

    @staticmethod
    def inst():
        if SearchTypeWindowInteractor.__instance is None:
            SearchTypeWindowInteractor.__instance = SearchTypeWindowInteractor()
        return SearchTypeWindowInteractor.__instance

    def get_sort_data(self, sort_by, value_to_search):
        """
            Создает словарь, отсортированный по нужным критериям
            return: словарь с отсортированными данными, готовыми для отображения
            params: sort_by - по какому ключу сортировать, value_to_search - данные, вводимые пользователем
            Автор: Соловьев М.М.
        """
        sorted_data = {}
        data = self.__BD.provide_wine_data()
        for i in list(data.keys()):
            if self.__BD.provide_specific_country(self.__BD.provide_specific_province(data[i]['Province id'])
                                                  ['Country id']) == value_to_search:
                sorted_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                       for j in list(data[i].items())])
                # if data[i]['Year'] != 'Нет данных':
                # sorted_data[i]['Year'] = int(sorted_data[i]['Year'])

                if data[i]['Province id'] != 'Нет данных':
                    province_data = self.__BD.provide_specific_province(int(sorted_data[i]['Province id']))
                    sorted_data[i]['Province'] = province_data['Province']
                    sorted_data[i]['Country'] = self.__BD.provide_specific_country(
                        int(province_data['Country id']))

        return sorted_data