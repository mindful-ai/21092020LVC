Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'s', 'p', 'm', 'i'}
>>> 
>>> 
>>> s1 = set('abcdefg')
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> S1
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    S1
NameError: name 'S1' is not defined
>>> s1
{'c', 'a', 'b', 'g', 'd', 'e', 'f'}
>>> s2
{'j', 'h', 'g', 'd', 'i', 'e', 'f'}
>>> 
>>> s1 | s2
{'j', 'h', 'c', 'a', 'b', 'g', 'd', 'i', 'e', 'f'}
>>> s1 & s2
{'d', 'f', 'g', 'e'}
>>> s1 ^ s2
{'c', 'b', 'i', 'j', 'h', 'a'}
>>> 
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'x', 'c', 'a', 'b', 'g', 'd', 'e', 'f'}
>>> s3 = {'y' ,'z'}
>>> s1.update(s3)
>>> s1
{'x', 'c', 'a', 'b', 'z', 'g', 'd', 'y', 'e', 'f'}
>>> 
>>> s1.remove('d')
>>> 'x' in s1
True
>>> 
>>> 
>>> s1.intersection(s2)
{'e', 'f', 'g'}
>>> s1.union(s2)
{'j', 'x', 'h', 'c', 'a', 'b', 'z', 'g', 'd', 'i', 'y', 'e', 'f'}
>>> 
>>> 
>>> s1
{'x', 'c', 'a', 'b', 'z', 'g', 'y', 'e', 'f'}
>>> s1.add('a')
>>> s1
{'x', 'c', 'a', 'b', 'z', 'g', 'y', 'e', 'f'}
>>> 
