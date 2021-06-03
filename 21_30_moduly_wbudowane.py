# -*- coding: utf-8 -*-
# %% 21
random.seed(30)
images = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]
 
base_dir = 'images'
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')
 
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
 
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
    for file in sorted(files):
        print(file)


# %% 22
import os 
 
 
fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
paths = [os.path.join(os.getcwd(), fname) for fname in fnames]
print(paths)
# %% 23
import os 
 
 
fnames = [f"{str(i).zfill(2)}_sales.csv" for i in range(1, 25)]
paths = [os.path.join(os.getcwd(), '2020', fname) if idx < 12 
         else os.path.join(os.getcwd(), '2021', fname) 
         for idx, fname in enumerate(fnames)]
         
for path in paths:
    print(path)
# %% 24
import os
 
 
paths = [os.path.join(os.getcwd(), f'dir_{str(i).zfill(2)}') for i in range(1, 14)]
 
for path in paths:
    if not os.path.exists(path):
        os.mkdir(path)
    
os.rmdir(os.path.join(os.getcwd(), 'dir_13')) 
fnames = [fname for fname in sorted(os.listdir()) if len(fname) == 6]
print(fnames)
# %% 25
import sys
 
 
print(sys.executable)
# %% 26
import sys
 
 
print(sys.path)
# %% 27 

import sys
 
 
for arg in sys.argv[1:]:
    print(arg)
    
# %% 28
import sys
 
 
if len(sys.argv) > 2:
    result = int(sys.argv[1]) + int(sys.argv[2])
    print(result)    


# %% 29


import sys
 
 
if len(sys.argv) > 1:
    values = [int(value) for value in sys.argv[1:]]
    result = sum(values) / len(values)
    print(f'Average: {result:.4f}')
else:
    print('No values were given.')

# %% 30

import sys
 
 
saved_stdout = sys.stdout
 
file = open('logs.txt', 'w')
sys.stdout = file
 
print('Logging...')
print('Connecting...')
print('Closing...')
 
file.close()
 
sys.stdout = saved_stdout
print('Completed successfully')
































