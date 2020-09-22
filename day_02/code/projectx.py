# Project X

# Accept data from the user
# Extract the minimum, maximum and seperate the prime numbers
# from the data


import primes
print("projectx.py ---> ", __name__)

# input

L = []
while True:
    uin = input(" -> (q to quit) ")
    if(uin.lower() == 'q'):
        break
    elif(uin.isdigit()):
        L.append(float(uin))

print(L)

# process

minimum = min(L)
maximum = max(L)
pn = []
for n in L:
    if(primes.checkprime(int(n))):
        pn.append(n)

# output

print('-' * 60)
print('MAXIMUM : ', maximum)
print('MINIMUM : ', minimum)
print('PRIMES  : ', pn)
