Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import os.path
>>> import shutil
>>> 
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_03\session #2\mydir"
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(path)
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_03\\session #2\\mydir'
>>> os.listdir()
['data1.txt', 'data2.txt', 'data3.txt', 'road.jpg', 'sunflower.jpg']
>>> 
>>> 
>>> 
>>> # ----------------------------- create directories
>>> 
>>> s = 'data1.txt'
>>> s[-3:]
'txt'
>>> s = 'file.io'
>>> s[-3:]
'.io'
>>> os.path.splitext(s)
('file', '.io')
>>> os.path.splitext(s)[1]
'.io'
>>> os.path.splitext(s)[1][1:]
'io'
>>> exts = [os.path.splitext(s)[1][1:] for s in os.listdir()]
>>> exts
['txt', 'txt', 'txt', 'jpg', 'jpg']
>>> 
>>> set(exts)
{'jpg', 'txt'}
>>> exts = set([os.path.splitext(s)[1][1:] for s in os.listdir()])
>>> exts
{'jpg', 'txt'}
>>> 
>>> # ---------------------------------------------- create the directories
>>> 
>>> exts
{'jpg', 'txt'}
>>> for ext in exts:
	os.mkdir(ext)

	
>>> # ------------------------------------------------- Movinf files
>>> 
>>> src = 'data1.txt'
>>> # dest = 'txt/data1.txt'
>>> os.path.splitext(src)[1][1:]
'txt'
>>> os.path.join(os.path.splitext(src)[1][1:], src)
'txt\\data1.txt'
>>> shutil.move(src, os.path.join(os.path.splitext(src)[1][1:], src))
'txt\\data1.txt'
>>> 
>>> 
>>> os.listdir()
['data1.txt', 'data2.txt', 'data3.txt', 'jpg', 'road.jpg', 'sunflower.jpg', 'txt']
>>> os.path.isfile('jpg')
False
>>> os.path.isfile('data1.txt')
True
>>> 
>>> for item in os.listdir():
	if(os.path.isfile(item)):
		src = item;
		dest = os.path.splitext(src)[1][1:]
		shutil.move(src, dest)

		
'txt\\data1.txt'
'txt\\data2.txt'
'txt\\data3.txt'
'jpg\\road.jpg'
'jpg\\sunflower.jpg'
>>> 
