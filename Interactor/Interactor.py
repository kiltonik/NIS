from Data.BD import prepared_data, add_new_entry


def provide_data_for_table():
    data = prepared_data()
    final_data = {}
    for i in list(data.keys()):
        if data[i]['Price'] == data[i]['Price']:
            final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                  for j in list(data[i].items())])

    return final_data


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
