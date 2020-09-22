Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ("red", "green", "blue")
>>> 
>>> T[0]
'red'
>>> T[2]
'blue'
>>> T[-1]
'blue'
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> T[0] = "yellow"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    T[0] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # ---------------------- rearrangement of elements
>>> 
>>> reversed(T)
<reversed object at 0x000001EA6A475550>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> sorted(T)
['blue', 'green', 'red']
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
>>> # ---------------------- operators
>>> 
>>> T
('red', 'green', 'blue')
>>> T1 = ("black, "white")
      
SyntaxError: invalid syntax
>>> T1 = ("black", "white")
>>> 
>>> T + T1
('red', 'green', 'blue', 'black', 'white')
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> len( T + T1 )
5
>>> "red" in T
True
>>> 
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T1
>>> t1
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t1
NameError: name 't1' is not defined
>>> T1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> 
>>> 
>>> # ----------------------- consciously doing changes on tuple
>>> 
>>> T
('red', 'green', 'blue')
>>> T[1] = "yellow"
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    T[1] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> T1 = tuple(L)
>>> T1
('red', 'yellow', 'blue')
>>> 
>>> 
>>> # -------------------------------- techniques
>>> 
>>> r,g,b = T
>>> T
('red', 'green', 'blue')
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> T = ('red', 'green', 'blue', "yellow", "orange")
>>> r,g,b = T
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    r,g,b = T
ValueError: too many values to unpack (expected 3)
>>> r,g,b,*x = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> x
['yellow', 'orange']
>>> 
