from Data.BD import prepared_data


def provide_data_for_table():
    data = prepared_data()
    final_data = {}
    for i in list(data.keys()):
        if data[i]['Price'] == data[i]['Price']:
            final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                  for j in list(data[i].items())])

    return final_data
