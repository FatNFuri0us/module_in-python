# %% 91
from pathlib import Path

path = Path.cwd() / 'reports/ecommerce/2020/01'

path.mkdir(parents=True)
print(path.is_dir())

# %% 92 tworzenie katalogow 
from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]
 
for path in paths:
    path.mkdir(parents=True)
 
for dir in sorted(path.parent.iterdir()):
    print(dir)    
# %%

b = [f'reports/2020/{str(i).zfill(4)}' for i in range(1, 13)]    
# .zfill(2) -> wplywa na ilosc 0 przed cyfra
# %% 93 tworzenie pliku, NIE ZMIENIA DANYCH W JUZ ZAPISANYM PLIKU(ta funkcja)
from pathlib import Path


path = Path.cwd() / 'hello.txt'

 
if not path.is_file():
    with open(path, 'w') as file:
        file.write('Open,High,Low,Cl1ose')
 
with open(path, 'r') as file:
    content = file.read()
print(content)
# %% 94 szybsza metoda
from pathlib import Path
 
 
path = Path.cwd() / 'hello.txt'
 
if not path.is_file():
    path.write_text('Open,High,Low,Clo1se')
 
content = path.read_text()
print(content)
# %% 95 zmiana nazwy juz istniejacych katalogow
from pathlib import Path
 
 
paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]
 
for path in paths:
    path.mkdir(parents=True)
 
targets = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]
 
for path, target in zip(paths, targets):
    path.rename(target)
 
for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)
# %% 96
from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]

for path in paths:
    path.mkdir(parents=True)
    
for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()): 
    print(dir)   
# %% 97 sprytne dodanie kwartałow, do zapamietania!
from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]

t = 3
targets = [Path.cwd() / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales' for i in range(t, t + 12)]
for target in targets:
    print(target)
# %% 98 zmiana nazwy
from pathlib import Path


paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]

for path in paths:
    path.mkdir(parents=True)

t = 3
targets = [Path.cwd() / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales' for i in range(t, t + 12)]

for target in targets:
    if not target.parent.is_dir():
        target.mkdir(parents=True)
 
for path, target in zip(paths, targets):
    path.rename(target)
 
for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)
# %% 99
from pathlib import Path

paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 11)]
 
for path in paths:
    path.mkdir(parents=True)
 
dirs = sorted(list(Path.cwd().joinpath('media/music').iterdir()))
 
for dir in dirs:
    print(dir)

# %% 100 tworzenie play listy:)
from pathlib import Path
from pprint import pprint
import random
 
 
random.seed(42)
paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 7)]
 
for path in paths:
    path.mkdir(parents=True)
 
paths_dict = {path: [f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}" 
                     for i in range(1, 6)] for path in paths}
pprint(paths_dict)











































