Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # File operations
>>> # open(), close()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # tell(), seek()
>>> 
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data.txt")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "c:\new\text\read\table.dat"
>>> print(path)
c:
ew	extead	able.dat
>>> path = r"c:\new\text\read\table.dat"
>>> print(path)
c:\new\text\read\table.dat
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data.txt")
>>> type(f)
<class '_io.TextIOWrapper'>
>>> content = f.read()
>>> type(content)
<class 'str'>
>>> print(content)
Imagine there's no heaven
It's easy if you try
No hell below us
Above us only sky
Imagine all the people living for today
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people living life in peace, you
You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people sharing all the world, you
You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
>>> len(content)
630
>>> content.upper()
"IMAGINE THERE'S NO HEAVEN\nIT'S EASY IF YOU TRY\nNO HELL BELOW US\nABOVE US ONLY SKY\nIMAGINE ALL THE PEOPLE LIVING FOR TODAY\nIMAGINE THERE'S NO COUNTRIES\nIT ISN'T HARD TO DO\nNOTHING TO KILL OR DIE FOR\nAND NO RELIGION TOO\nIMAGINE ALL THE PEOPLE LIVING LIFE IN PEACE, YOU\nYOU MAY SAY I'M A DREAMER\nBUT I'M NOT THE ONLY ONE\nI HOPE SOME DAY YOU'LL JOIN US\nAND THE WORLD WILL BE AS ONE\nIMAGINE NO POSSESSIONS\nI WONDER IF YOU CAN\nNO NEED FOR GREED OR HUNGER\nA BROTHERHOOD OF MAN\nIMAGINE ALL THE PEOPLE SHARING ALL THE WORLD, YOU\nYOU MAY SAY I'M A DREAMER\nBUT I'M NOT THE ONLY ONE\nI HOPE SOME DAY YOU'LL JOIN US\nAND THE WORLD WILL BE AS ONE"
>>> "imagine".content.lower()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    "imagine".content.lower()
AttributeError: 'str' object has no attribute 'content'
>>> content.lower().count("imagine")
6
>>> 
>>> 
>>> f.readline()
''
>>> f.tell()
652
>>> f.seek(0)
0
>>> f.tell()
0
>>> f.readline()
"Imagine there's no heaven\n"
>>> f.readline()
"It's easy if you try\n"
>>> f.readline()
'No hell below us\n'
>>> f.readline()
'Above us only sky\n'
>>> f.readline()
'Imagine all the people living for today\n'
>>> f.readline()
"Imagine there's no countries\n"
>>> f.readline()
"It isn't hard to do\n"
>>> 
>>> f.seek(0)
0
>>> f.readlines()
["Imagine there's no heaven\n", "It's easy if you try\n", 'No hell below us\n', 'Above us only sky\n', 'Imagine all the people living for today\n', "Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> f.seek(0)
0
>>> content = f.readlines()
>>> type(content)
<class 'list'>
>>> content[1]
"It's easy if you try\n"
>>> content[-2:]
["I hope some day you'll join us\n", 'And the world will be as one']
>>> 
>>> f.close()
>>> 
>>> # --------------------------------- writing to files
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "w")
>>> f.write('IMAGINE by JOHN LENNON\n')
23
>>> f.write('-'*60 + '\n')
61
>>> f.close()
>>> 
>>> content
["Imagine there's no heaven\n", "It's easy if you try\n", 'No hell below us\n', 'Above us only sky\n', 'Imagine all the people living for today\n', "Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f.writelines(content)
>>> f.close()
>>> f.close()
>>> 
>>> 
>>> content
["Imagine there's no heaven\n", "It's easy if you try\n", 'No hell below us\n', 'Above us only sky\n', 'Imagine all the people living for today\n', "Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> content[0]
"Imagine there's no heaven\n"
>>> content[0].strip()
"Imagine there's no heaven"
>>> newcontent = []
>>> for line in content:
	newcontent.append(line.strip())

	
>>> newcontent
["Imagine there's no heaven", "It's easy if you try", 'No hell below us', 'Above us only sky', 'Imagine all the people living for today', "Imagine there's no countries", "It isn't hard to do", 'Nothing to kill or die for', 'And no religion too', 'Imagine all the people living life in peace, you', "You may say I'm a dreamer", "But I'm not the only one", "I hope some day you'll join us", 'And the world will be as one', 'Imagine no possessions', 'I wonder if you can', 'No need for greed or hunger', 'A brotherhood of man', 'Imagine all the people sharing all the world, you', "You may say I'm a dreamer", "But I'm not the only one", "I hope some day you'll join us", 'And the world will be as one']
>>> text = ' '.join(newcontent)
>>> text
"Imagine there's no heaven It's easy if you try No hell below us Above us only sky Imagine all the people living for today Imagine there's no countries It isn't hard to do Nothing to kill or die for And no religion too Imagine all the people living life in peace, you You may say I'm a dreamer But I'm not the only one I hope some day you'll join us And the world will be as one Imagine no possessions I wonder if you can No need for greed or hunger A brotherhood of man Imagine all the people sharing all the world, you You may say I'm a dreamer But I'm not the only one I hope some day you'll join us And the world will be as one"
>>> 
>>> 
>>> words = text.split()
>>> words
['Imagine', "there's", 'no', 'heaven', "It's", 'easy', 'if', 'you', 'try', 'No', 'hell', 'below', 'us', 'Above', 'us', 'only', 'sky', 'Imagine', 'all', 'the', 'people', 'living', 'for', 'today', 'Imagine', "there's", 'no', 'countries', 'It', "isn't", 'hard', 'to', 'do', 'Nothing', 'to', 'kill', 'or', 'die', 'for', 'And', 'no', 'religion', 'too', 'Imagine', 'all', 'the', 'people', 'living', 'life', 'in', 'peace,', 'you', 'You', 'may', 'say', "I'm", 'a', 'dreamer', 'But', "I'm", 'not', 'the', 'only', 'one', 'I', 'hope', 'some', 'day', "you'll", 'join', 'us', 'And', 'the', 'world', 'will', 'be', 'as', 'one', 'Imagine', 'no', 'possessions', 'I', 'wonder', 'if', 'you', 'can', 'No', 'need', 'for', 'greed', 'or', 'hunger', 'A', 'brotherhood', 'of', 'man', 'Imagine', 'all', 'the', 'people', 'sharing', 'all', 'the', 'world,', 'you', 'You', 'may', 'say', "I'm", 'a', 'dreamer', 'But', "I'm", 'not', 'the', 'only', 'one', 'I', 'hope', 'some', 'day', "you'll", 'join', 'us', 'And', 'the', 'world', 'will', 'be', 'as', 'one']
>>> 
>>> 
>>> D = {}
>>> for word in words:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'Imagine': 6, "there's": 2, 'no': 4, 'heaven': 1, "It's": 1, 'easy': 1, 'if': 2, 'you': 4, 'try': 1, 'No': 2, 'hell': 1, 'below': 1, 'us': 4, 'Above': 1, 'only': 3, 'sky': 1, 'all': 4, 'the': 8, 'people': 3, 'living': 2, 'for': 3, 'today': 1, 'countries': 1, 'It': 1, "isn't": 1, 'hard': 1, 'to': 2, 'do': 1, 'Nothing': 1, 'kill': 1, 'or': 2, 'die': 1, 'And': 3, 'religion': 1, 'too': 1, 'life': 1, 'in': 1, 'peace,': 1, 'You': 2, 'may': 2, 'say': 2, "I'm": 4, 'a': 2, 'dreamer': 2, 'But': 2, 'not': 2, 'one': 4, 'I': 3, 'hope': 2, 'some': 2, 'day': 2, "you'll": 2, 'join': 2, 'world': 2, 'will': 2, 'be': 2, 'as': 2, 'possessions': 1, 'wonder': 1, 'can': 1, 'need': 1, 'greed': 1, 'hunger': 1, 'A': 1, 'brotherhood': 1, 'of': 1, 'man': 1, 'sharing': 1, 'world,': 1}
>>> 
>>> for key in D.keys():
	print(key.ljust(15) + ' | ' + D[key])

	
Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    print(key.ljust(15) + ' | ' + D[key])
TypeError: can only concatenate str (not "int") to str
>>> for key in D.keys():
	print(key.ljust(15) + ' | ' + str(D[key]))

	
Imagine         | 6
there's         | 2
no              | 4
heaven          | 1
It's            | 1
easy            | 1
if              | 2
you             | 4
try             | 1
No              | 2
hell            | 1
below           | 1
us              | 4
Above           | 1
only            | 3
sky             | 1
all             | 4
the             | 8
people          | 3
living          | 2
for             | 3
today           | 1
countries       | 1
It              | 1
isn't           | 1
hard            | 1
to              | 2
do              | 1
Nothing         | 1
kill            | 1
or              | 2
die             | 1
And             | 3
religion        | 1
too             | 1
life            | 1
in              | 1
peace,          | 1
You             | 2
may             | 2
say             | 2
I'm             | 4
a               | 2
dreamer         | 2
But             | 2
not             | 2
one             | 4
I               | 3
hope            | 2
some            | 2
day             | 2
you'll          | 2
join            | 2
world           | 2
will            | 2
be              | 2
as              | 2
possessions     | 1
wonder          | 1
can             | 1
need            | 1
greed           | 1
hunger          | 1
A               | 1
brotherhood     | 1
of              | 1
man             | 1
sharing         | 1
world,          | 1
>>> for key in D.keys():
	print(key + ' | ' + str(D[key]))

	
Imagine | 6
there's | 2
no | 4
heaven | 1
It's | 1
easy | 1
if | 2
you | 4
try | 1
No | 2
hell | 1
below | 1
us | 4
Above | 1
only | 3
sky | 1
all | 4
the | 8
people | 3
living | 2
for | 3
today | 1
countries | 1
It | 1
isn't | 1
hard | 1
to | 2
do | 1
Nothing | 1
kill | 1
or | 2
die | 1
And | 3
religion | 1
too | 1
life | 1
in | 1
peace, | 1
You | 2
may | 2
say | 2
I'm | 4
a | 2
dreamer | 2
But | 2
not | 2
one | 4
I | 3
hope | 2
some | 2
day | 2
you'll | 2
join | 2
world | 2
will | 2
be | 2
as | 2
possessions | 1
wonder | 1
can | 1
need | 1
greed | 1
hunger | 1
A | 1
brotherhood | 1
of | 1
man | 1
sharing | 1
world, | 1
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f.write('_' * 60 + '\n')
61
>>> f.write('\nWord Histogram\n')
16
>>> 
>>> f.write('Word'.ljust(15) + '|' + 'Occurances')
26
>>> f.write('-' * 60 + '\n')
61
>>> for key in D.keys():
	f.write(key.ljust(15) + ' | ' + str(D[key]))

	
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
19
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f.write('\n\n' + '_' * 60 + '\n')
63
>>> f.write('\nWord Histogram\n')
16
>>> f.write('Word'.ljust(15) + '|' + 'Occurances')
26
>>> f.write('\n\n' + '-' * 60 + '\n')
63
>>> for key in D.keys():
	f.write(key.ljust(15) + ' | ' + str(D[key] + '\n'))

	
Traceback (most recent call last):
  File "<pyshell#110>", line 2, in <module>
    f.write(key.ljust(15) + ' | ' + str(D[key] + '\n'))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for key in D.keys():
	f.write(key.ljust(15) + ' | ' + str(D[key]) + '\n')

	
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
20
>>> f.close()
>>> 
