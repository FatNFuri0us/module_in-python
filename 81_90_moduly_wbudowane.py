# -*- coding: utf-8 -*-
# %% 81
from pprint import pprint
 
 
data_dict = {
    "users": [
        {
            "userId": 1,
            "firstName": "Krish",
            "lastName": "Lee",
            "emailAddress": "krish.lee@example.com"
        },
        {
            "userId": 2,
            "firstName": "racks",
            "lastName": "jacson",
            "emailAddress": "racks.jacson@example.com"
        },
        {
            "userId": 3,
            "firstName": "denial",
            "lastName": "roast",
            "emailAddress": "denial.roast@example.com"
        }
    ]
}
 
pprint(data_dict)
# %% 82
import pathlib
 
 
print(pathlib.Path.cwd())
# %% 83
import pathlib
 
 
print(pathlib.Path.home())

# %% 84
from pathlib import Path
 
 
path = Path('/home/evaluator/reports/2020/01/sales.csv')
print(path)

# %% 85
from pathlib import Path
 
 
path1 = Path.home().joinpath('reports/2020/01/sales.csv')
path2 = Path.cwd().joinpath('reports/2020/01/sales.csv')
print(path1)
print(path2)
# %% 86
from pathlib import Path
 
 
path = Path.home() / 'reports/2020/01/sales.csv'
print(path)
print(path.parent)
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parts)
# %% 87
from pathlib import Path
 
 
path = Path.home() / 'reports/2020/01/sales.csv'
 
for parent in path.parents:
    print(parent)
# %% 88
from pathlib import Path
 
 
path = Path.cwd() / 'reports'
 
if not path.is_dir():
    path.mkdir()
 
for item in sorted(Path.cwd().iterdir()):
    print(item) 
# %% 89
from pathlib import Path
 
 
path = Path.cwd() / 'reports/ecommerce/2020/01'
path.mkdir(parents=True)
print(path.is_dir())    
# %% 90
from pathlib import Path
 
 
paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]
 
for path in paths:
    path.mkdir(parents=True)
 
for dir in sorted(path.parent.iterdir()):
    print(dir) 




