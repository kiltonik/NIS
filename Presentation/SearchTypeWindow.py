import tkinter as tk
from tkinter import StringVar
from Data.BD import BD
from Presentation.SortedDataWindow import SortedDataWindow


class SearchTypeWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.init_search_type_window()

    def init_search_type_window(self):
        #TODO при первом открытии окна - все radiobuttons активные; при последующем - сохраняется предыдущее значение
        sort_by = StringVar()
        sort_by = 'Country'
        value_to_search = tk.Entry(self)
        value_to_search.grid(row=0, column=0, sticky='w', padx=3, pady=3)

        country_radio_button = tk.Radiobutton(self, text='Страна', variable=sort_by, value='Country')
        country_radio_button.grid(row=1, column=0, sticky='w', padx=3, pady=3)
        # country_radio_button.

        province_type_radio_button = tk.Radiobutton(self, text='Провинция', variable=sort_by, value='Provinces')
        province_type_radio_button.grid(row=2, column=0, sticky='w', padx=3, pady=3)

        variety_radio_button = tk.Radiobutton(self, text='Вид', variable=sort_by, value='Species')
        variety_radio_button.grid(row=3, column=0, sticky='w', padx=3, pady=3)

        year_radio_button = tk.Radiobutton(self, text='Год сбора', variable=sort_by, value='Year')
        year_radio_button.grid(row=4, column=0, sticky='w', padx=3, pady=3)

        points_radio_button = tk.Radiobutton(self, text='Оценка', variable=sort_by, value='Value')
        points_radio_button.grid(row=5, column=0, sticky='w', padx=3, pady=3)

        price_radio_button = tk.Radiobutton(self, text='Цена', variable=sort_by, value='Price')
        price_radio_button.grid(row=6, column=0, sticky='w', padx=3, pady=3)

        taster_radio_button = tk.Radiobutton(self, text='Сомелье', variable=sort_by, value='Person')
        taster_radio_button.grid(row=7, column=0, sticky='w', padx=3, pady=3)

        #TODO sortd_by - всегда передает Country, вне зависимости от того, как поставлен radiobutton
        sort_button = tk.Button(self, text='Сортировать', command=lambda: SortedDataWindow(sort_by, value_to_search.get()))
        sort_button.grid(row=8, column=0, sticky='w', padx=3, pady=2)