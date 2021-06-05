# -*- coding: utf-8 -*-
# %% 41
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
 
print(re.findall(r"<ht.*>", html)[0])
# %% 42
import re
 
 
text = "Please send an email to info@template.com or sales-info@template.it"
print(re.findall(r"[\w\.-]+@[\w\.-]+", text))
# %% 43
import re
 
 
text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""
 
print(re.findall(pattern=r"\w+", string=text))
# %% 44
import re
 
 
text = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""
 
print(re.findall(pattern=r"[A-Z]\w+", string=text))
# %% 45
import re
 
 
message = 'For more information, please call: 123-456-789'
print(re.findall(r"\d{3}-\d{3}-\d{3}", message)[0])
# %% 46
import re
 
 
text = "Please send an email to info@template.com or call to: 123-456-789."
print(re.sub(r"\d{3}-\d{3}-\d{3}", '***-***-***', text))
# %% 47
from collections import Counter
 
 
target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']
cnt = Counter(target)
print(cnt)
# %% 48
from collections import Counter
 
 
poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
 
cnt_1 = Counter(poll_1)
cnt_2 = Counter(poll_2)
 
cnt_total = cnt_1 + cnt_2
print(cnt_total)
# %% 49
from collections import Counter
 
 
poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}
 
cnt_1 = Counter(poll_1)
cnt_2 = Counter(poll_2)
cnt_3 = Counter(poll_3)
 
cnt_total = cnt_1 + cnt_2 + cnt_3
print(cnt_total['yes'])

# %% 50
from collections import Counter
 
 
text = 'python programming - introduction'
 
cnt = Counter(text)
print(cnt)
































