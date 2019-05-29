import tkinter as tk
from Domain.BDWindowsInteractor import BDWindowsInteractor


class EditEntryInfoWindow(tk.Toplevel, object):

    __interactor = BDWindowsInteractor.inst()

    def __init__(self, entry_id):
        super().__init__()
        self.entry_id = entry_id
        self.init_edit_entry_info_window()

    def init_edit_entry_info_window(self):

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

        year_label = tk.Label(self, text='Год сбора:')
        year_label.grid(row=3, column=0, sticky='w', padx=3, pady=3)
        year_entry = tk.Entry(self, width=50)
        year_entry.grid(row=3, column=1, sticky='w', pady=3)

        points_label = tk.Label(self, text='Оценка:')
        points_label.grid(row=4, column=0, sticky='w', padx=3, pady=3)
        points_entry = tk.Entry(self, width=50)
        points_entry.grid(row=4, column=1, sticky='w', pady=3)

        price_label = tk.Label(self, text='Цена, $:')
        price_label.grid(row=5, column=0, sticky='w', padx=3, pady=3)
        price_entry = tk.Entry(self, width=50)
        price_entry.grid(row=5, column=1, sticky='w', pady=3)

        taster_label = tk.Label(self, text='Сомелье:')
        taster_label.grid(row=6, column=0, sticky='w', padx=3, pady=3)
        taster_entry = tk.Entry(self, width=50)
        taster_entry.grid(row=6, column=1, sticky='w', pady=3)

