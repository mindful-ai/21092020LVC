# Program to out a message telling if the outcome is
# positive, negative or zero after subtraction

# input

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

# process

res = a - b

# output

if(res > 0):
    print("The result is positive")
elif(res < 0):
    print("The result is negative")
else:
    print("The result is zero")
