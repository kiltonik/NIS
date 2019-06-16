import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from Domain.SearchTypeWindowInteractor import SearchTypeWindowInteractor
from Data.BD import BD
from Presentation.SortedDataWindow import SortedDataWindow

class SortingParamsWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.init_sorting_params_window()

    def init_sorting_params_window(self):
        country_label = tk.Label(self, text='Страна:')
        country_label.grid(row=0, column=0, sticky='w', padx=3, pady=3)
        country_entry = tk.Text(self, width=50, height=1)
        country_entry.grid(row=0, column=1, sticky='w', padx=3, pady=3)

        province_label = tk.Label(self, text='Провинция:')
        province_label.grid(row=1, column=0, sticky='w', padx=3, pady=3)
        province_entry = tk.Text(self, width=50, height=1)
        province_entry.grid(row=1, column=1, sticky='w', padx=3, pady=3)

        variety_label = tk.Label(self, text='Вид:')
        variety_label.grid(row=2, column=0, sticky='w', padx=3, pady=3)
        variety_entry = tk.Text(self, width=50, height=1)
        variety_entry.grid(row=2, column=1, sticky='w', padx=3, pady=3)

        year_label = tk.Label(self, text='Год сбора:')
        year_label.grid(row=3, column=0, sticky='w', padx=3, pady=3)
        year_entry = tk.Entry(self, width=67)
        year_entry.grid(row=3, column=1, sticky='w', padx=3, pady=3)

        points_label = tk.Label(self, text='Оценка:')
        points_label.grid(row=4, column=0, sticky='w', padx=3, pady=3)
        points_entry = tk.Entry(self, width=67)
        points_entry.grid(row=4, column=1, sticky='w', padx=3, pady=3)

        price_label = tk.Label(self, text='Цена, $:')
        price_label.grid(row=5, column=0, sticky='w', padx=3, pady=3)
        price_entry = tk.Entry(self, width=67)
        price_entry.grid(row=5, column=1, sticky='w', padx=3, pady=3)

        taster_label = tk.Label(self, text='Сомелье:')
        taster_label.grid(row=6, column=0, sticky='w', padx=3, pady=3)
        taster_entry = tk.Text(self, width=50, height=1)
        taster_entry.grid(row=6, column=1, sticky='w', padx=3, pady=3)


        sort_button = tk.Button(self, text='Отсортировать', command=lambda: SortedDataWindow(country_entry.get(index1="1.0", index2="end"),
                                                                                             province_entry.get(index1="1.0", index2="end"),
                                                                                             variety_entry.get(index1="1.0", index2="end"),
                                                                                             year_entry.get(),
                                                                                             points_entry.get(),
                                                                                             price_entry.get(),
                                                                                             taster_entry.get(index1="1.0",index2="end")))



        sort_button.grid(row=7, column=0, sticky='w', padx=10, pady=3)

        cancel_button = tk.Button(self, text='Отмена', command=lambda: self.destroy())
        cancel_button.grid(row=7, column=1, sticky='e', padx=10, pady=3)

