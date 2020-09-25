import shelve

f = shelve.open('mydata.db')

L = f['colorlist']
M = f['matrix']
D = f['dict']

f.close()

print(L, type(L))
print(M, type(M))
print(D, type(D))

