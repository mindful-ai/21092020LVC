# -------------------------------------------------
# LAB 6 - Determine the time taken to run the loop
# -------------------------------------------------

import random
from datetime import datetime

t_before = datetime.now()

L = []
for i in range(1000):
  L.append(random.randint(1, 100))

t_after = datetime.now()

print("Time elapsed: ", t_after - t_before)
