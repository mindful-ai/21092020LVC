# -------------------------------------------------
# LAB 1
# -------------------------------------------------

L = ['red', 'red', 'green', 'blue', 'orange']

L.remove('red')

L.append('golden')

L1 = []
for item in L:
    L1.append(item[::-1])

L1.sort(reverse=True)
L = L1

print(L)

# OUTPUT > ['neerg', 'nedlog', 'eulb', 'egnaro', 'der']

