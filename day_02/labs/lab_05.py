# Print a multiplication table


# input
n = int(input('Enter a number: '))

# process
# output

f = open(r"yourpath", "w")
for i in range(1, 11):
    f.write(str(n) + ' X ' + str(i) + ' = ' + str(n * i) + '\n')

f.close()
