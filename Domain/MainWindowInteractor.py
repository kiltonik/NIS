from Data.BD import BD
import re


# new_entry_added = False


class MainWindowInteractor(object):
    __instance = None
    __new_entry_added = False
    __BD = BD.inst()

    @staticmethod
    def inst():
        if MainWindowInteractor.__instance is None:
            MainWindowInteractor.__instance = MainWindowInteractor()
        return MainWindowInteractor.__instance

    def __init__(self):
        print('works')

    @staticmethod
    def set_new_entry_added_true():
        MainWindowInteractor.__new_entry_added = True

    @staticmethod
    def set_new_entry_added_false():
        MainWindowInteractor.__new_entry_added = False

    @staticmethod
    def check_new_entry_added_status():
        return MainWindowInteractor.__new_entry_added

    @staticmethod
    def provide_data_for_table():
        data = MainWindowInteractor.__BD.prepared_data()
        final_data = {}
        # keys = []
        for i in list(data.keys()):
            if data[i]['Price'] == data[i]['Price']:
                final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                      for j in list(data[i].items())])
                # year = re.search('\d{4}', final_data[i]['Name'])
                # try:
                #     final_data[i]['Year'] = year.group(0)
                # except AttributeError:
                #     final_data[i]['Year'] = 'Нет данных'

        return final_data

    @staticmethod
    def provide_last_entry():
        data = MainWindowInteractor.__BD.prepared_data()
        last_entry = data[list(data.keys())[-1]]
        last_entry_id = data.keys()[-1]
        return last_entry, last_entry_id

