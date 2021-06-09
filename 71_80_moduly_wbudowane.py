# -*- coding: utf-8 -*-
# %% 71
from collections import defaultdict
 
 
data = [
    ('technology', 'Facebook'),        
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('gaming', 'EA'),    
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]
 
def_dict = defaultdict(set)
for sector, company in data:
    def_dict[sector].add(company)
 
print(def_dict)
# %% 72
from collections import defaultdict
 
 
transactions = [
    ('001', 100),
    ('003', 10),
    ('002', 80),
    ('001', 90),
    ('002', 46),
    ('001', 43),
    ('003', 23),
]
 
def_dict = defaultdict(int)
for user_id, amount in transactions:
    def_dict[user_id] += amount
 
print(def_dict) 
# %% 73
from collections import deque
 
 
daynames = deque(['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])
daynames.appendleft('Mon.')
daynames.append('Sun.')
print(daynames)
# %% 74
from collections import deque
 
 
daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
daynames.rotate(1)
print(daynames)
# %% 75
from collections import deque
 
 
daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
daynames.rotate(-3)
print(daynames.pop())
# %% 76
from collections import deque
 
 
daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
daynames.reverse()
print(daynames.popleft())
# %% 77
from collections import deque
 
 
wishlist = deque()
wishlist.append('003')
wishlist.append('001')
wishlist.append('004')
wishlist.append('002')
wishlist.append('005')
print(wishlist.popleft())
# %% 78
from collections import deque
 
 
user_ids = ['003', '001', '004', None, '002', '005']
 
wishlist = deque()
for user_id in user_ids:
    if user_id is not None:
        wishlist.append(user_id)
    else:
        wishlist.clear()
 
print(wishlist)
# %% 79
from collections import deque
 
 
user_ids = ['003', '001', '004', '006', '002', '005']
 
wishlist = deque(maxlen=3)
for user_id in user_ids:
    wishlist.append(user_id)
    print(wishlist)

# %% 80
from collections import deque
 
 
user_ids = ['003', '001', '004', '002', '005']
 
wishlist = deque(user_ids)
wishlist.extend(['007', '009', '010'])
print(wishlist)









































