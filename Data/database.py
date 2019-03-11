'''
Скрипт для создания базы данных
'''

#
# def database():

# catalog = {1: {'Country': 'Itally',
#                'Province': 'Rosso',
#                'Points': 80,
#                'Taster': 'Michael Schachner',
#                'Variety': 'White',
#                'Price': 15}}
import pandas
from tqdm import tqdm


a = pandas.read_csv('D:\\Univer\\NIS\\winemag-data-130k-v2.csv')
a = a.drop(['region_1', 'region_2', 'taster_twitter_handle', 'winery'], axis=1)
data = {}

for index, row in tqdm(a.iterrows()):
    data[row['Unnamed: 0']] = {
        'Country': row['country'],
        'Province': row['province'],
        'Points': row['points'],
        'Taster': row['taster_name'],
        'Variety': row['variety'],
        'Price': row['price'],
    }
print(len(data))