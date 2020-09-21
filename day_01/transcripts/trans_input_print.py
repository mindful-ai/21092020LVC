Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # INPUT and OUTPUT
>>> 
>>> input()
873246
'873246'
>>> a = input('Enter a number: ')
Enter a number: 56
>>> a
'56'
>>> a + 10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a + 10
TypeError: can only concatenate str (not "int") to str
>>> type(a)
<class 'str'>
>>> int(a) + 10
66
>>> a = int(input("Enter a number: "))
Enter a number: 23
>>> type(a)
<class 'int'>
>>> a + 10
33
>>> 
>>> 
>>> 
>>> print(a + 10)
33
>>> print('The output value is: ', a + 10)
The output value is:  33
>>> 
