Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [12, 1.4, -5, True, False, "apple", "boy", [1, 2, 3], hex, bin, int]
>>> type(L)
<class 'list'>
>>> 
>>> # ---------------- subscripting
>>> 
>>> L[0]
12
>>> L[-1]
<class 'int'>
>>> L[2:5]
[-5, True, False]
>>> L[::2]
[12, -5, False, 'boy', <built-in function hex>, <class 'int'>]
>>> 
>>> 
>>> # ---------------------- Accessing elements and mutability
>>> 
>>> L = ['red'. 'green', 'blue']
SyntaxError: invalid syntax
>>> L = ['red', 'green', 'blue']
>>> L
['red', 'green', 'blue']
>>> L[0]
'red'
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue']
>>> L[0]
'orange'
>>> L[0][1]
'r'
>>> L[0][1] = 'g'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    L[0][1] = 'g'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # ------------------------------------ operators
>>> 
>>> 
>>> L1 = ['black', 'white', 'grey']
>>> L
['orange', 'green', 'blue']
>>> L + L1
['orange', 'green', 'blue', 'black', 'white', 'grey']
>>> L * 3
['orange', 'green', 'blue', 'orange', 'green', 'blue', 'orange', 'green', 'blue']
>>> len(L)
3
>>> 'red' in (L + L1)
False
>>> 'orange' in (L + L1)
True
>>> del L1[2]
>>> del
SyntaxError: invalid syntax
>>> L1
['black', 'white']
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> 
>>> # ------------------------------- functions to work with a list
>>> 
>>> # ---- Adding elements
>>> 
>>> L
['orange', 'green', 'blue']
>>> L.append("yellow")
>>> L
['orange', 'green', 'blue', 'yellow']
>>> L.append("red")
>>> L
['orange', 'green', 'blue', 'yellow', 'red']
>>> L.insert(1, "pink")
>>> L
['orange', 'pink', 'green', 'blue', 'yellow', 'red']
>>> 
>>> L1 = ["white", "Black"]
>>> L.extend(L1)
>>> L
['orange', 'pink', 'green', 'blue', 'yellow', 'red', 'white', 'Black']
>>> 
>>> L[3] = 'maroon'
>>> L
['orange', 'pink', 'green', 'maroon', 'yellow', 'red', 'white', 'Black']
>>> L[3] = ['cyan', 'blue']
>>> L
['orange', 'pink', 'green', ['cyan', 'blue'], 'yellow', 'red', 'white', 'Black']
>>> 
>>> 
>>> 
>>> 
>>> L = ['orange', 'pink', 'green', 'blue', 'yellow', 'red', 'white', 'Black']
>>> L
['orange', 'pink', 'green', 'blue', 'yellow', 'red', 'white', 'Black']
>>> L[3:4]
['blue']
>>> L[3:4] = "maroon"
>>> L
['orange', 'pink', 'green', 'm', 'a', 'r', 'o', 'o', 'n', 'yellow', 'red', 'white', 'Black']
>>> 
>>> 
>>> 
>>> L = ['orange', 'pink', 'green', 'blue', 'yellow', 'red', 'white', 'Black']
>>> L
['orange', 'pink', 'green', 'blue', 'yellow', 'red', 'white', 'Black']
>>> L[3:4] = ['cyan', 'maroon', 'magenta']
>>> L
['orange', 'pink', 'green', 'cyan', 'maroon', 'magenta', 'yellow', 'red', 'white', 'Black']
>>> 
>>> 
>>> L
['orange', 'pink', 'green', 'cyan', 'maroon', 'magenta', 'yellow', 'red', 'white', 'Black']
>>> L[-3:]
['red', 'white', 'Black']
>>> L[-3:] = ['golden', 'cerulean']
>>> L
['orange', 'pink', 'green', 'cyan', 'maroon', 'magenta', 'yellow', 'golden', 'cerulean']
>>> 
>>> 
>>> # Remove elements
>>> 
>>> L
['orange', 'pink', 'green', 'cyan', 'maroon', 'magenta', 'yellow', 'golden', 'cerulean']
>>> L.pop()
'cerulean'
>>> L
['orange', 'pink', 'green', 'cyan', 'maroon', 'magenta', 'yellow', 'golden']
>>> L.pop(3)
'cyan'
>>> L
['orange', 'pink', 'green', 'maroon', 'magenta', 'yellow', 'golden']
>>> L.remove('pink')
>>> L
['orange', 'green', 'maroon', 'magenta', 'yellow', 'golden']
>>> 
>>> 
>>> # Searching
>>> 
>>> L
['orange', 'green', 'maroon', 'magenta', 'yellow', 'golden']
>>> L.index('green')
1
>>> L.index('apple')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    L.index('apple')
ValueError: 'apple' is not in list
>>> L.find('apple')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    L.find('apple')
AttributeError: 'list' object has no attribute 'find'
>>> 
>>> L.count('red')
0
>>> L.count('golden')
1
>>> 
>>> # rearranging elements in the list
>>> 
>>> L
['orange', 'green', 'maroon', 'magenta', 'yellow', 'golden']
>>> reversed(L)
<list_reverseiterator object at 0x000001BAEE745208>
>>> list(reversed(L))
['golden', 'yellow', 'magenta', 'maroon', 'green', 'orange']
>>> L
['orange', 'green', 'maroon', 'magenta', 'yellow', 'golden']
>>> L.reverse()
>>> L
['golden', 'yellow', 'magenta', 'maroon', 'green', 'orange']
>>> 
>>> 
>>> 
>>> sorted(L)
['golden', 'green', 'magenta', 'maroon', 'orange', 'yellow']
>>> L
['golden', 'yellow', 'magenta', 'maroon', 'green', 'orange']
>>> L.sort()
>>> L
['golden', 'green', 'magenta', 'maroon', 'orange', 'yellow']
>>> L.sort(reverse=True)
>>> L
['yellow', 'orange', 'maroon', 'magenta', 'green', 'golden']
>>> 
>>> 
>>> 
>>> # Iteration
>>> 
>>> for item in L:

	print(item)

	
yellow
orange
maroon
magenta
green
golden
>>> for item in L:
	print(item.upper())

	
YELLOW
ORANGE
MAROON
MAGENTA
GREEN
GOLDEN
>>> 
