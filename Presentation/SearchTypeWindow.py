import tkinter as tk

class SearchTypeWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.init_search_type_window()

    def init_search_type_window(self):

        value_to_search = tk.Entry(self)
        value_to_search.grid(row=0, column=0, sticky='w', padx=3, pady=3)

        country_radio_button = tk.Radiobutton(self, text='Страна')
        country_radio_button.grid(row=1, column=0, sticky='w', padx=3, pady=3)
        # country_radio_button.

        province_type_radio_button = tk.Radiobutton(self, text='Провинция')
        province_type_radio_button.grid(row=2, column=0, sticky='w', padx=3, pady=3)

        variety_radio_button = tk.Radiobutton(self, text='Вид')
        variety_radio_button.grid(row=3, column=0, sticky='w', padx=3, pady=3)

        year_radio_button = tk.Radiobutton(self, text='Год сбора')
        year_radio_button.grid(row=4, column=0, sticky='w', padx=3, pady=3)

        points_radio_button = tk.Radiobutton(self, text='Оценка')
        points_radio_button.grid(row=5, column=0, sticky='w', padx=3, pady=3)

        price_radio_button = tk.Radiobutton(self, text='Цена')
        price_radio_button.grid(row=5, column=0, sticky='w', padx=3, pady=3)

        taster_radio_button = tk.Radiobutton(self, text='Сомелье')
        taster_radio_button.grid(row=5, column=0, sticky='w', padx=3, pady=3)

