# -*- coding: utf-8 -*-
# %% 131
import decimal
 
 
print(round(19.345, 2))
 
number = decimal.Decimal(19.345)
result = round(number, 2)
print(result)
 
result = decimal.Decimal(number).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)
print(result)

# %% 132
from fractions import Fraction
 
 
frac = Fraction(13, 15)
print(f'fraction: {frac}')
print(f'numerator: {frac.numerator}')
print(f'denominator: {frac.denominator}')
# %% 133
from fractions import Fraction
 
 
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
 
print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} - {f2} = {f1 - f2}')
print(f'{f1} * {f2} = {f1 * f2}')
print(f'{f1} / {f2} = {f1 / f2}')
#%% 134
from fractions import Fraction
import math
 
 
f1 = Fraction(1, 4)
 
print(f'{f1} ** 2 = {f1 ** 2}')
print(f'{f1} ** 3 = {f1 ** 3}')
print(f'math.sqrt({f1}) = {math.sqrt(f1)}')
print(f'math.sqrt(Fraction({f1}) = {Fraction(math.sqrt(f1))}')
# %% 135
from fractions import Fraction
import math
 
 
pi = Fraction(math.pi)
e = Fraction(math.e)
 
print(f'pi = {pi}')
print(f'e = {e}')
# %% 136
from fractions import Fraction
import math
 
 
pi = Fraction(math.pi)
e = Fraction(math.e)
 
for limit in [10, 100, 1000]:
    print(f'limit: {limit}')
    print(f'\tpi = {pi.limit_denominator(limit)}')
    print(f'\te = {e.limit_denominator(limit)}')

# %% 137
import itertools
 
 
counter = itertools.count()
for i in counter:
    if i > 9:
        break
    print(i)

# %% 138
import itertools
 
 
counter = itertools.count(start=1, step=2)
for i in counter:
    if i > 9:
        break
    print(i)
# %% 139
import itertools
 
 
cycle = itertools.cycle([-1, 0, 1])
results = [next(cycle) for _ in range(15)]
for result in results:
    print(result)
# %% 140
import itertools
 
 
repeat = itertools.repeat('#')
results = [next(repeat) for _ in range(10)]
for result in results:
    print(result)    
