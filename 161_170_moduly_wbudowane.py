# -*- coding: utf-8 -*-
# %% 161
import itertools
 
 
eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]
 
for rate, revenue in itertools.zip_longest(eurusd, revenues, fillvalue=1.17):
    print(rate, revenue)
# %% 162
import itertools
 
 
values = [(44, 7), (57, 6), (10, 3)]
 
for val in itertools.starmap(lambda x, y: x % y, values):
    print(val)    
# %% 163
import itertools
 
tesla = {
    'Close': {0: 1499.11,
           1: 1476.49,
           2: 1539.6,
           3: 1417.0,
           4: 1513.07,
           5: 1592.33,
           6: 1568.36,
           7: 1643.0,
           8: 1500.84,
           9: 1500.64},
    'Date': {0: '2020-07-29',
          1: '2020-07-28',
          2: '2020-07-27',
          3: '2020-07-24',
          4: '2020-07-23',
          5: '2020-07-22',
          6: '2020-07-21',
          7: '2020-07-20',
          8: '2020-07-17',
          9: '2020-07-16'},
    'Volume': {0: 9426893,
            1: 15808700,
            2: 16048669,
            3: 19396616,
            4: 24328504,
            5: 14161080,
            6: 16157280,
            7: 17121367,
            8: 9329972,
            9: 14300785}
    }
 
for val in itertools.starmap(lambda x, y: round(x / (y / 1000), 6), zip(tesla['Close'].values(), tesla['Volume'].values())):
    print(val)
# %% 164
import itertools
 
 
data = [1, 5, 3, 4, 6, 9, 3]
 
grouped_data = itertools.groupby(data, key=lambda x: 'even' if x % 2 == 0 else 'odd')
 
for key, group in grouped_data:
    print(f'{key} -> {list(group)}')
# %% 165
import itertools
 
 
data = [1, 5, 3, 4, 6, 9, 3]
 
func = lambda x: 'even' if x % 2 == 0 else 'odd'
sorted_data = sorted(data, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)
 
for key, group in grouped_data:
    print(f'{key} -> {list(group)}')
# %% 166
import itertools
 
 
fnames = ['01_image.jpg', '02_image.png', '03_image.jpg', '04_image.jpg',
         '05_image.jpg', '06_image.png', '07_image.jpg', '08_image.jpg']
 
func = lambda fname: 'jpg' if fname.endswith('jpg') else 'png'
sorted_data = sorted(fnames, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)
 
for key, group in grouped_data:
    print(f'{key} -> {list(group)}')
# %% 167
import itertools
 
 
fnames = ['01_image.jpg', '02_image.png', '03_image.jpg', '04_image.jpg',
         '05_image.jpg', '06_image.png', '07_image.jpg', '08_image.png',
         '09_image.svg', '10_image.svg', '11_image.jpeg', '12_image.jpeg']
 
func = lambda fname: fname.split('.')[-1]
sorted_data = sorted(fnames, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)
 
for key, group in grouped_data:
    print(f'{key} -> {len(list(group))}')
# %% 168
import itertools
 
 
fnames = ['01_image.jpg', '02_image.png', '03_image.jpg', '04_image.jpg',
         '05_image.jpg', '06_image.png', '07_image.jpg', '08_image.png',
         '09_image.svg', '10_image.svg', '11_image.jpeg', '12_image.jpeg']
 
func = lambda fname: fname.split('.')[-1]
sorted_data = sorted(fnames, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)
 
for key, group in grouped_data:
    print(f'{key} -> {round(100 * len(list(group)) / len(fnames), 2)}%')  
# %% 169
import itertools
 
 
data = [{'user': '0032', 'level': 70},
        {'user': '0034', 'level': 74},
        {'user': '0233', 'level': 71},
        {'user': '0532', 'level': 70},
        {'user': '0634', 'level': 74},
        {'user': '0245', 'level': 70},
        {'user': '0235', 'level': 70},
        {'user': '0255', 'level': 71}]
 
func = lambda row: row['level']
sorted_data = sorted(data, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)
 
for key, group in grouped_data:
    print(f'{key} -> {list(group)}')    
# %% 170
import itertools
 
 
data = [{'user': '0032', 'level': 70},
        {'user': '0034', 'level': 74},
        {'user': '0233', 'level': 71},
        {'user': '0532', 'level': 70},
        {'user': '0634', 'level': 74},
        {'user': '0245', 'level': 70},
        {'user': '0235', 'level': 70},
        {'user': '0255', 'level': 71}]
 
func = lambda row: row['level']
sorted_data = sorted(data, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)
 
for key, group in grouped_data:
    print(f'{key} -> ', end='')
    print([user['user'] for user in group])    