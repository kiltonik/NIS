from Data.BD import BD
from Domain.MainWindowInteractor import MainWindowInteractor


class AddDataWindowInteractor(object):
    __instance = None
    __BD = BD.inst()

    @staticmethod
    def inst():
        if AddDataWindowInteractor.__instance is None:
            AddDataWindowInteractor.__instance = AddDataWindowInteractor()
        return AddDataWindowInteractor.__instance

    def __init__(self):
        print('works')

    @staticmethod
    def add_data(new_data, *args):
        for i in range(len(new_data)):
            if new_data[i] == '':
                new_data[i] = 'Нет данных'
        prepared_new_data = {'country': new_data[0],
                             'province': new_data[1],
                             'points': new_data[3],
                             'taster_name': new_data[5],
                             'variety': new_data[2],
                             'price': new_data[4]}
        AddDataWindowInteractor.__BD.add_new_entry(prepared_new_data)
        MainWindowInteractor.set_new_entry_added_true()

