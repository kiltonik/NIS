from Data.BD import BD
from Domain.MainWindowInteractor import MainWindowInteractor


class BDWindowsInteractor:
    __instance = None
    __BD = BD.inst()
    __MainWindowInteractor = MainWindowInteractor.inst()

    def __init__(self):
        print('BDWindowsInteractor created')

    @staticmethod
    def inst():
        if BDWindowsInteractor.__instance is None:
            BDWindowsInteractor.__instance = BDWindowsInteractor()
        return BDWindowsInteractor.__instance

    def add_entry(self, new_data):
        for i in range(len(new_data)):
            if new_data[i] == '':
                new_data[i] = 'Нет данных'
        prepared_new_data = {'country': new_data[0],
                             'province': new_data[1],
                             'points': new_data[4],
                             'year': new_data[3],
                             'taster_name': new_data[6],
                             'variety': new_data[2],
                             'price': new_data[5]}
        self.__BD.add_new_entry(prepared_new_data)
        self.__MainWindowInteractor.set_new_entry_added_true()

    def provide_certain_entry(self, entry_id):
        return dict([j if j[1] == j[1] else (j[0], 'Нет данных') for j in
                     list(self.__BD.provide_entry_by_id(int(list(entry_id)[0][1:], 16)-1).items())])

