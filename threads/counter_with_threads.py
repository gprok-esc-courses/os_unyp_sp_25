import time
import random
from threading import Thread

def counter(id):
    for i in range(5):
        print(id, i)
        time.sleep(random.randint(3, 10))


threads = []
for id in range(5):
    th = Thread(target=counter, args=(id,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()
print("DONE!")