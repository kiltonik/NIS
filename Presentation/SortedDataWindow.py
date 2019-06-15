import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from Domain.SearchTypeWindowInteractor import SearchTypeWindowInteractor
from Data.BD import BD


class SortedDataWindow(tk.Toplevel):
    """
        Класс отвечающий за создание окна отсортированных записей записей
        Автор: Соловьев М.М. БИВ185
    """
    def __init__(self, sort_by, value_to_search):
        super().__init__()
        self.sort_by = sort_by
        self.value_to_search = value_to_search
        self.resizable(False, False)
        self.grab_set()
        self.sorted_data = SearchTypeWindowInteractor.get_sort_data(self, self.sort_by, self.value_to_search)
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
    #qq

        for i in list(self.sorted_data.keys()):
            table.insert(parent='',
                         index=i,
                         values=[self.sorted_data[i]['Country'],
                                     self.sorted_data[i]['Province'],
                                     self.sorted_data[i]['Variety'],
                                     self.sorted_data[i]['Year'],
                                     self.sorted_data[i]['Points'],
                                     self.sorted_data[i]['Price'],
                                     self.sorted_data[i]['Taster']])

