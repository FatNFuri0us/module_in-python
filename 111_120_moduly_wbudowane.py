# -*- coding: utf-8 -*-

# %% 111
import random
 
 
random.seed(32)
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']
print(random.sample(population=techs, k=3))

# %% 112
import random
 
 
random.seed(32)
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']
random.shuffle(techs)
print(techs)
#%% 113
import math
 
 
print(f'Pi number: {math.pi}')
print(f'Euler\'s number: {math.e}')
# %% 114
def calculate_seq(n):
    return (1 + (1 / n)) ** n
 
 
sequence = [calculate_seq(i) for i in range(1, 21)]
for item in sequence:
    print(item)
# %% 115
import math
 
 
def calculate_seq(n):
    return (1 + (1 / n)) ** n
 
 
i = 1
while True:
    item = calculate_seq(i)
    if math.isclose(item, math.e, rel_tol=1e-06):
        print(i)
        break
    i += 1

# %% 116

import math
 
 
result = 1 / math.comb(49, 6)
print(f'{100 * result:.10f}%')    
# %% 117
import math
 
 
for k in range(0, 7)[::-1]:
    hits = math.comb(6, k) * math.comb(49 - 6, 6 - k)
    result = hits / math.comb(49, 6)
    print(f'hit: {k} prob: {100 * result:.10f}%')
# %% 118
import math
 
 
fnames = {'01_stream.txt', '02_stream.txt', '03_stream.txt', '04_stream.txt', '05_stream.txt'}
print(math.factorial(len(fnames)))
# %% 119
import math
 
 
pv = 1000
r = 0.04
n = 3
 
fv = pv * math.e ** (r * n)
print(f'fv = {fv:.2f} PLN')
# %% 120
import math
 
 
pv = 1
fv = 2
r = 0.04
n = math.ceil((1 / r) * math.log(fv / pv))
print(f'n = {n}')


    