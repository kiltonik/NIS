import tkinter as tk
from tkinter import ttk
from Domain.MainWindowInteractor import provide_data_for_table
from Presentation.AddDataWindow import AddDataWindow


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):

        # Верстка главного окна
        add_data_button = tk.Button(self, text='Добавить запись')
        add_data_button.grid(sticky='w', padx=2.5, pady=5)

        delete_data_button = tk.Button(self, text='Удалить запись')
        delete_data_button.grid(column=1, row=0, sticky='w', padx=2.5, pady=5)

        y_scrollbar_for_table = tk.Scrollbar(self, orient='vertical')
        y_scrollbar_for_table.grid(row=1, column=21, rowspan=5, sticky='ns')

        table = ttk.Treeview(self, columns=('Country', 'Province', 'Variety',
                                            'Year', 'Points', 'Price', 'Taster'),
                             show='headings', yscrollcommand=y_scrollbar_for_table.set)

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

        table.grid(row=1, column=0, columnspan=20, rowspan=5, sticky='nsew', padx=2.5)

        y_scrollbar_for_table.config(command=table.yview)

        label_for_sort = tk.Label(self, text='Сортировать по:')
        label_for_sort.grid(row=0, column=2, sticky='w', padx=2.5, pady=5)

        columns_to_sort = ttk.Combobox(self, values=('Страна', 'Провинция',
                                                     'Вид', 'Год сбора', 'Оценка', 'Цена', 'Сомелье'))
        columns_to_sort.grid(row=0, column=3, sticky='w', padx=2.5, pady=5)
        columns_to_sort.current(4)

        type_of_sorting = ttk.Combobox(self, values=('По возрастанию', 'По убыванию'))
        type_of_sorting.grid(row=0, column=4, sticky='w', padx=2.5, pady=5)
        type_of_sorting.current(1)

        # Заполнение таблицы данными из бд
        data = provide_data_for_table()
        for i in list(data.keys()):
            if data[i]['Price'] != 'nan':
                table.insert(parent='', index=i, values=[data[i]['Country'],
                                                         data[i]['Province'],
                                                         data[i]['Variety'],
                                                         data[i]['Year'],
                                                         data[i]['Points'],
                                                         data[i]['Price'],
                                                         data[i]['Taster']])

        # Добавление обработки нажатий
        def add_data(self):
            AddDataWindow()
            data = provide_data_for_table()
            data = data[list(data.keys())[-1]]
            table.insert(parent='', index=list(data.keys())[-1],
                         values=[data['Country'],
                                 data['Province'],
                                 data['Variety'],
                                 data['Year'],
                                 data['Points'],
                                 data['Price'],
                                 data['Taster']])

        add_data_button['command'] = add_data
