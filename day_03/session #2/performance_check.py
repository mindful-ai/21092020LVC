import random
from datetime import datetime

t_before = datetime.now()

for i in range(1000):
    s = "imagination is more important than knowledge"
    '''
    words = s.split()
    newwords = []
    for word in words:
            newwords.append(word.capitalize())
    ' '.join(newwords)
    '''
    ' '.join([word.capitalize() for word in s.split()])

t_after = datetime.now()


print(t_after - t_before)


