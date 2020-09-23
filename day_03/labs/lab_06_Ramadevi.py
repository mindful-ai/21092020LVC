import random
from datetime import datetime

dt = datetime.now()
start = dt.microsecond

L = []
for i in range(1000):
    L.append(random.randint(1, 100))
    
dt = datetime.now()
end = dt.microsecond

print ("Executiontime in milliseconds = " , end-start)
print ("Executiontime in seconds = " , (end-start)/1000000)
