import tkinter as tk
from tkinter import ttk
from Domain.SearchTypeWindowInteractor import SearchTypeWindowInteractor


class SortedDataWindow(tk.Toplevel):
    __interactor = SearchTypeWindowInteractor.inst()


    """
        Класс отвечающий за создание окна отсортированных записей записей
        Автор: Соловьев М.М. БИВ185
    """
    def __init__(self, country, province, variety, year, points, price, taster):
        super().__init__()
        self.country = country
        self.province = province
        self.variety = variety
        self.year = year
        self.points = points
        self.price = price
        self.taster = taster
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

        data = self.__interactor.get_sort_data(self.country)
        for i in list(data.keys()):
            if data[i]['Price'] != 'nan':
                table.insert(parent='',
                             index=i,
                             values=[data[i]['Country'],
                                     data[i]['Province'],
                                     data[i]['Variety'],
                                     data[i]['Year'],
                                     data[i]['Points'],
                                     data[i]['Price'],
                                     data[i]['Taster']])

