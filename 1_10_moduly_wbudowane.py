# -*- coding: utf-8 -*-
## % 1 metoda split
import sys

dir(sys)
print(sys.version.split(' ')[0])

# %% 2
import datetime

dir(datetime)

print(datetime)

>>> help(datetime.time)
# %%
class date(builtins.object):
    date(year, month, day)
# %%
d1 = datetime.date(2021, 1, 1)
d2 = datetime.date(2021, 7, 31)
d3 = datetime.date(1990, 5, 7)
 
print(d1)
print(d2)
print(d3)    

# %% 3

b1 = datetime.time(12, 00, 00)
b2 = datetime.time(6, 30, 00)
b3 = datetime.time(9, 15, 00)

print(b1)
print(b2)
print(b3) 
# %% 4
import datetime


a1 = (datetime.datetime(2020, 7, 20, 11, 30, 00))
a2 = (datetime.datetime(1990, 3, 10, 12))
a3 = (datetime.datetime(2021, 1, 1, 00))

print(a1)
print(a2)
print(a3) 
# %% 5
import datetime


dir(datetime)

a1 = (datetime.datetime(2020, 7, 21))
a2 = (datetime.datetime(2020, 12, 31))

diff = (a2 - a1).days
print(f'Number of days: {diff}')
# %% 6
a1 = datetime.datetime(20, 7, 20, 11, 30)
a2 = datetime.datetime(21, 2, 20, 10, 25)

diff = a2 - a1
print(diff)
## mozna szybciej
print(a2 - a1)
# %% 6
from datetime import datetime

dt1 = datetime(2021, 4, 20, 11, 30, 00)
 
print(dt1.strftime('%Y-%m-%d'))
print(dt1.strftime('%d-%m-%Y'))
print(dt1.strftime('%m-%Y'))
print(dt1.strftime('%B-%Y'))
print(dt1.strftime('%d %B, %Y'))
print(dt1.strftime('%Y-%m-%d %H:%M:%S'))
print(dt1.strftime('%m/%d/%y %H:%M:%S'))
print(dt1.strftime('%d(%a) %B %Y'))
# %% 7

from datetime import datetime


date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'

dt1 = datetime.strptime(date_str_1, '%d %B %Y')
dt2 = datetime.strptime(date_str_2, '%d/%m/%Y')
dt3 = datetime.strptime(date_str_3, '%d-%m-%Y')
 
print(dt1)
print(dt2)
print(dt3)
# %% 8
import datetime

d1 = datetime.datetime(21, 6, 1)
d2 = datetime.datetime(21, 12, 31)
d3 = (d2 - d1).days
print(f'Number of days until the end of the year:{d3}')
### mozna lepie
today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
diff = (end_of_year - today).days
print(f'Number of days until the end of the year: {diff}')
# %% 9
import datetime

now = datetime.datetime.now()
end_of_year = datetime.datetime(now.year, 12, 31, 12)
diff = end_of_year - now
print(f'Until the end of the year: {diff}')

# %% 10
dt = datetime.datetime(2020, 1, 1)
 
print(dt + datetime.timedelta(days=7))
print(dt + datetime.timedelta(days=30))
print(dt + datetime.timedelta(hours=30))
print(dt + datetime.timedelta(minutes=15))




































































