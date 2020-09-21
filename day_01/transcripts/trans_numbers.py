Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Purushotham\Desktop\oracle\day_01\startup\myfirstcode.py =
148
>>> print('Hello')
Hello
>>> # NUMBERS
>>> 5
5
>>> 2
2
>>> a = 5
>>> b = 2
>>> __myvar = a + b
>>> a
5
>>> a
5
>>> a
5
>>> a
5
>>> b
2
>>> b
2
>>> b
2
>>> b
2
>>> # -------------------------------- OPERATORS
>>> 
>>> # Arithmetic Operators
>>> # + - * / // % **
>>> c = a + b
>>> print(c)
7
>>> c
7
>>> a + b
7
>>> a + b - 2
5
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a ** b
25
>>> # Relational Operators
>>> # > < <= >= != ==
>>> 
>>> a > b # Is the value in a greater than the value in b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a != b
True
>>> a == b * 2 + 1
True
>>> 
>>> # Logical Operators
>>> 
>>> a > b and a < 10
True
>>> not(a > b and a < 10)
False
>>> a > b and not a < 10 or a != 0
True
>>> 
>>> 
>>> # Chaining of operators
>>> 
>>> a > 1 and a < 10
True
>>> 1 < a < 10
True
>>> 
>>> 
>>> # ---------------------------------- Built In Functions
>>> 
>>> abs(10 -3)
7
>>> 10 - 3
7
>>> 3 - 10
-7
>>> abs(3 - 10)
7
>>> abs(10 -3)
7
>>> a = 100
>>> type(a)
<class 'int'>
>>> b = '100'
>>> type(b)
<class 'str'>
>>> a + b
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a + int(b)
200
>>> bin(a)
'0b1100100'
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> type(a)
<class 'int'>
>>> x = bin(a)
>>> type(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
>>> type(x)
<class 'str'>
>>> x
'0b1100100'
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '0b1100100'
>>> int(x, 2)
100
>>> 
>>> 
>>> # --------------------------------- In - built module
>>> 
>>> a = 99
>>> b = 55
>>> gcd(a, b)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    gcd(a, b)
NameError: name 'gcd' is not defined
>>> import math
>>> gcd(a, b)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    gcd(a, b)
NameError: name 'gcd' is not defined
>>> math.gcd(a, b)
11
>>> math.sqrt(a * b)
73.79024325749306
>>> math.factorial(5)
120
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * 3.14159/180)
0.9999999999991198
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> 
>>> 
>>> from random import randint
>>> randint(1, 100)
63
>>> randint(1, 100)
94
>>> randint(1, 100)
79
>>> randint(1, 100)
15
>>> randint(1, 100)
100
>>> randint(1, 100)
67
>>> randint(1, 100)
79
>>> 
