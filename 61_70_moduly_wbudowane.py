# -*- coding: utf-8 -*-
# %% 61
from collections import namedtuple
 
 
Point = namedtuple(typename='Point', field_names=['x', 'y'])
 
pt1 = Point(3, 4)
pt2 = Point(-2, 6)
 
print(pt1)
print(pt2)
# %% 62
from collections import namedtuple
 
 
Point = namedtuple(typename='Point', field_names=['x', 'y'])
 
pt1 = Point(3, 4)
pt2 = Point(-2, 6)
 
avg_pt = Point((pt1.x + pt2.x) / 2.0, (pt1.y + pt2.y) / 2.0)
print(avg_pt)
# %% 63
from collections import namedtuple
 
 
Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])
 
students = [
    Student('Mike', 21, 'physics'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
    ]
 
for student in students:
    print(f'{student.name:5}: {student.age}: {student.specialization}')
# %% 64
from collections import namedtuple
 
 
Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])
 
students = [
    Student('Mike', 21, 'physics'),
    Student('Mark', 22, 'biology'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
    ]
 
students.sort(key=lambda student: student.age)
print(students) 
# %% 65
from collections import namedtuple
 
 
Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])
 
st1 = {'name': 'Kate', 'age': 20, 'specialization': 'mathematics'}
st2 = {'name': 'Mike', 'age': 21, 'specialization': 'physics'}
st3 = {'name': 'Bob', 'age': 21, 'specialization': 'information technology'}
 
students = [Student(**st1), Student(**st2), Student(**st3)]
 
for student in students:
    print(student)
# %% 66
from collections import namedtuple
 
 
Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])
 
students = []
with open('students.txt', 'r') as file:
    lines = [eval(line.strip()) for line in file.readlines()]
    for line in lines:
        students.append(Student(**line))
 
print(students)    
# %% 67
quotations = {}
print(quotations.get('source', 'NYSE'))
print(quotations)
# %% 68
quotations = {}
quotations.setdefault('source', 'NYSE')
print(quotations)
quotations.setdefault('source', 'LSE')
print(quotations)
print(quotations['source'])
# %% 69
data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]
 
data_dict = {}
for sector, company in data:
    data_dict.setdefault(sector, []).append(company)
 
print(data_dict)
# %% 70
from collections import defaultdict
 
 
data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]
 
def_dict = defaultdict(list)
for sector, company in data:
    def_dict[sector].append(company)
 
print(def_dict)






















   