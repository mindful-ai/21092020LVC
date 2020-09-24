def getnumbers():
    #return list(range(5))

    yield 0
    yield 1
    yield 2
    yield 3
    yield 4
    




# --------------------------


r = getnumbers()

'''
for i in r:
    print(i)
'''

print(next(r))
print(next(r))

print('-'*30)

for i in r:
    print(i)

