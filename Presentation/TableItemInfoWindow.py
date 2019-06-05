import tkinter as tk
from Domain.BDWindowsInteractor import BDWindowsInteractor
from Presentation.EditEntryInfoWindow import EditEntryInfoWindow

class TableItemInfoWindow(tk.Toplevel, object):

    __interactor = BDWindowsInteractor.inst()

    def __init__(self, entry_id):
        super().__init__()
        self.__entry_id = entry_id
        self.resizable(False, False)
        self.grab_set()
        self.init_table_item_info_window()

    def init_table_item_info_window(self):

        country_label = tk.Label(self, text='Страна:')
        country_label.grid(row=0, column=0, sticky='w', padx=3, pady=3)
        country_text_field = tk.Message(self, width=300)
        country_text_field.grid(row=0, column=1, sticky='w', padx=3, pady=3)

        province_label = tk.Label(self, text='Провинция:')
        province_label.grid(row=1, column=0, sticky='w', padx=3, pady=3)
        province_text_field = tk.Message(self, width=300)
        province_text_field.grid(row=1, column=1, sticky='w', padx=3, pady=3)

        variety_label = tk.Label(self, text='Вид:')
        variety_label.grid(row=2, column=0, sticky='w', padx=3, pady=3)
        variety_text_field = tk.Message(self, width=300)
        variety_text_field.grid(row=2, column=1, sticky='w', padx=3, pady=3)

        year_label = tk.Label(self, text='Год сбора:')
        year_label.grid(row=3, column=0, sticky='w', padx=3, pady=3)
        year_text_field = tk.Message(self, width=300)
        year_text_field.grid(row=3, column=1, sticky='w', padx=3, pady=3)

        points_label = tk.Label(self, text='Оценка:')
        points_label.grid(row=4, column=0, sticky='w', padx=3, pady=3)
        points_text_field = tk.Message(self, width=300)
        points_text_field.grid(row=4, column=1, sticky='w', padx=3, pady=3)

        price_label = tk.Label(self, text='Цена, $:')
        price_label.grid(row=5, column=0, sticky='w', padx=3, pady=3)
        price_text_field = tk.Message(self, width=300)
        price_text_field.grid(row=5, column=1, sticky='w', padx=3, pady=3)

        taster_label = tk.Label(self, text='Сомелье:')
        taster_label.grid(row=6, column=0, sticky='w', padx=3, pady=3)
        taster_text_field = tk.Message(self, width=300)
        taster_text_field.grid(row=6, column=1, sticky='w', padx=3, pady=3)

        title_label = tk.Label(self, text='Название:')
        title_label.grid(row=7, column=0, sticky='w', padx=3, pady=3)
        title_text_field = tk.Message(self, width=300)
        title_text_field.grid(row=7, column=1, sticky='w', padx=3, pady=3)

        description_label = tk.Label(self, text='Описание:')
        description_label.grid(row=8, column=0, sticky='w', padx=3, pady=3)
        description_text_field = tk.Message(self, width=300)
        description_text_field.grid(row=8, column=1, sticky='w', padx=3, pady=3)

        edit_button = tk.Button(self, text='Изменить', command=lambda: {EditEntryInfoWindow(self.__entry_id), self.destroy()})
        edit_button.grid(row=9, column=0, sticky='wsn', padx=3, pady=3)

        delete_button = tk.Button(self, text='Удалить')
        delete_button.grid(row=9, column=1, sticky='e', padx=3, pady=3)

        print(self.__entry_id)
        entry = self.__interactor.provide_certain_entry(self.__entry_id)
        country_text_field['text'] = entry['Country']
        province_text_field['text'] = entry['Province']
        variety_text_field['text'] = entry['Variety']
        year_text_field['text'] = str(entry['Year'])
        points_text_field['text'] = str(entry['Points'])
        price_text_field['text'] = str(entry['Price'])
        taster_text_field['text'] = entry['Taster']
        description_text_field['text'] = entry['Description']
        title_text_field['text'] = entry['Name']
