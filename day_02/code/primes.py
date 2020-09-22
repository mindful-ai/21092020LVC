# -------------------------------------------------
# LAB 2 - Determine if a number is prime or not
# -------------------------------------------------

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

print("primes.py ---> ", __name__)

if __name__ == '__main__' :
    
    # input

    x = int(input('Enter a number: '))

    # process

    if(checkprime(x)):
        print('The number is prime')
    else:
        print('The number is not prime')
