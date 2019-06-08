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
                self.__BD.add_new_province({'Province': new_data[1],
                                            'Country id': self.__BD.provide_all_countries().index(new_data[0])})
            all_provinces = self.__BD.provide_all_provinces()
            prepared_new_data = {'Province id': all_provinces.index(new_data[1]),
                                 'Description': new_data[7],
                                 'Points': new_data[4],
                                 'Year': new_data[3],
                                 'Taster': new_data[6],
                                 'Variety': new_data[2],
                                 'Price': new_data[5],
                                 'Name': new_data[8]}

            self.__BD.add_new_wine_entry(prepared_new_data)
            self.__MainWindowInteractor.set_new_entry_added_true()

    def provide_certain_entry(self, entry_id):

        if list(entry_id)[0][1:] == '':
            entry_id = [entry_id[1:]]
        certain_entry = dict([j if j[1] == j[1] else (j[0], 'Нет данных') for j in
                              list(self.__BD.provide_entry_by_id(
                                  list(self.__BD.provide_wine_data().keys())[int(list(entry_id)[0][1:], 16)-1])
                                   .items())])
        if certain_entry['Province id'] != 'Нет данных':
            province_data = self.__BD.provide_specific_province(int(certain_entry['Province id']))
            certain_entry['Province'] = province_data['Province']
            certain_entry['Country'] = self.__BD.provide_specific_country(
                province_data['Country id'])
        if certain_entry['Year'] != 'Нет данных':
            certain_entry['Year'] = int(certain_entry['Year'])
        return certain_entry

    def provide_entry_id_in_table(self, entry):
        if entry[3] != 'Нет данных':
            entry[3] = float(entry[3])
        if entry[5] != 'Нет данных':
            entry[5] = float(entry[5])
        if entry[4] != 'Нет данных':
            entry[4] = int(entry[4])
        for i in range(len(entry)):
            if entry[i] == '\n' or entry[i] == 'Нет данных' or entry[i] == '':
                entry[i] = None
        entry = {'Province id': self.__BD.provide_all_provinces().index(entry[1]),
                 'Points': entry[4],
                 'Taster': entry[6],
                 'Variety': entry[2],
                 'Year': entry[3],
                 'Description': entry[7],
                 'Name': entry[8],
                 'Price': entry[5]}
        wine_data = self.__BD.provide_wine_data()
        for i in wine_data:
            if wine_data[i] == entry:
                return hex(i+1)

    def delete_wine_entry(self, entry, index):
        if not index:
            all_wines = self.__BD.provide_wine_data()
            for i in all_wines:
                if all_wines[i] == entry:
                    entry = i
                    break
            self.__BD.delete_wine_entry(i)
        else:
            if list(entry)[0][1:] == '':
                entry = [entry[1:]]
            self.__BD.delete_wine_entry(list(self.__BD.provide_wine_data().keys())[int(list(entry)[0][1:], 16) - 1])

    def edit_entry(self, new_data, entry, index):
        if not index:
            all_wines = self.__BD.provide_wine_data()
            for i in all_wines:
                if all_wines[i] == entry:
                    entry = i
                    break

        else:
            if list(entry)[0][1:] == '':
                entry = [entry[1:]]
            if new_data[0] not in set(self.__BD.provide_all_countries()):
                self.__BD.add_new_country(new_data[0])
            all_provinces = self.__BD.provide_all_provinces()
            if new_data[1] not in set(all_provinces):
                self.__BD.add_new_province({'Province': new_data[1],
                                            'Country id': self.__BD.provide_all_countries().index(new_data[0])})
            all_provinces = self.__BD.provide_all_provinces()
            prepared_new_data = {'Province id': all_provinces.index(new_data[1]),
                                 'Description': new_data[7],
                                 'Points': new_data[4],
                                 'Year': new_data[3],
                                 'Taster': new_data[6],
                                 'Variety': new_data[2],
                                 'Price': new_data[5],
                                 'Name': new_data[8]}
            self.__BD.edit_wine_entry(int(list(entry)[0][1:], 16) - 1, prepared_new_data)
