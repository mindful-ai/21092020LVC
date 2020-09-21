Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> 
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> # -------------- accessing individual characters
>>> # [index]
>>> # [start:end] [4:7] 4, 5, 6 characters
>>> # [start:end:skip]
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[2]
't'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> s[1:5]
'ytho'
>>> s[-5:-2]
'yth'
>>> s[-2:-5]
''
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> s1 = '0123456789'
>>> type(s1)
<class 'str'>
>>> s1[2:6]
'2345'
>>> s1[2:6:2]
'24'
>>> s1[:]
'0123456789'
>>> s1[::2]
'02468'
>>> s1[1::2]
'13579'
>>> s1
'0123456789'
>>> s1[:]
'0123456789'
>>> s1[::-1]
'9876543210'
>>> 
>>> 
>>> s1
'0123456789'
>>> 
>>> 
>>> # ------------------------ operators to work on stringsd
>>> 
>>> 
>>> 'hello' + 'world'
'helloworld'
>>> 'hello' * 3
'hellohellohello'
>>> len(s1)
10
>>> '345' in s1
True
>>> 'app' in s1
False
>>> del s1
>>> s1
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s1
NameError: name 's1' is not defined
>>> 
>>> 
>>> # -----------------------
>>> 
>>> s1 = '0123456789'
>>> s2 = s1[:3] + s1[3:8][::-1] + s1[8:]
>>> s2
'0127654389'
>>> s1[:3]
'012'
>>> s1[:3]
'012'
>>> s1[3:8][::-1]
'76543'
>>> s1[3:7][::-1]
'6543'
>>> s1[7:]
'789'
>>> s1[:3] + s1[3:7][::-1] + s1[7:]
'0126543789'
>>> s1
'0123456789'
>>> 
>>> # ---------------------------- immutable nature of strings
>>> 
>>> s1
'0123456789'
>>> s1[0]
'0'
>>> s1[-1]
'9'
>>> s1[0] = '7'
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s1[0] = '7'
TypeError: 'str' object does not support item assignment
>>> s1 = s1[:3] + s1[3:7][::-1] + s1[7:]
>>> s1
'0126543789'
>>> 
>>> 
>>> # ------------------------------------ functions to work with strings
>>> 
>>> s
'python'
>>> 
>>> # --------------- case related functions
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> 
>>> # --------------------- querying
>>> 
>>> s.isdigit()
False
>>> s1.isdigit()
True
>>> s1
'0126543789'
>>> s
'python'
>>> s.isalpha()
True
>>> s.isalnum()
True
>>> '123abc'.isalnum()
True
>>> '123abc%'.isalnum()
False
>>> ' '.isspace()
True
>>> 
>>> site = "www.google.com"
>>> site.startswith("https")
False
>>> site.endsswith("com")
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    site.endsswith("com")
AttributeError: 'str' object has no attribute 'endsswith'
>>> site.endswith("com")
True
>>> 
>>> 
>>> # ------------------------ search
>>> 
>>> s.find("th")
2
>>> s.count('t')
1
>>> s2 = "apple"
>>> s2.count("p")
2
>>> s2.count("pp")
1
>>> 
>>> # -------------------------------- modifications
>>> 
>>> s3 = '  python  '
>>> s3.strip()
'python'
>>> s3.lstrip()
'python  '
>>> s3.rstrip()
'  python'
>>> 
>>> s3
'  python  '
>>> 
>>> 
>>> ip = "192-56-34-54"
>>> ip.replace('-', '.')
'192.56.34.54'
>>> ip
'192-56-34-54'
>>> 
>>> p = "10,456,345"
>>> 0.1 * p
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    0.1 * p
TypeError: can't multiply sequence by non-int of type 'float'
>>> 0.1 * int(p)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    0.1 * int(p)
ValueError: invalid literal for int() with base 10: '10,456,345'
>>> 0.1 * int(p.replace(',', ''))
1045634.5
>>> p.replace(',', '') + 0.1 * int(p.replace(',', ''))
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    p.replace(',', '') + 0.1 * int(p.replace(',', ''))
TypeError: can only concatenate str (not "float") to str
>>> int(p.replace(',', '')) + 0.1 * int(p.replace(',', ''))
11501979.5
>>> "11,501,979.50"
'11,501,979.50'
>>> 
>>> 
>>> s
'python'
>>> s.ljust(20)
'python              '
>>> s.rjust(20, '>')
'>>>>>>>>>>>>>>python'
>>> 
>>> 
>>> st = "imagination is more important than knowledge"
>>> st.split()
['imagination', 'is', 'more', 'important', 'than', 'knowledge']
>>> st.split('a')
['im', 'gin', 'tion is more import', 'nt th', 'n knowledge']
>>> L = st.split()
>>> type(L)
<class 'list'>
>>> 
>>> '-'.join(L)
'imagination-is-more-important-than-knowledge'
>>> 
