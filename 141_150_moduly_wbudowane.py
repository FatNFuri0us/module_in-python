# -*- coding: utf-8 -*-
# %% 141
import itertools
 
 
stocks = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Adidas', 'Audi', 'Siemens']
 
results = itertools.combinations(stocks, 2)
for result in results:
    print(result)
# %% 142
import itertools
 
 
stocks = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Adidas', 'Audi', 'Siemens']
 
results = itertools.combinations_with_replacement(stocks, 2)
for result in results:
    print(result)    
# %% 143
import itertools
 
 
names = ['Bob', 'Mark', 'Guido']
results = itertools.permutations(names)
 
for result in results:
    print(result)
# %% 144
import itertools
 
 
letters = list('ABCDEFGH')
numbers = [str(i) for i in range(1, 9)]
chessboard = itertools.product(letters, numbers)
chessboard = [''.join(fields) for fields in chessboard]
print(chessboard)
# %% 145
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
 
results = itertools.accumulate(tesla['Volume'].values())
for result in results:
    print(result) 
# %% 146
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
 
results = itertools.accumulate(tesla['Close'].values(), min)
for result in results:
    print(result)   
# %% 147
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
 
results = itertools.accumulate(tesla['Close'].values(), lambda x, y: (x + y) / 2)
for result in results:
    print(result)
# %% 148
import itertools
 
 
stocks_usa = ['Apple', 'Microsoft', 'Amazon', 'Google']
stocks_de = ['Adidas', 'Audi', 'Siemens']
 
results = itertools.chain(stocks_usa, stocks_de)
for result in results:
    print(result)
# %% 149
import itertools
 
 
stocks_usa = ['Apple', 'Microsoft', 'Amazon', 'Google']
stocks_de = ['Adidas', 'Audi', 'Siemens']
stocks = [stocks_usa, stocks_de]
 
results = itertools.chain.from_iterable(stocks)
for result in results:
    print(result)
# %% 150
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
 
results = itertools.islice(tesla['Date'].values(), 0, None, 2)
for result in results:
    print(result)    















    