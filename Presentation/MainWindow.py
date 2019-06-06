import tkinter as tk
from tkinter import ttk
from Domain.MainWindowInteractor import MainWindowInteractor
from Presentation.AddDataWindow import AddDataWindow
from Presentation.TableItemInfoWindow import TableItemInfoWindow
from Presentation.SearchTypeWindow import SearchTypeWindow


class MainWindow(tk.Frame):

    __interactor = MainWindowInteractor.inst()

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.init_main_window()

    def open_add_data_window(self, table):
        child_window = AddDataWindow()
        child_window.wait_window()
        if self.__interactor.check_new_entry_added_status():
            print('An entry created')
            last_entry, last_entry_id = self.__interactor.provide_last_entry()
            self.__interactor.set_new_entry_added_false()
            table.insert(parent='',
                         index=last_entry_id,
                         values=[last_entry['Country'],
                             last_entry['Province'],
                             last_entry['Variety'],
                             last_entry['Year'],
                             last_entry['Points'],
                             last_entry['Price'],
                             last_entry['Taster']])

    def open_table_item_info(self, selected_entry):
        print('Item selected')
        child_window = TableItemInfoWindow(selected_entry)
        # print(int(list(table.selection())[0][1:]))

    def init_main_window(self):

        # Верстка главного окна

        tool_bar = tk.Menu(self.root)
        self.root.config(menu=tool_bar)

        db_bar = tk.Menu(tool_bar)
        db_bar.add_command(label='Добавить запись', command=lambda: self.open_add_data_window(table))
        db_bar.add_command(label='Изменить запись')
        db_bar.add_command(label='Удалить запись')
        db_bar.add_command(label='Выгрузить базу данных')

        # sort_bar = tk.Menu(tool_bar)
        # sort_bar.add_command(label='Страна')
        # sort_bar.add_command(label='Провинция')
        # sort_bar.add_command(label='Вид')
        # sort_bar.add_command(label='Год сбора')
        # sort_bar.add_command(label='Оценка')
        # sort_bar.add_command(label='Цена')
        # sort_bar.add_command(label='Сомелье')
        #
        # sort_type_bar = tk.Menu(sort_bar)
        # sort_type_bar.add_command(label='По возрастанию')
        # sort_type_bar.add_command(label='По убыванию')
        # sort_type_bar.add_command(label='В диапозоне')

        tool_bar.add_cascade(label='База данных', menu=db_bar)
        # tool_bar.add_cascade(label='Поиск', menu=search_bar)
        tool_bar.add_command(label='Поиск', command=lambda: SearchTypeWindow())

        y_scrollbar_for_table = tk.Scrollbar(self, orient='vertical')
        y_scrollbar_for_table.grid(row=1,
                                   column=21,
                                   rowspan=5,
                                   sticky='ns')

        table = ttk.Treeview(self, columns=('Country', 'Province', 'Variety',
                                            'Year', 'Points', 'Price', 'Taster'),
                             show='headings',
                             yscrollcommand=y_scrollbar_for_table.set)
        #TODO command=lambda: print(1) - зачем?
        table.heading('Country', text='Страна', command=lambda: print(1))
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
                   padx=2.5,
                   pady=2.5)

        table.bind("<Double-1>", lambda event: self.open_table_item_info(table.selection()))

        y_scrollbar_for_table.config(command=table.yview)

        # label_for_sort = tk.Label(self, text='Сортировать по:')
        # label_for_sort.grid(row=0,
        #                     column=2,
        #                     sticky='w',
        #                     padx=2.5,
        #                     pady=5)
        #
        # columns_to_sort = ttk.Combobox(self, values=('Страна',
        #                                              'Провинция',
        #                                              'Вид',
        #                                              'Год сбора',
        #                                              'Оценка',
        #                                              'Цена',
        #                                              'Сомелье'))
        # columns_to_sort.grid(row=0, column=3, sticky='w', padx=2.5, pady=5)
        # columns_to_sort.current(4)
        #
        # type_of_sorting = ttk.Combobox(self, values=('По возрастанию', 'По убыванию'))
        # type_of_sorting.grid(row=0,
        #                      column=4,
        #                      sticky='w',
        #                      padx=2.5,
        #                      pady=5)
        # type_of_sorting.current(1)

        # Заполнение таблицы данными из бд
        data = self.__interactor.provide_data_for_table()
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

        # Добавление обработки нажатий на элементы таблицы
        # add_data_button['command'] = open_add_data_window
