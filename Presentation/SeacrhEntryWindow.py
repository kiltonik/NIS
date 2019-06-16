import tkinter as tk
from tkinter import messagebox
import re
from Domain.BDWindowsInteractor import BDWindowsInteractor
from Presentation.TableItemInfoWindow import TableItemInfoWindow


class SearchEntryWindow(tk.Toplevel):
    """
    Класс отвечающий за окно поиска записи
    Автор Вальков М.Д. БИВ185
    """
    __interactor = BDWindowsInteractor.inst()

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.init_search_entry_window()

    def init_search_entry_window(self):
        """
        Инициализирует окно поиска записи
        :return: -
        Автор Вальков М.Д. БИВ185
        """
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

        title_label = tk.Label(self, text='Название')
        title_label.grid(row=7, column=0, sticky='w', padx=3, pady=3)
        title_entry = tk.Text(self, width=50, height=1)
        title_entry.grid(row=7, column=1, sticky='w', padx=3, pady=3)

        description_label = tk.Label(self, text='Описание:')
        description_label.grid(row=8, column=0, sticky='w', padx=3, pady=3)
        description_entry = tk.Text(self, width=50, height=5)
        description_entry.grid(row=8, column=1, sticky='w', padx=3, pady=3)

        search_button = tk.Button(self, text='Найти')
        search_button.grid(row=9, column=0, sticky='we', padx=10, pady=3)

        def search_entry():
            """
            Передает данные в интерактор для поиска записи. Выдает ошибку в случае неправильных данных
            :return: -
            Автор Вальков М.Д. БИВ185
            """
            country = country_entry.get(index1="1.0", index2="end")
            province = province_entry.get(index1="1.0", index2="end")
            variety = variety_entry.get(index1="1.0", index2="end")
            year = year_entry.get()
            points = points_entry.get()
            price = price_entry.get()
            taster = taster_entry.get(index1="1.0", index2="end")
            description = description_entry.get(index1="1.0", index2="end")
            title = title_entry.get(index1="1.0", index2="end")

            if re.search('[^\w\s]', country) is None \
                    and re.search('\d', country) is None \
                    and re.search('[^\w\s]', province) is None \
                    and re.search('\d', province) is None \
                    and re.search('[^\w\s]', variety) is None \
                    and re.search('\d', variety) is None \
                    and re.search('\D', year) is None \
                    and re.search('\D', points) is None \
                    and re.search('[^\d.]', price) is None \
                    and re.search('[^\w\s]', taster) is None \
                    and re.search('\d', taster) is None:
                try:
                    TableItemInfoWindow(self.__interactor.provide_entry_id_in_table([country[:-1], province[:-1],
                                                                                 variety[:-1], year, points,
                                                                                 price, taster[:-1],
                                                                                 description[:-1], title[:-1]]))\
                        .wait_window()
                except ValueError:
                    messagebox.showerror('Ошибка', 'Запись не найдена')
                self.destroy()

            else:
                messagebox.showerror('Ошибка', 'Данные введены неправильно')

        search_button['command'] = search_entry

