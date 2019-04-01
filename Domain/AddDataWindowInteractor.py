from Data.BD import add_new_entry


def add_data(new_data=[], *args):
    for i in range(len(new_data)):
        if new_data[i] == '':
            new_data[i] = 'Нет данных'
    prepared_new_data = {'country': new_data[0],
                         'province': new_data[1],
                         'points': new_data[3],
                         'taster_name': new_data[5],
                         'variety': new_data[2],
                         'price': new_data[4]}
    add_new_entry(prepared_new_data)
