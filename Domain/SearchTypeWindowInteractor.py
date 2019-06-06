import tkinter as tk
from Data.BD import BD


class SearchTypeWindowInteractor:

    def get_sort_data(self, sort_by, value_to_search):
        sorted_data = {}
        data = BD.provide_prepared_data()
        for i in list(data.keys()):
            if data[i]['Price'] != 'nan':
                if data[i][sort_by] == value_to_search:
                    sorted_data[i] = data[i]
        return sorted_data