# -*- coding: utf-8 -*-
# %% 31
stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.copy(stocks)
 
stocks[0][1] = 'CRJ'
 
print(f'stocks: {stocks}')
print(f'stocks_copied: {stocks_copied}')
# %% 32

import copy
 
 
stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.deepcopy(stocks)
 
stocks[0][1] = 'CRJ'
 
print(f'stocks: {stocks}')
print(f'stocks_copied: {stocks_copied}')

# %% 33
docs = 'programming in python'
code_map = dict((enumerate(string.ascii_lowercase)))
code_map_inv = {val: key for key, val in code_map.items()}
 
result = ''
for char in docs:
    if char == ' ':
        result += ' '
        continue
    idx = (code_map_inv[char] + 3) % 26
    result += code_map[idx]
 
print(result)
# %% 34
from string import Template
 
 
names = ['John', 'Paul', 'Lisa', 'Michael']
 
email = """Hello $name,
Thank you for visiting our website.
Team, XYZ"""
 
template = Template(email)
 
for name in names:
    print(template.substitute(name=name))
    print('-' * 35)
    
# %% 35
import re
 
 
text = 'Python 3.8'
print(re.findall(pattern=r'\d', string=text))
# %% 36
import re
 
 
text = 'Python 3.8'
print(re.findall(pattern=r'\D', string=text))
# %% 37
import re
 
 
code = '0010-000-423'
print(re.findall(pattern=r"[^0-]", string=code))
# %% 38
import re
 
 
code = '0010-000-423-22'
print(re.split(pattern='-', string=code))

# %% 39

import re
 
 
code = 'PL code: XG-GH-110'
print(re.findall(pattern=r"PL|\d+", string=code))

# %% 40
import re
 
 
html = """<!doctype html>
 
<html lang="en">
<head>
  <meta charset="utf-8">
 
  <title>The HTML5 Title</title>
  <meta name="description">
 
  <link rel="stylesheet" href="css/styles.css?v=1.0">
 
</head>
 
<body>
  <script src="js/scripts.js"></script>
</body>
</html>"""
 
for tag in re.findall(r"<.*>", html):
    print(tag)    












