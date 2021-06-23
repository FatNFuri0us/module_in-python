# -*- coding: utf-8 -*-
# %% 151
import itertools
import string
 
 
results = itertools.islice(string.ascii_lowercase, 0, None)
print(list(results))
# %% 152
import itertools
import string
 
 
results = itertools.islice(string.ascii_lowercase, 0, None, 3)
print(list(results))
# %% 153
import itertools
 
 
stocks = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Adidas', 'Audi', 'Siemens']
stocks_flag = [name.startswith('A') for name in stocks]
 
results = itertools.compress(stocks, stocks_flag)
for result in results:
    print(result)
# %% 154
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
 
results = itertools.filterfalse(lambda price: price >= 1500, tesla['Close'].values())
for result in results:
    print(result)
# %% 155
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
 
results = itertools.takewhile(lambda price: price <= 1600, tesla['Close'].values())
for result in results:
    print(result)
# %% 156
import itertools
 
 
stream1 = [0.5, 9.9, 8.53, 4.6, 5.58, 7.07, None, 4.5, 3.61, 9.31]
stream2 = [3.75, 9.51, 7.32, None, 1.56, 1.56, 0.58, 8.66, 6.01, 7.08]
 
results = itertools.chain(itertools.takewhile(bool, stream1), itertools.takewhile(bool, stream2))
for result in results:
    print(result)
# %% 157
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
 
results = itertools.dropwhile(lambda price: price <= 1500, tesla['Close'].values())
for result in results:
    print(result)
# %% 158
eurusd = [1.18425, 1.17928, 1.17211, 1.17505, 1.16421, 1.15958]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]
 
for rate, revenue in zip(eurusd, revenues):
    print(rate, revenue)
# %% 159
eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]
 
for rate, revenue in zip(eurusd, revenues):
    print(rate, revenue)
# %% 160
import itertools
 
 
eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]
 
for rate, revenue in itertools.zip_longest(eurusd, revenues):
    print(rate, revenue)    

    
