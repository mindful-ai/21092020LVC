# input

n = int(input('Enter a number: '))

# process
# output

for i in range(2, n):
    if(n % i == 0):
        print('The number is not prime')
        break
else:
    print('The number is prime')


    
