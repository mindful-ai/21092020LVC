Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = [100, 35, 67, 99, 120]
>>> 
>>> F = []
>>> for temp in T:
	F.append(temp * 1.8 + 32)

	
>>> F
[212.0, 95.0, 152.60000000000002, 210.20000000000002, 248.0]
>>> 
>>> def c2f(t):
	return t * 1.8 + 32

>>> F2 = map(c2f, T)
>>> F2
<map object at 0x00000237D20EE320>
>>> list(F2)
[212.0, 95.0, 152.60000000000002, 210.20000000000002, 248.0]
>>> 
>>> lambda t : t * 1.8 + 32
<function <lambda> at 0x00000237D20E3EA0>
>>> f = lambda t : t * 1.8 + 32
>>> f
<function <lambda> at 0x00000237D211A488>
>>> f(100)
212.0
>>> f(56)
132.8
>>> 
>>> g = lambda a, b : a + b
>>> f(10, 20)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    f(10, 20)
TypeError: <lambda>() takes 1 positional argument but 2 were given
>>> g(10, 20)
30
>>> g("Hello", "World")
'HelloWorld'
>>> 
>>> 
>>> # -------------------------------- map & lambda
>>> 
>>> T = [100, 35, 67, 99, 120]
>>> F = map(lambda t : t * 1.8 + 32, T)
>>> F
<map object at 0x00000237D2109DD8>
>>> list(F)
[212.0, 95.0, 152.60000000000002, 210.20000000000002, 248.0]
>>> 
>>> 
>>> # ---------------------------------- filter & lambda
>>> 
>>> L = list(range(1, 100))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> R = filter(lambda v : (v % 13 == 0), L)
>>> R
<filter object at 0x00000237D2109F98>
>>> list(R)
[13, 26, 39, 52, 65, 78, 91]
>>> 
>>> 
>>> L = list(range(10, 100))
>>> L
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> X = filter(lambda v : (int(str(v)[1]) + int(str(v)[0]) == 10), L)
>>> X
<filter object at 0x00000237D2109F28>
>>> list(X)
[19, 28, 37, 46, 55, 64, 73, 82, 91]
>>> 
>>> n = 76
>>> s = str(n)
>>> s
'76'
>>> s[1]
'6'
>>> s[0]
'7'
>>> s[0] + s[1]
'76'
>>> int(s[0]) + int(s[1])
13
>>> # --------------------------------------- sort & lambda
>>> 
>>> L = ['zebra', 'goat', 'buffalo', 'antelope']
>>> L.sort()
>>> L
['antelope', 'buffalo', 'goat', 'zebra']
>>> 
>>> L.sort(key=lambda s : s[-1])
>>> L
['zebra', 'antelope', 'buffalo', 'goat']
>>> 
>>> 
>>> # --------------------------------------- zip
>>> 
>>> T1 = ('Ram', 'Anil', 'Subhash')
>>> T2 = ('Oracle', 'Intel', 'Infosys')
>>> 
>>> T = zip(T1, T2)
>>> T
<zip object at 0x00000237D20D7A88>
>>> tuple(T)
(('Ram', 'Oracle'), ('Anil', 'Intel'), ('Subhash', 'Infosys'))
>>> 
>>> T3 = ('Oracle', 'Intel', 'Infosys', 'Wipro')
>>> list(zip(T1, T3))
[('Ram', 'Oracle'), ('Anil', 'Intel'), ('Subhash', 'Infosys')]
>>> 
>>> 
>>> D = dict(zip(T1, T3))
>>> D
{'Ram': 'Oracle', 'Anil': 'Intel', 'Subhash': 'Infosys'}
>>> D
{'Ram': 'Oracle', 'Anil': 'Intel', 'Subhash': 'Infosys'}
>>> D.keys()
dict_keys(['Ram', 'Anil', 'Subhash'])
>>> D.values()
dict_values(['Oracle', 'Intel', 'Infosys'])
>>> 
>>> D.items()
dict_items([('Ram', 'Oracle'), ('Anil', 'Intel'), ('Subhash', 'Infosys')])
>>> zip(*D.items())
<zip object at 0x00000237D2117A88>
>>> list(zip(*D.items()))
[('Ram', 'Anil', 'Subhash'), ('Oracle', 'Intel', 'Infosys')]
>>> 
>>> 
>>> # ----------------------------------------- eval
>>> 
>>> eval('10 + 20')
30
>>> x = "s"
>>> eval(' x + 3 ')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    eval(' x + 3 ')
  File "<string>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> eval('x + 3')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    eval('x + 3')
  File "<string>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> c = eval('x + 3')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    c = eval('x + 3')
  File "<string>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> c
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> 10 + 30
40
>>> # ------------------------------------- exec
>>> 
>>> code = '''
x = 10
y = 20
print(x + y)
'''
>>> exec(code)
30
>>> compiledobj = compile(code)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    compiledobj = compile(code)
TypeError: compile() missing required argument 'filename' (pos 2)
>>> fname = r"C:\Users\Purushotham\Desktop\oracle\day_03\session #1\test.py"
>>> compiledobj = compile(fname)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    compiledobj = compile(fname)
TypeError: compile() missing required argument 'filename' (pos 2)
>>> # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
>>> 
>>> 
>>> code = fname.read()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    code = fname.read()
AttributeError: 'str' object has no attribute 'read'
>>> fname = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\session #1\test.py")
>>> code = fname.read()
>>> code
'x = 10\ny = 20\nprint(x + y)\n'
>>> exec(code)
30
>>> compile(fname)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    compile(fname)
TypeError: compile() missing required argument 'filename' (pos 2)
>>> 
>>> 
>>> # --------------------------------------------------- enumerate
>>> 
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> enumerate(seasons)
<enumerate object at 0x00000237D211C5A0>
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=5))
[(5, 'Spring'), (6, 'Summer'), (7, 'Fall'), (8, 'Winter')]
>>> dict(enumerate(seasons))
{0: 'Spring', 1: 'Summer', 2: 'Fall', 3: 'Winter'}
>>> 
>>> 
>>> >>> code_str = 'x=5\ny=10\nprint("sum =",x+y)'
>>> code = compile(code_str, 'sum.py', 'exec')
>>> print(type(code))
<class 'code'>
>>> exec(code)
SyntaxError: invalid syntax
>>> 
>>> 
>>> # --------------- NOEL DAS
>>> 
>>> code_str = '''
x = 5
y = 10
print(x + y)
'''
>>> codeobj = compile(code_str, '', 'exec')
>>> exec(codeobj)
15
>>> fname = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\session #1\test.py")
>>> codeobj = (fname.read(), 'text.py', 'exec')
>>> exec(codeobj)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    exec(codeobj)
TypeError: exec() arg 1 must be a string, bytes or code object
>>> fname.read()
''
>>> fname = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\session #1\test.py")
>>> fname.read()
'x = 10\ny = 20\nprint(x + y)\n'
>>> fname.read()
''
>>> fname.seek(0)
0
>>> codeobj = (fname.read(), 'text.py', 'exec')
>>> exec(codeobj)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    exec(codeobj)
TypeError: exec() arg 1 must be a string, bytes or code object
>>> fname.seek(0)
0
>>> code = fname.read()
>>> code
'x = 10\ny = 20\nprint(x + y)\n'
>>> codeobj = (code, 'text.py', 'exec')
>>> exec(codeobj)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    exec(codeobj)
TypeError: exec() arg 1 must be a string, bytes or code object
>>> codeobj = compile(code, 'text.py', 'exec')
>>> exec(codeobj)
30
>>> 
