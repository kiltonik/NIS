import tkinter as tk
from Data.BD import BD
import re


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

    def get_sort_data(self, value_to_search):
        """
        Создает словарь, отсортированный по нужным критериям
        return: словарь с отсортированными данными, готовыми для отображения
        params: value_to_search - данные, вводимые пользователем
        Автор: Соловьев М.М.
        """
        for i in value_to_search.keys():
            if i in ('Points', 'Year') and value_to_search[i] != '':
                value_to_search[i] = int(value_to_search[i])
            elif i == 'Price' and value_to_search[i] != '':
                value_to_search[i] = float(value_to_search[i])
            else:
                try:
                    value_to_search[i] = value_to_search[i][:re.search('\n', value_to_search[i]).start()]
                except AttributeError:
                    value_to_search[i]
        # if value_to_search == 'Страна'
        sorted_data = {}
        data = self.__BD.provide_wine_data()
        final_data = {}
        for i in list(data.keys()):
            final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                  for j in list(data[i].items())])

            if final_data[i]['Province id'] != 'Нет данных':
                province_data = self.__BD.provide_specific_province(int(final_data[i]['Province id']))
                final_data[i]['Province'] = province_data['Province']
                final_data[i]['Country'] = self.__BD.provide_specific_country(
                    int(province_data['Country id']))

            if final_data[i]['Year'] != 'Нет данных':
                final_data[i]['Year'] = int(final_data[i]['Year'])
        j = 0
        for i in list(final_data.keys()):
            k = 0
            flag = True
            for k in value_to_search.keys():
                if final_data[i][k] != value_to_search[k]  and value_to_search[k] != '' and \
                        value_to_search[k] != '\n':
                    flag = False
                    break
            # while k < len(value_to_search.keys()) and flag:
            #     if list(final_data[i].values())[k] != value_to_search[k] and value_to_search[k] != '' and \
            #             value_to_search[k] != '\n':
            #         flag = False
            #     k += 1
            if flag:
                sorted_data[j] = final_data[i]
                j += 1

        return sorted_data
