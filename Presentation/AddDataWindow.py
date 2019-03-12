import tkinter as tk
from tkinter import messagebox
import re
from Interactor.Interactor import add_data


class AddDataWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.init_add_data_window()

    def init_add_data_window(self):

        country_label = tk.Label(self, text='Страна:')
        country_label.grid(row=0, column=0, sticky='w', padx=3, pady=3)
        country_entry = tk.Entry(self, width=50)
        country_entry.grid(row=0, column=1, sticky='w', pady=3)

        province_label = tk.Label(self, text='Провинция:')
        province_label.grid(row=1, column=0, sticky='w', padx=3, pady=3)
        province_entry = tk.Entry(self, width=50)
        province_entry.grid(row=1, column=1, sticky='w', pady=3)

        variety_label = tk.Label(self, text='Вид:')
        variety_label.grid(row=2, column=0, sticky='w', padx=3, pady=3)
        variety_entry = tk.Entry(self, width=50)
        variety_entry.grid(row=2, column=1, sticky='w', pady=3)

        points_label = tk.Label(self, text='Оценка:')
        points_label.grid(row=3, column=0, sticky='w', padx=3, pady=3)
        points_entry = tk.Entry(self, width=50)
        points_entry.grid(row=3, column=1, sticky='w', pady=3)

        price_label = tk.Label(self, text='Цена, $:')
        price_label.grid(row=4, column=0, sticky='w', padx=3, pady=3)
        price_entry = tk.Entry(self, width=50)
        price_entry.grid(row=4, column=1, sticky='w', pady=3)

        taster_label = tk.Label(self, text='Сомелье:')
        taster_label.grid(row=5, column=0, sticky='w', padx=3, pady=3)
        taster_entry = tk.Entry(self, width=50)
        taster_entry.grid(row=5, column=1, sticky='w', pady=3)

        ok_button = tk.Button(self, text='Сохранить')
        ok_button.grid(row=6, column=0, sticky='w', padx=10, pady=3)

        cancel_button = tk.Button(self, text='Отмена')
        cancel_button.grid(row=6, column=1, sticky='e', padx=10, pady=3)

        def add_new_data():
            country = country_entry.get()
            province = province_entry.get()
            variety = variety_entry.get()
            points = points_entry.get()
            price = price_entry.get()
            taster = taster_entry.get()

            if re.search('\W', country) is None \
                    and re.search('\d', country) is None \
                    and re.search('\W', province) is None \
                    and re.search('\d', province) is None \
                    and re.search('\W', variety) is None \
                    and re.search('\d', variety) is None \
                    and re.search('\D', points) is None \
                    and re.search('\D', price) is None \
                    and re.search('\W', taster) is None \
                    and re.search('\d', taster) is None:
                print(price)
                add_data([country, province, variety, points, price, taster])
                self.destroy()

            else:
                messagebox.showerror('Ошибка', 'Данные введены неправльно')

        def close_window(event):
            self.destroy()

        ok_button.bind('<Button-1>', (lambda event: add_new_data()))
        cancel_button.bind('<Button-1>', close_window)
