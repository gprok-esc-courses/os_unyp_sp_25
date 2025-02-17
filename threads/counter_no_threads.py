import time
import random

def counter(id):
    for i in range(5):
        print(id, i)
        time.sleep(random.randint(3, 10))


for id in range(5):
    counter(id)