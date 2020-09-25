#f = open('xyz.py')

D = {}

try:
    D['name'] = 'Raj'
    c = 10/2
    f = open('xyz.py')
except FileNotFoundError:
    print('File not found in the directory')
except ZeroDivisionError:
    print('Cannot divide by zero')
except Exception as E:
    print('Some other error -> ' + str(E))
else:
    content = f.read()
    f.close()
    print(content)
finally:
    print('Operation Done!')



a = 10
b = 20
print(a + b)
print('Thank you!')

