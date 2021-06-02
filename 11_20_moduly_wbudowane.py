# -*- coding: utf-8 -*-
# %% 11

import datetime

dt = datetime.datetime(2020, 1, 1)
delta = datetime.timedelta(hours=8)
 
dates = [dt + i * delta for i in range(12)]
 
for date in dates:
    print(date)
# %% 12    

r = 0.04
pv = 1000
daily_rate = r / 365.0
 
d1 = datetime.date(2021, 7, 1)
d2 = datetime.date(2021, 12, 31)
duration = d2 - d1
 
fv = pv * (1 + daily_rate) ** duration.days
print(f'Future value: {fv:.2f} USD')

# %% MODUL OS 13
import os

print(os.getcwd())
# %% 14
import os

print(os.listdir(None))
# %% mozna tez tak
print(os.listdir())
# %% 15
import os


names = os.listdir()
names = sorted([name for name in os.listdir() if name.startswith('e')])
print(names)

# %% 16


names = sorted([x for x in os.listdir() if x.endswith('.py')])

## names = sorted(names, key = lambda x : x[1])

# %% 17 ISTOTNE OPCJE
import os

os.mkdir('images')
os.chdir('images')
print(os.getcwd())
# %% 18
import os

os.mkdir('documents')

dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]
for dirname in dirnames:
    path = os.path.join('documents', dirname)
    os.mkdir(path)
 
print(sorted(os.listdir('documents')))

#%%

dirnames = [f'{str(i)}_sales' for i in range(1, 13)]
# %% 19
import os

os.mkdir.join('images', 'images_png')
i2 = os.path.join('images', 'images_png')
i3 = os.path.join('images', 'images_jpg')
os.mkdir(i2)
os.mkdir(i3)

# %% duzo lepiej
base_dir = 'images'
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')
 
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
 
if not os.path.exists(png_dir):
    os.mkdir(png_dir)
 
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)
 
for root, dirs, files in os.walk(base_dir):
    print(root)
# %% 20
import os
import random
 
 
random.seed(30)
images = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]
 
base_dir = 'images'
 
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
 
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')
 
if not os.path.exists(png_dir):
    os.mkdir(png_dir)
 
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)
 
for image in images:
    if image.endswith('.png'):
        open(os.path.join(png_dir, image), 'w').close()
    elif image.endswith('.jpg'):
        open(os.path.join(jpg_dir, image), 'w').close()
 
for root, dirs, files in os.walk(base_dir):
    print(root)
    for file in sorted(files):
        print(f'\t{file}')
















