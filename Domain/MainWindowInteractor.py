from Data.BD import BD


class MainWindowInteractor(object):
    """
    Синглтон для обработки информации содержащейся в базе данных, а также обработке бизнес логики различных событий
    Автор Вальков М.Д. БИВ185
    """
    __instance = None
    __new_entry_added = False
    __BD = BD.inst()
    __entry_deleted = None
    __entry_edited = None

    @staticmethod
    def inst():
        """
        Реализует синглтон поведение класса
        :return: обьект MainWindowInteractor
        Автор Вальков М.Д. БИВ185
        """
        if MainWindowInteractor.__instance is None:
            MainWindowInteractor.__instance = MainWindowInteractor()
        return MainWindowInteractor.__instance

    def __init__(self):
        print('MainWindowInteractor created')

    def set_new_entry_added_true(self):
        self.__new_entry_added = True

    def set_new_entry_added_false(self):
        self.__new_entry_added = False

    def check_new_entry_added_status(self):
        return self.__new_entry_added

    def set_entry_deleted_none(self):
        self.__entry_deleted = None

    def set_entry_deleted(self, entry_id):
        self.__entry_deleted = entry_id

    def check_entry_deleted_status(self):
        return self.__entry_deleted

    def set_entry_edited_none(self):
        self.__entry_edited = None

    def set_entry_edited(self, entry_id):
        self.__entry_edited = entry_id

    def check_entry_edited_status(self):
        return self.__entry_edited

    def provide_data_for_table(self):
        """
        Получает данные из базы данных и обрабатывает их, чтобы вернуть словарь для отображения в таблице
        :return: словарь с готовыми данными для отображения их в таблице
        Автор Вальков М.Д. БИВ185
        """
        wine_data = self.__BD.provide_wine_data()
        final_data = {}
        for i in list(wine_data.keys()):
            final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                  for j in list(wine_data[i].items())])

            if final_data[i]['Province id'] != 'Нет данных':
                province_data = self.__BD.provide_specific_province(int(final_data[i]['Province id']))
                final_data[i]['Province'] = province_data['Province']
                final_data[i]['Country'] = self.__BD.provide_specific_country(
                    int(province_data['Country id']))

            if final_data[i]['Year'] != 'Нет данных':
                final_data[i]['Year'] = int(final_data[i]['Year'])

        return final_data

    def provide_last_entry(self):
        """
        Получает последнюю запись из базы данных и обрабатывает её, чтобы вернуть словарь для отображения в таблице
        :return: словарь содержащий последнюю запись
        Автор Вальков М.Д. БИВ185
        """
        last_entry, last_entry_id = self.__BD.provide_last_entry()
        last_entry = dict([j if j[1] == j[1] else (j[0], 'Нет данных') for j in list(last_entry.items())])
        if last_entry['Province id'] != 'Нет данных':
            province_data = self.__BD.provide_specific_province(int(last_entry['Province id']))
            last_entry['Province'] = province_data['Province']
            last_entry['Country'] = self.__BD.provide_specific_country(
                province_data['Country id'])

        if last_entry['Year'] != 'Нет данных':
            last_entry['Year'] = int(last_entry['Year'])
        return last_entry, last_entry_id

