import shelve

D = { 'name':'Ram', 'age':35, 'country':'Netherlands' }
L = ['red', 'green', 'blue']
M = [[1, 2, 4], [1, 3, 5], [6, 7, 8]]

f = shelve.open("mydata.db")

f['dict'] = D
f['colorlist'] = L
f['matrix'] = M

f.sync()
f.close()
