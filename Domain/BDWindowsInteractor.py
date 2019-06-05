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
        number_clear_fields = 0
        for i in range(len(new_data)):
            if new_data[i] == '\n' or new_data[i] == 'Нет данных' or new_data[i] == '':
                new_data[i] = None
                number_clear_fields += 1
        if number_clear_fields < len(new_data):
            if new_data[0] not in set(self.__BD.provide_all_countries()):
                self.__BD.add_new_country(new_data[0])
            all_provinces = self.__BD.provide_all_provinces()
            if new_data[1] not in set(all_provinces):
                self.__BD.add_new_province({'province': new_data[1],
                                            'id country': list(self.__BD.provide_all_countries()).index(new_data[0])+3})
            print(self.__BD.provide_all_countries())
            all_provinces = self.__BD.provide_all_provinces()
            prepared_new_data = {'province': all_provinces.index(new_data[1]),
                                     'description': new_data[7],
                                     'points': new_data[4],
                                     'year': new_data[3],
                                     'taster_name': new_data[6],
                                     'variety': new_data[2],
                                     'price': new_data[5],
                                     'title':new_data[8]}

            self.__BD.add_new_wine_entry(prepared_new_data)
            self.__MainWindowInteractor.set_new_entry_added_true()

    def provide_certain_entry(self, entry_id):
        certain_entry = dict([j if j[1] == j[1] else (j[0], 'Нет данных') for j in
                     list(self.__BD.provide_entry_by_id(int(list(entry_id)[0][1:], 16)-1).items())])
        if certain_entry['Province id'] != 'Нет данных':
            province_data = self.__BD.provide_specific_province(int(certain_entry['Province id']))
            certain_entry['Province'] = province_data['Province']
            certain_entry['Country'] = self.__BD.provide_specific_country(
                province_data['Country id'])
        return certain_entry
