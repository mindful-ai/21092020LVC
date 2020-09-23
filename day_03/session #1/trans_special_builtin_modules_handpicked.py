Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # --------------------------------- datetime
>>> 
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 9, 23, 21, 53, 31, 801363)
>>> t.year
2020
>>> t.month
9
>>> t.day
23
>>> t.hour
21
>>> t.second
31
>>> t.minute
53
>>> # Wednesday, 9 September 2020, 21:53
>>> 
>>> # Wednesday, 23 September 2020, 21:53
>>> fstr = "%A, %d %B %Y, %I:%M %p"
>>> t
datetime.datetime(2020, 9, 23, 21, 53, 31, 801363)
>>> t.strftime(fstr)
'Wednesday, 23 September 2020, 09:53 PM'
>>> t.strftime("%A")
'Wednesday'
>>> t1 = t.strftime(fstr)
>>> t1
'Wednesday, 23 September 2020, 09:53 PM'
>>> 
>>> t
datetime.datetime(2020, 9, 23, 21, 53, 31, 801363)
>>> t2 = datetime.now
>>> t2
<built-in method now of type object at 0x00007FF89C53D6C0>
>>> t2 = datetime.now()
>>> t2
datetime.datetime(2020, 9, 23, 22, 2, 48, 898759)
>>> t
datetime.datetime(2020, 9, 23, 21, 53, 31, 801363)
>>> t2 - t
datetime.timedelta(seconds=557, microseconds=97396)
>>> 
>>> 
>>> # ----------------------------------------------
>>> 
>>> 
>>> import datetime
>>> t = datetime.datetime.now()
>>> t
datetime.datetime(2020, 9, 23, 22, 7, 19, 549477)
>>> 
>>> # --------------------------------------- Ana H
>>> 
>>> # --------------------------------------- itertools
>>> 
>>> from itertools import permutations, combinations
>>> 
>>> s = 'ABCD'
>>> permutations(s)
<itertools.permutations object at 0x0000020EC2E1DDB0>
>>> list(permutations(s))
[('A', 'B', 'C', 'D'), ('A', 'B', 'D', 'C'), ('A', 'C', 'B', 'D'), ('A', 'C', 'D', 'B'), ('A', 'D', 'B', 'C'), ('A', 'D', 'C', 'B'), ('B', 'A', 'C', 'D'), ('B', 'A', 'D', 'C'), ('B', 'C', 'A', 'D'), ('B', 'C', 'D', 'A'), ('B', 'D', 'A', 'C'), ('B', 'D', 'C', 'A'), ('C', 'A', 'B', 'D'), ('C', 'A', 'D', 'B'), ('C', 'B', 'A', 'D'), ('C', 'B', 'D', 'A'), ('C', 'D', 'A', 'B'), ('C', 'D', 'B', 'A'), ('D', 'A', 'B', 'C'), ('D', 'A', 'C', 'B'), ('D', 'B', 'A', 'C'), ('D', 'B', 'C', 'A'), ('D', 'C', 'A', 'B'), ('D', 'C', 'B', 'A')]
>>> list(permutations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(permutations(s[:3], 3))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
>>> 
>>> L = list(permutations(s, 3))
>>> L
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> # 'ABC'
>>> 
>>> # 'ABC', ABD' ...
>>> 
>>> R = map(lambda t : ''.join(t), list(permutations(s, 3)))
>>> R
<map object at 0x0000020EC2E43A58>
>>> list(R)
['ABC', 'ABD', 'ACB', 'ACD', 'ADB', 'ADC', 'BAC', 'BAD', 'BCA', 'BCD', 'BDA', 'BDC', 'CAB', 'CAD', 'CBA', 'CBD', 'CDA', 'CDB', 'DAB', 'DAC', 'DBA', 'DBC', 'DCA', 'DCB']
>>> t = ('A', 'B', 'C')
>>> ''.join(t)
'ABC'
>>> R = map(lambda t : ''.join(t), list(permutations(s)))
>>> R
<map object at 0x0000020EC2DD4A20>
>>> list(R)
['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']
>>> combinations(s)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    combinations(s)
TypeError: combinations() missing required argument 'r' (pos 2)
>>> combinations(s, 4)
<itertools.combinations object at 0x0000020EC2E708B8>
>>> list(combinations(s, 4))
[('A', 'B', 'C', 'D')]
>>> 
>>> 
>>> 
>>> # ------------------------------------------- operator
>>> 
>>> from operator import itemgetter
>>> 
>>> itemgetter(1)("apple")
'p'
>>> f = itemgetter(1)
>>> f
operator.itemgetter(1)
>>> 
>>> f('apple')
'p'
>>> f(['a', 'e', 'i', 'o', 'u'])
'e'
>>> L
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> f(L)
('A', 'B', 'D')
>>> f(f(L))
'B'
>>> L = ['zebra', 'goat', 'buffalo', 'giraffe']
>>> L.sort()
>>> L
['buffalo', 'giraffe', 'goat', 'zebra']
>>> L.sort(key=lambda item : item[1])
>>> L
['zebra', 'giraffe', 'goat', 'buffalo']
>>> L.sort(key=f)
>>> L
['zebra', 'giraffe', 'goat', 'buffalo']
>>> 
>>> 
>>> 
>>> 
>>> # ------------------------------------------------ collections
>>> 
>>> from collections import Counter
>>> data = ['red', 'red', 'green', 'red', 'green', 'yellow']
>>> 
>>> D = {}
>>> for item in data:
	if(item in D.keys()):
		D[item] = D[item] + 1
	else:
		D[item] = 1

		
>>> D
{'red': 3, 'green': 2, 'yellow': 1}
>>> 
>>> D1 = Counter(data)
>>> D1
Counter({'red': 3, 'green': 2, 'yellow': 1})
>>> 
>>> # -------------------------------------------- functools
>>> 
>>> from functools import reduce
>>> 
>>> L = list(range(1, 6))
>>> L
[1, 2, 3, 4, 5]
>>> 
>>> reduce(lambda x,y:x+y, L)
15
>>> ''.join(L)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    ''.join(L)
TypeError: sequence item 0: expected str instance, int found
>>> reduce(lambda x,y:str(x)+ str(y), L)
'12345'
>>> 
