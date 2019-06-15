import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from Domain.SearchTypeWindowInteractor import SearchTypeWindowInteractor
from Data.BD import BD
from Domain.MainWindowInteractor import MainWindowInteractor

class SortedDataWindow(tk.Toplevel):
    __interactor = SearchTypeWindowInteractor.inst()
    """
        Класс отвечающий за создание окна отсортированных записей записей
        Автор: Соловьев М.М. БИВ185
    """
    def __init__(self, country, province, variety, year, points, price, taster, title):
        super().__init__()
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

        data = self.__interactor.provide_data_for_table()
        table.insert(parent='',
                             index=1,
                             values=[data[1]['Country'],
                                     data[1]['Province'],
                                     data[1]['Variety'],
                                     data[1]['Year'],
                                     data[1]['Points'],
                                     data[1]['Price'],
                                     data[1]['Taster']])

