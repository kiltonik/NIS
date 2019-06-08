import tkinter as tk
from Data.BD import BD


class SearchTypeWindowInteractor:
    """
        Синглтон для обработки данных получаемых из базы данных и предоставления готовых данных в классы,
        отвечающие за интерфейс программы
        Автор: Соловьев М.М. БИВ185
    """
    def get_sort_data(self, sort_by, value_to_search):
        """
            Создает словарь, отсортированный по нужным критериям
            return: словарь с отсортированными данными, готовыми для отображения
            params: sort_by - по какому ключу сортировать, value_to_search - данные, вводимые пользователем
            Автор: Соловьев М.М.
        """
        sorted_data = {}
        data = BD.provide_prepared_data()
        for i in list(data.keys()):
            if data[i]['Price'] != 'nan':
                if data[i][sort_by] == value_to_search:
                    sorted_data[i] = data[i]
        return sorted_data