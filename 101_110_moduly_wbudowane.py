# -*- coding: utf-8 -*-
# %% 101
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
 
path = Path.cwd() / 'media/music'
for path in sorted(list(path.rglob('*.mp3'))):
    print(path)
# %% 102
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
 
path = Path.cwd() / 'media/music/playlist_05'
fnames_mp3 = list(path.glob('*.mp3'))
fnames_wav = list(path.glob('*.wav'))
 
print(f'fnames_mp3: {len(fnames_mp3)}')
print(f'fnames_wav: {len(fnames_wav)}')
# %% 103
from pathlib import Path
 
 
path = Path.cwd() / 'README.md'
 
with path.open('r') as file:
    headers = [line.strip() for line in file if line.startswith('#')]
print('\n'.join(headers))  
# %% 104
from pathlib import Path
import re
 
 
pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
 
path = Path.cwd() / 'README.md'
content = path.read_text()
https = re.findall(pattern, content)
print('\n'.join(sorted((set(https)))))
# %% 105
import random
 
 
random.seed(42)
var = random.random()
print(f'{var:.5}')
# %% 106
import random
 
 
random.seed(42)
numbers = [round(random.random(), 4) for _ in range(10)]
print(numbers)
# %% 107
import random
 
 
random.seed(42)
a = 5
b = 10
numbers = [round((b - a) * random.random() + a, 4) for _ in range(10)]
print(numbers)
# %% 108
import random
 
 
random.seed(42)
numbers = [random.randint(1, 49) for _ in range(6)]
print(numbers)
# %% 109
import random
 
 
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']
random.seed(32)
print(random.choice(techs))
# %% 110

import random
 
 
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']
random.seed(32)
print(random.choices(population=techs, k=3))














  
