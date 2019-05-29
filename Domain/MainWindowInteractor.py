from Data.BD import BD


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
        print('MainWindowInteractor created')

    def set_new_entry_added_true(self):
        MainWindowInteractor.__new_entry_added = True

    def set_new_entry_added_false(self):
        MainWindowInteractor.__new_entry_added = False

    def check_new_entry_added_status(self):
        return MainWindowInteractor.__new_entry_added

    def provide_data_for_table(self):
        data = MainWindowInteractor.__BD.provide_prepared_data()
        final_data = {}
        for i in list(data.keys()):
            # if data[i]['Price'] == data[i]['Price']:
            final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                  for j in list(data[i].items())])

        return final_data

    def provide_last_entry(self):
        data = self.__BD.provide_prepared_data()
        last_entry = data[list(data.keys())[-1]]
        last_entry_id = list(data.keys())[-1]
        return last_entry, last_entry_id

