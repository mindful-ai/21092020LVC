Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "imagination is more important than knowledge"
>>> # "Imagination Is More Important Than Knowledge"
>>> words = s.split()
>>> words
['imagination', 'is', 'more', 'important', 'than', 'knowledge']
>>> newwords = []
>>> for word in words:
	newwords.append(word.capitalize())

	
>>> newwords
['Imagination', 'Is', 'More', 'Important', 'Than', 'Knowledge']
>>> ' '.join(newwords)
'Imagination Is More Important Than Knowledge'
>>> 
>>> # ---------------------------- pythonic #1
>>> s = "imagination is more important than knowledge"
>>> words = s.split()
>>> newwords = map(lambda word : word.capitalize(), words)
>>> ' '.join(newwords)
'Imagination Is More Important Than Knowledge'
>>> 
>>> 
>>> # ---------------------------- pythonic #1
>>> s = "imagination is more important than knowledge"
>>> words = s.split()
>>> newwords = [word.capitalize() for word in words]
>>> ' '.join(newwords)
'Imagination Is More Important Than Knowledge'
>>> 
>>> 
>>> 
>>> # ---------------------------- pythonic #2 futher improvisation
>>> s = "imagination is more important than knowledge"
>>> ' '.join([word.capitalize() for word in s.split()])
'Imagination Is More Important Than Knowledge'
>>> 
>>> 
>>> 
>>> # formula for writing a comprehension
>>> 
>>> # [], (), {}, {}
>>> # [<expression> <loop> <condition>]
>>> 
>>> L = [x for x in range(100) if x % 2 == 0]
>>> L
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> T = (x for x in range(100) if x % 2 == 1 and x % 7 == 0)
>>> T
<generator object <genexpr> at 0x000001ACDC21B930>
>>> tuple(T)
(7, 21, 35, 49, 63, 77, 91)
>>> 
>>> L = ['red', 'green', 'blue']
>>> D = { s:len(s) for s in L }
>>> D
{'red': 3, 'green': 5, 'blue': 4}
>>> from collections import Counter
>>> D = { s: {'length':len(s), 'chist':Counter(s)} for s in L }
>>> D
{'red': {'length': 3, 'chist': Counter({'r': 1, 'e': 1, 'd': 1})}, 'green': {'length': 5, 'chist': Counter({'e': 2, 'g': 1, 'r': 1, 'n': 1})}, 'blue': {'length': 4, 'chist': Counter({'b': 1, 'l': 1, 'u': 1, 'e': 1})}}
>>> 
>>> 
>>> 
>>> L = [1,2,3,4,5]
>>> F = [x**2 for x in L if(x == 3)]
>>> F
[9]
>>> F = [x ** 2 if x == 3 else x for x in L]
>>> F
[1, 2, 9, 4, 5]
>>> 
 RESTART: C:/Users/Purushotham/Desktop/oracle/day_03/session #2/performance_check.py 
Time elapsed:  0:00:00
>>> 
>>> 
>>> 
