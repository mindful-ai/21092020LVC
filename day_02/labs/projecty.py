# Project Y


# Generate 100 random numbers
# 1. Filter out the fibonacci numbers
# 2. Filter out those numbers which are divisible by any of the last 7 of the
#    first 12 fibonacci numbers

import fibo
import random

rn = []
for i in range(100):
    rn.append(random.randint(1, 100))

print('RANDOM : ', rn)

print('-'*60)


# Part 1

fiboref = fibo.genfibo(12)

fn = []
for n in rn:
    if(n in fiboref):
        fn.append(n)
print('Number of Fibonacci numbers: ', len(fn))
print('FIBONACCI Series Numbers: ', fn)

# Part 2

fibodiv = fiboref[-7:]
fibolist = []
for n in rn:
    for d in fibodiv:
        if(n % d == 0):
            fibolist.append(n)
            break
print('Length of FIBOLIST: ', len(fibolist))
print('FIBOLIST: ', fibolist)           
