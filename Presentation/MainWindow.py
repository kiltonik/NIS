import tkinter as tk
from tkinter import ttk
from Domain.MainWindowInteractor import MainWindowInteractor
from Presentation.AddDataWindow import AddDataWindow
# from Domain.MainWindowInteractor import


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):

        interactor = MainWindowInteractor.inst()

        # Верстка главного окна
        add_data_button = tk.Button(self, text='Добавить запись')
        add_data_button.grid(sticky='w',
                             padx=2.5,
                             pady=5)

        delete_data_button = tk.Button(self, text='Удалить запись')
        delete_data_button.grid(column=1,
                                row=0,
                                sticky='w',
                                padx=2.5,
                                pady=5)

        y_scrollbar_for_table = tk.Scrollbar(self, orient='vertical')
        y_scrollbar_for_table.grid(row=1,
                                   column=21,
                                   rowspan=5,
                                   sticky='ns')

        table = ttk.Treeview(self, columns=('Country', 'Province', 'Variety',
                                            'Year', 'Points', 'Price', 'Taster'),
                             show='headings',
                             yscrollcommand=y_scrollbar_for_table.set)

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

        table.grid(row=1,
                   column=0,
                   columnspan=20,
                   rowspan=5,
                   sticky='nsew',
                   padx=2.5)

        y_scrollbar_for_table.config(command=table.yview)

        label_for_sort = tk.Label(self, text='Сортировать по:')
        label_for_sort.grid(row=0,
                            column=2,
                            sticky='w',
                            padx=2.5,
                            pady=5)

        columns_to_sort = ttk.Combobox(self, values=('Страна',
                                                     'Провинция',
                                                     'Вид',
                                                     'Год сбора',
                                                     'Оценка',
                                                     'Цена',
                                                     'Сомелье'))
        columns_to_sort.grid(row=0, column=3, sticky='w', padx=2.5, pady=5)
        columns_to_sort.current(4)

        type_of_sorting = ttk.Combobox(self, values=('По возрастанию', 'По убыванию'))
        type_of_sorting.grid(row=0,
                             column=4,
                             sticky='w',
                             padx=2.5,
                             pady=5)
        type_of_sorting.current(1)

        # Заполнение таблицы данными из бд
        data = interactor.provide_data_for_table()
        for i in list(data.keys()):
            if data[i]['Price'] != 'nan':
                table.insert(parent='',
                             index=i,
                             values=[data[i]['Country'],
                                     data[i]['Province'],
                                     data[i]['Variety'],
                                     data[i]['Year'],
                                     data[i]['Points'],
                                     data[i]['Price'],
                                     data[i]['Taster']])

        # Добавление обработки нажатий
        def open_add_data_window():
            child_window = AddDataWindow()
            child_window.wait_window()
            if interactor.check_new_entry_added_status():
                print('An entry created')
                last_entry, last_entry_id = interactor.provide_last_entry()
                interactor.set_new_entry_added_false()
                table.insert(parent='',
                             index=last_entry_id,
                             values=[last_entry['Country'],
                                     last_entry['Province'],
                                     last_entry['Variety'],
                                     last_entry['Year'],
                                     last_entry['Points'],
                                     last_entry['Price'],
                                     last_entry['Taster']])
            else:
                print("Entry creation has been canceled")
            # last_entry = provide_last_entry()
            # print(table.exists(last_entry))
            # if not table.exists(last_entry):
            #     print(provide_last_entry())
            #     table.insert(parent='', index=list(last_entry.keys())[-1],
            #                  values=[last_entry['Country'],
            #                          last_entry['Province'],
            #                          last_entry['Variety'],
            #                          last_entry['Year'],
            #                          last_entry['Points'],
            #                          last_entry['Price'],
            #                          last_entry['Taster']])

        add_data_button['command'] = open_add_data_window
