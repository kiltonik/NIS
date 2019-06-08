import tkinter as tk


class SearchTypeWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.init_search_type_window()

    def init_search_type_window(self):

        value_to_search = tk.Entry(self, width=100)
        value_to_search.grid(row=0, column=0, sticky='w', padx=3, pady=3)

        search_type_value = tk.StringVar()

        country_radio_button = tk.Radiobutton(self, text='Страна', value='Country', variable=search_type_value)
        country_radio_button.grid(row=1, column=0, sticky='w', padx=3, pady=3)

        province_type_radio_button = tk.Radiobutton(self, text='Провинция', value='Province', variable=search_type_value)
        province_type_radio_button.grid(row=2, column=0, sticky='w', padx=3, pady=3)

        variety_radio_button = tk.Radiobutton(self, text='Вид', value='Variety', variable=search_type_value)
        variety_radio_button.grid(row=3, column=0, sticky='w', padx=3, pady=3)


        year_radio_button = tk.Radiobutton(self, text='Год сбора', value='Year', variable=search_type_value)
        year_radio_button.grid(row=4, column=0, sticky='w', padx=3, pady=3)

        points_radio_button = tk.Radiobutton(self, text='Оценка', value='Points', variable=search_type_value)
        points_radio_button.grid(row=5, column=0, sticky='w', padx=3, pady=3)

        price_radio_button = tk.Radiobutton(self, text='Цена', value='Price', variable=search_type_value)
        price_radio_button.grid(row=6, column=0, sticky='w', padx=3, pady=3)

        taster_radio_button = tk.Radiobutton(self, text='Сомелье', value='Taster', variable=search_type_value)
        taster_radio_button.grid(row=7, column=0, sticky='w', padx=3, pady=3)

        search_button = tk.Button(self, text='Найти')
        search_button.grid(row=8, column=0, sticky='we', padx=3, pady=3)

