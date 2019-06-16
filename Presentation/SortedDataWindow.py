import tkinter as tk
from tkinter import ttk
from Domain.SearchTypeWindowInteractor import SearchTypeWindowInteractor
from Data.BD import BD

class SortedDataWindow(tk.Toplevel):

    __interactor = SearchTypeWindowInteractor.inst()


    """
        Класс отвечающий за создание окна отсортированных записей записей
        Автор: Соловьев М.М. БИВ185
    """
    def __init__(self, values_to_search):
        super().__init__()
        self.values_to_search = values_to_search
        self.init_sorted_data_window()

    def init_sorted_data_window(self):
        """
                Инициирует  окно отсортированных данных
                :return: -
                Соловеьв М.М. БИВ185
        """
        y_scrollbar_for_table = tk.Scrollbar(self, orient='vertical')
        y_scrollbar_for_table.grid(row=1,
                                   column=21,
                                   rowspan=5,
                                   sticky='ns')
        table = ttk.Treeview(self, columns=('Country', 'Province', 'Variety',
                                            'Year', 'Points', 'Price', 'Taster'),
                             show='headings',
                             yscrollcommand=y_scrollbar_for_table.set)
        table.heading('Country', text='Страна')
        table.heading('Province', text='Провинция')
        table.heading('Variety', text='Вид')
        table.heading('Year', text='Год сбора')
        table.heading('Points', text='Оценка')
        table.heading('Price', text='Цена, $')
        table.heading('Taster', text='Сомелье')

        table.column('Country', width=100, anchor=tk.CENTER)
        table.column('Province', width=100, anchor=tk.CENTER)
        table.column('Variety', width=100, anchor=tk.CENTER)
        table.column('Year', width=70, anchor=tk.CENTER)
        table.column('Points', width=70, anchor=tk.CENTER)
        table.column('Price', width=70, anchor=tk.CENTER)
        table.column('Taster', width=100, anchor=tk.CENTER)

        table.grid(row=1,
                   column=0,
                   columnspan=20,
                   rowspan=5,
                   sticky='nsew',
                   padx=2.5,
                   pady=2.5)
        y_scrollbar_for_table.config(command=table.yview)

        sort_data = self.__interactor.get_sort_data(self.values_to_search)

        for i in list(sort_data.keys()):
            if sort_data[i]['Price'] != 'nan':
                table.insert(parent='',
                             index=i,
                             values=[sort_data[i]['Country'],
                                     sort_data[i]['Province'],
                                     sort_data[i]['Variety'],
                                     sort_data[i]['Year'],
                                     sort_data[i]['Points'],
                                     sort_data[i]['Price'],
                                     sort_data[i]['Taster']])

