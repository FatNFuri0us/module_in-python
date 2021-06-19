# -*- coding: utf-8 -*-

# %% 121
import math
import random
from random import random as rand
 
 
random.seed(42)
centroid = (0.5, 0.5)
points = [(rand(), rand()) for i in range(10)]
    
distances = [math.dist(point, centroid) for point in points]
result = min(list(enumerate(distances)), key=lambda item: item[1])
print(result)
# %% 122
import statistics
 
 
data = [59.19, 72.05, 66.82, 81.15, 66.33, 94.87, 99.65, 70.13, 55.75, 87.71,
        95.43, 93.17, 98.54, 68.31, 59.24, 88.94, 79.44, 83.91, 84.4, 68.21]
 
print(round(statistics.mean(data), 2))
print(round(statistics.geometric_mean(data), 2))
print(round(statistics.harmonic_mean(data), 2))
print(round(statistics.median(data), 2))
# %% 123
import statistics
import random
 
 
data = [59.19, 72.05, 66.82, 81.15, 66.33, 94.87, 99.65, 70.13, 55.75, 87.71,
        95.43, 93.17, 98.54, 68.31, 59.24, 88.94, 79.44, 83.91, 84.4, 68.21]
 
random.seed(42)
mu = statistics.mean(data)
sigma = statistics.stdev(data)
dist = statistics.NormalDist(mu, sigma)
result = dist.samples(10)
result = [round(val, 3) for val in result]
print(result)
#%% 124
from statistics import NormalDist
 
 
height = NormalDist(mu=170, sigma=15)
prob = round(height.cdf(180) - height.cdf(170), 4)
print(f'Probability: {100 * prob}%')
# %% 125
import statistics
 
 
data = [59.19, 72.05, 66.82, 81.15, 66.33, 94.87, 99.65, 70.13, 55.75, 87.71,
        95.43, 93.17, 98.54, 68.31, 59.24, 88.94, 79.44, 83.91, 84.4, 68.21]
 
quartiles = statistics.quantiles(data, n=4)
for quartile in quartiles:
    print(round(quartile, 2))
# %% 126
import numbers
 
 
values = [2.0, 2, '2.0', '2', None, False, True]
 
for value in values:
    print(f'{str(value).ljust(6)}: {str(type(value)).ljust(18)} : {isinstance(value, numbers.Number)}')
# %% 127
import numbers
 
 
class Phone:
    
    def __init__(self, price):
        if isinstance(price, numbers.Number) and price > 0:
            self.price = price
        else:
            raise TypeError('Parameter \'value\' must be a positive number.')

# %% 128
import decimal
 
 
result = decimal.Decimal(0.1) + decimal.Decimal(0.2)
print(result)
# %% 129
import decimal
 
 
decimal.getcontext().prec = 40
result = decimal.Decimal(0.1) + decimal.Decimal(0.2)
print(result)
# %% 130
import decimal
 
 
with decimal.localcontext() as ctx:
    ctx.prec = 40
    result = decimal.Decimal(0.1) + decimal.Decimal(0.2)
    print(result)
    
result = decimal.Decimal(0.1) + decimal.Decimal(0.2)
print(result)

















