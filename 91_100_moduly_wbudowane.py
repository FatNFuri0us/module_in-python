# -*- coding: utf-8 -*-
from pathlib import Path
 
 
path = Path.cwd() / 'hello.txt'
 
if not path.is_file():
    with open(path, 'w') as file:
        file.write('Open,High,Low,Close')
 
with open(path, 'r') as file:
    content = file.read()
print(content)
# %% 92
from pathlib import Path
 
 
path = Path.cwd() / 'hello.txt'
 
if not path.is_file():
    path.write_text('Open,High,Low,Close')
 
content = path.read_text()
print(content)
#%% 93
from pathlib import Path
 
 
paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}' for i in range(1, 13)]
 
for path in paths:
    path.mkdir(parents=True)
 
targets = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]
 
for path, target in zip(paths, targets):
    path.rename(target)
 
for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)
# %% 94
from pathlib import Path
 
 
paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]
 
for path in paths:
    path.mkdir(parents=True)
 
for dir in sorted(Path.cwd().joinpath('reports/2020').iterdir()):
    print(dir)  
# %% 95
from pathlib import Path
 
 
paths = [Path.cwd() / f'reports/2020/{str(i).zfill(2)}_sales' for i in range(1, 13)]
 
t = 3
targets = [Path.cwd() / f'reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales' for i in range(t, t + 12)]
for target in targets:
    print(target)
# %% 96
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
# %% 97
from pathlib import Path
 
 
paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 11)]
 
for path in paths:
    path.mkdir(parents=True)
 
dirs = sorted(list(Path.cwd().joinpath('media/music').iterdir()))
 
for dir in dirs:
    print(dir)  
# %% 98
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
# %% 99
from pathlib import Path
from pprint import pprint
import random
 
 
random.seed(42)
paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 7)]
 
for path in paths:
    path.mkdir(parents=True)
 
paths_dict = {path: [f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}" 
                     for i in range(1, 6)] for path in paths}
 
fname_paths = []
for path, fnames in paths_dict.items():
    for fname in fnames:
        fname_paths.append(path.joinpath(fname))
 
for fname_path in fname_paths:
    print(fname_path) 
# %% 100
from pathlib import Path
from pprint import pprint
import random
 
 
random.seed(42)
paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 7)]
 
for path in paths:
    path.mkdir(parents=True)
 
paths_dict = {path: [f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}" 
                     for i in range(1, 6)] for path in paths}
 
fname_paths = []
for path, fnames in paths_dict.items():
    for fname in fnames:
        fname_paths.append(path.joinpath(fname))
 
for fname_path in fname_paths:
    fname_path.touch()
 
path = Path.cwd() / 'media/music/playlist_01'
for path in sorted(list(path.glob('*.mp3'))):
    print(path)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    