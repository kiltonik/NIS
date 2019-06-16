import tkinter as tk
from tkinter import ttk
from Domain.MainWindowInteractor import MainWindowInteractor
from Presentation.AddDataWindow import AddDataWindow
from Presentation.TableItemInfoWindow import TableItemInfoWindow
from Presentation.SeacrhEntryWindow import SearchEntryWindow
from Presentation.ExportBDWindow import ExportBDWindow
from Presentation.GraphicWindow import GraphicWindow
from Presentation.SortingParamsWindow import SortingParamsWindow


class MainWindow(tk.Frame):
    """
    Класс для создания основного окна программы
    __interactor - обьект класса MainWindowInteractor
    Автор Вальков М.Д. БИВ185
    """
    __interactor = MainWindowInteractor.inst()

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.init_main_window()

    def open_add_data_window(self, table):
        """
        Окрывает окно добавления записи. Добавляет запись в таблицу, в случае если пользователь создал верную запись
        :param table: виджет TreeView созданный при инициализации окна
        :return: -
        Автор Вальков М.Д. БИВ185
        """
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
                             int(last_entry['Year']),
                             last_entry['Points'],
                             last_entry['Price'],
                             last_entry['Taster']])

    def open_table_item_info(self, table):
        """
        Открывает окно подробной информации о записи в таблице. Изменяет/удаляет запись в таблице,
         если пользователь изменил или удалил её после открытия этого окна
        :param table: виджет TreeView созданный при инициализации окна
        :return: -
        Автор Вальков М.Д. БИВ185
        """
        child_window = TableItemInfoWindow(table.selection())
        child_window.wait_window()
        if self.__interactor.check_entry_deleted_status() is not None:
            table.delete(table.selection())
            self.__interactor.set_entry_deleted_none()
        if self.__interactor.check_entry_edited_status() is not None:
            table.item(table.selection(), values=self.__interactor.check_entry_edited_status()[0])
            self.__interactor.set_entry_edited_none()

    def open_search_entry_window(self, table):
        """
        Открывает окно поиска записи. Изменяет/удалет запись, если пользователь изменил или удалил запись,
        в результате поиска записи
        :param table: виджет TreeView созданный при инициализации окна
        :return: -
        Автор Вальков М.Д. БИВ185
        """
        SearchEntryWindow().wait_window()
        if self.__interactor.check_entry_deleted_status() is not None:
            index = self.__interactor.check_entry_deleted_status()
            if int(index, 16) < 16:
                index = 'I00'+str(index)
            elif int(index, 16) < 256:
                index = 'I0'+str(index)
            else:
                index = 'I'+str(index)
            table.delete(self.__interactor.check_entry_deleted_status())
            self.__interactor.set_entry_deleted_none()
        entry_edited_status = self.__interactor.check_entry_edited_status()
        if entry_edited_status is not None:
            index = entry_edited_status[1][2:]
            if int(index, 16) < 16:
                index = 'I00'+str(index)
            elif int(index, 16) < 256:
                index = 'I0'+str(index)
            else:
                index = 'I'+str(index)
            table.item(index, values=entry_edited_status)
            self.__interactor.set_entry_edited_none()



    def init_main_window(self):
        """
        Инициирует основное окно программы
        :return: -
        Автор Вальков М.Д. БИВ185
        """
        tool_bar = tk.Menu(self.root)
        self.root.config(menu=tool_bar)

        db_bar = tk.Menu(tool_bar)
        db_bar.add_command(label='Добавить запись', command=lambda: self.open_add_data_window(table))
        db_bar.add_command(label='Найти запись', command=lambda: self.open_search_entry_window(table))
        db_bar.add_command(label='Выгрузить базу данных', command=lambda:ExportBDWindow())
        tool_bar.add_command(label='Отчёты', command=lambda: GraphicWindow())
        tool_bar.add_command(label='Сортировка', command=lambda: SortingParamsWindow())

        tool_bar.add_cascade(label='База данных', menu=db_bar)
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

        table.bind("<Double-1>", lambda event: self.open_table_item_info(table))

        y_scrollbar_for_table.config(command=table.yview)

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
