Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> L [ 'red', 'blue', 'green']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    L [ 'red', 'blue', 'green']
NameError: name 'L' is not defined
>>> L = [ 'red', 'blue', 'green']
>>> T = ('a', 'e', 'i', 'o', 'u')
>>> D = { 'name': 'anil', 'age' : 35, 'country' : 'India' }
>>> S = set('abcdefg')
>>> S
{'d', 'e', 'b', 'c', 'f', 'g', 'a'}
>>> 
>>> 
>>> # ------------------------------- Using for loop on different data types
>>> 
>>> for ch in s:
	print(ch)

	
p
y
t
h
o
n
>>> for ch in s:
	print(ch, end='-')

	
p-y-t-h-o-n-
>>> 
>>> text = "Imagination is more important than Knowledge"
>>> vowels = 'aeiou'
>>> for vowel in vowels:
	print(vowel.upper() + ' ---> ' + str(text.lower().count(vowel)))

	
A ---> 4
E ---> 3
I ---> 5
O ---> 4
U ---> 0
>>> 
>>> 
>>> for item in L:
	print(item.upper())

	
RED
BLUE
GREEN
>>> 
>>> for vowel in T:
	print(vowel.upper() + ' ---> ' + str(text.lower().count(vowel)))

	
A ---> 4
E ---> 3
I ---> 5
O ---> 4
U ---> 0
>>> 
>>> 
>>> S = set(vowels)
>>> S
{'u', 'e', 'i', 'a', 'o'}
>>> for vowel in S:
	print(vowel.upper() + ' ---> ' + str(text.lower().count(vowel)))

	
U ---> 0
E ---> 3
I ---> 5
A ---> 4
O ---> 4
>>> 
>>> # ---------------------------- iterating a dictionary
>>> 
>>> for x in D:
	print(x)

	
name
age
country
>>> for key in D.keys():
	print(key)

	
name
age
country
>>> for value in D.values():
	print(value)

	
anil
35
India
>>> for item in D.items()
SyntaxError: invalid syntax
>>> for item in D.items():
	print(item)

	
('name', 'anil')
('age', 35)
('country', 'India')
>>> 
>>> for k, v in D.items():
	print(k, v)

	
name anil
age 35
country India
>>> D
{'name': 'anil', 'age': 35, 'country': 'India'}
>>> D1 = {}
>>> for key, value in D.items():
	D1.setdefault(value, key)

	
'name'
'age'
'country'
>>> D1
{'anil': 'name', 35: 'age', 'India': 'country'}
>>> 
>>> 
>>> # --------------------------------- Loop control
>>> # break, continue
>>> 
>>> text = "mississippi"
>>> for ch in text:
	if(ch == 'e'):
		break
	print(ch, end=' ')

	
m i s s i s s i p p i 
>>> text = "soverign"
>>> for ch in text:
	if(ch == 'e'):
		break
	print(ch, end=' ')

	
s o v 
>>> for ch in text:
	if(ch == 'e'):
		continue
	print(ch, end=' ')

	
s o v r i g n 
>>> 
>>> 
>>> # ------------------------------- working with natural numbers
>>> 
>>> range(1, 10)
range(1, 10)
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 40, 3))
[10, 13, 16, 19, 22, 25, 28, 31, 34, 37]
>>> list(range(20, 10, -1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> 
>>> for n in range(1, 11):
	print(str(n) + ' | ' + str(n**2) + ' | ' + str(n**3) + ' | ')

	
1 | 1 | 1 | 
2 | 4 | 8 | 
3 | 9 | 27 | 
4 | 16 | 64 | 
5 | 25 | 125 | 
6 | 36 | 216 | 
7 | 49 | 343 | 
8 | 64 | 512 | 
9 | 81 | 729 | 
10 | 100 | 1000 | 
>>> 
>>> 
>>> # ----------------------------------- Loop else block
>>> 
>>> text = "mississippi"
>>> for ch in text:
	if(ch == 'e'):
		break
	print(ch, end=' ')

	
m i s s i s s i p p i 
>>> for ch in text:
	if(ch == 'e'):
		break
	print(ch, end=' ')
else:
	print('There was no e in the word')

	
m i s s i s s i p p i There was no e in the word
>>> text = "soverign"
>>> for ch in text:
	if(ch == 'e'):
		break
	print(ch, end=' ')
else:
	print('There was no e in the word')

	
s o v 
>>> 
>>> 
>>> # ---------------------------------------- while loop
>>> 
>>> i = 0
>>> while i < 10:
	print(i)
	i += 1  # i = i + 1

	
0
1
2
3
4
5
6
7
8
9
>>> n = 1
>>> while True:
	n = int(input('Enter a number: '))
	if n == 0:
		break

	
Enter a number: 12
Enter a number: 12
Enter a number: 23
Enter a number: 34
Enter a number: 45
Enter a number: 56
Enter a number: 67
Enter a number: 78
Enter a number: 89
Enter a number: 0
>>> 
