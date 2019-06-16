import tkinter as tk
from Data.BD import BD


class SearchTypeWindowInteractor(object):
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

    def get_sort_data(self, country):
        """
            Создает словарь, отсортированный по нужным критериям
            return: словарь с отсортированными данными, готовыми для отображения
            params: sort_by - по какому ключу сортировать, value_to_search - данные, вводимые пользователем
            Автор: Соловьев М.М.
        """
        sorted_data = {}
        data = self.__BD.provide_wine_data()
        print(self.__BD.provide_specific_country(self.__BD.provide_specific_province(data[1]['Province id'])['Country id']))
        for i in list(data.keys()):
            if self.__BD.provide_specific_country(self.__BD.provide_specific_province(data[i]['Province id'])['Country id']) == country:
                sorted_data[i] = data[i]
        return sorted_data
