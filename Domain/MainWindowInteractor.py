from Data.BD import prepared_data
import re

def provide_data_for_table():
    data = prepared_data()
    final_data = {}
    keys = []
    for i in list(data.keys()):
        if data[i]['Price'] == data[i]['Price']:
            final_data[i] = dict([j if j[1] == j[1] else (j[0], 'Нет данных')
                                  for j in list(data[i].items())])
            year = re.search('\d{4}', final_data[i]['Name'])
            try:
                final_data[i]['Year'] = year.group(0)
            except AttributeError:
                final_data[i]['Year'] = 'Нет данных'

    return final_data


