Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> D = {'name' : 'Anil', 'age' : 35 }  # L = ['Anil', 35]
>>> D
{'name': 'Anil', 'age': 35}
>>> D['name']
'Anil'
>>> D['age']
35
>>> 
>>> # --------------------- update values
>>> 
>>> D['name'] = 'Raj'
>>> D
{'name': 'Raj', 'age': 35}
>>> 
>>> 
>>> # --------------------- add values
>>> D['country'] = 'India'
>>> D
{'name': 'Raj', 'age': 35, 'country': 'India'}
>>> D.setdefault('company', 'Oracle')
'Oracle'
>>> D
{'name': 'Raj', 'age': 35, 'country': 'India', 'company': 'Oracle'}
>>> {'name': 'Raj', 'age': 35, 'country': 'India', 'company': 'Oracle'}
{'name': 'Raj', 'age': 35, 'country': 'India', 'company': 'Oracle'}
>>> 
>>> D.setdefault('country')
'India'
>>> D.setfault('addr')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    D.setfault('addr')
AttributeError: 'dict' object has no attribute 'setfault'
>>> D.setdefault('addr')
>>> D
{'name': 'Raj', 'age': 35, 'country': 'India', 'company': 'Oracle', 'addr': None}
>>> D['rank']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    D['rank']
KeyError: 'rank'
>>> 
>>> 
>>> D1 = {'addr' : 'Seattle', 'salary' : '100000 USD' }
>>> D.update(D1)
>>> D
{'name': 'Raj', 'age': 35, 'country': 'India', 'company': 'Oracle', 'addr': 'Seattle', 'salary': '100000 USD'}
>>> 
>>> 
>>> # ---------------------- remove values
>>> 
>>> D.remove('age')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    D.remove('age')
AttributeError: 'dict' object has no attribute 'remove'
>>> D.pop('age')
35
>>> D
{'name': 'Raj', 'country': 'India', 'company': 'Oracle', 'addr': 'Seattle', 'salary': '100000 USD'}
>>> 
>>> 
>>> # ------------------------------- Some useful functions
>>> 
>>> D.keys()
dict_keys(['name', 'country', 'company', 'addr', 'salary'])
>>> D.values()
dict_values(['Raj', 'India', 'Oracle', 'Seattle', '100000 USD'])
>>> D.items()
dict_items([('name', 'Raj'), ('country', 'India'), ('company', 'Oracle'), ('addr', 'Seattle'), ('salary', '100000 USD')])
>>> 
