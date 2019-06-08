import tkinter as tk
from Domain.BDWindowsInteractor import BDWindowsInteractor
from Domain.MainWindowInteractor import MainWindowInteractor


class EditEntryInfoWindow(tk.Toplevel, object):
    """
    Класс отвечающий за окно изменения данных
    Автор Кабисов Г.Ч. БИВ185
    """

    __interactor = BDWindowsInteractor.inst()
    __main_window_interactor = MainWindowInteractor.inst()

    def __init__(self, entry_id):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.entry_id = entry_id
        self.init_edit_entry_info_window()

    def init_edit_entry_info_window(self):
        """
        Инициализирует окно изменения данных
        :return: -
        Автор Кабисов Г.Ч. БИВ185
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

        entry = self.__interactor.provide_certain_entry(self.entry_id)
        country_entry.insert('1.0', entry['Country'])
        province_entry.insert('1.0', entry['Province'])
        variety_entry.insert('1.0', entry['Variety'])
        year_entry.insert(0, int(entry['Year']))
        points_entry.insert(0, entry['Points'])
        price_entry.insert(0, entry['Price'])
        taster_entry.insert('1.0', entry['Taster'])
        title_entry.insert('1.0', entry['Name'])
        description_entry.insert('1.0', entry['Description'])

        ok_button = tk.Button(self, text='Сохранить', command=lambda: {self.__interactor.edit_entry([
            country_entry.get(index1="1.0", index2="end")[:-1],
            province_entry.get(index1="1.0", index2="end")[:-1],
            variety_entry.get(index1="1.0", index2="end")[:-1],
            year_entry.get(),
            points_entry.get(),
            price_entry.get(),
            taster_entry.get(index1="1.0", index2="end")[:-1],
            description_entry.get(index1="1.0", index2="end")[:-1],
            title_entry.get(index1="1.0", index2="end")[:-1],
        ], self.entry_id, True),
            self.__main_window_interactor.set_entry_edited([[country_entry.get(index1="1.0", index2="end")[:-1],
                                                            province_entry.get(index1="1.0", index2="end")[:-1],
                                                            variety_entry.get(index1="1.0", index2="end")[:-1],
                                                            year_entry.get(),
                                                            points_entry.get(),
                                                            price_entry.get(),
                                                            taster_entry.get(index1="1.0", index2="end")[:-1]
                                                             ], self.entry_id]),
            self.destroy()})
        ok_button.grid(row=9, column=0, sticky='w', padx=10, pady=3)

        cancel_button = tk.Button(self, text='Отмена', command=lambda: self.destroy())
        cancel_button.grid(row=9, column=1, sticky='e', padx=10, pady=3)

