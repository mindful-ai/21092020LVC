# Program to calculate the height of the building
# given angle of sight and distance of the measurer from the building

import math

# input

a = float(input("Enter the angle of sight in deg: "))
d = float(input("Enter the distance in mts: "))

# process

h = d * math.tan(math.radians(a))
h = h * 3.281

# output

# print('The height of the building is ', h, ' ft')
print('The height of the building is %.2f ft' % h)
