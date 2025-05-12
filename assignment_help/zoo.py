import random
import time 
from threading import Thread

class Visitor:
    def __init__(self, people, priority):
        self.people = people
        self.priority = priority 

    def __str__(self):
        return "people: " + str(self.people) + ", priority: " + str(self.priority)

class Gate:
    def __init__(self, name, zoo):
        self.name = name
        self.zoo = zoo
        self.queue = []

    def run(self):
        while True:
            v = Visitor(random.randint(1, 5), random.randint(1, 4))
            print("WAIT:", v)
            self.queue.append(v)
            time.sleep(random.randint(1, 20))
            
            if random.randint(1, 100) > 80:
                # let visitor get in
                self.queue.sort(key=lambda x : x.priority)
                v = self.queue.pop(0)
                print("IN:", v)


class Zoo:
    def __init__(self):
        self.capacity_open = 300
        self.capacity_theater = 30
        self.open_visitors = []
        self.theater_visitors = []
        self.both_visitors = [] 

    def leave_zoo(self):
        pass


zoo = Zoo()
outth = Thread(zoo.leave_zoo)
outth.start()
gate = Gate("G1", zoo)
th = Thread(target=gate.run)
th.start()
gate = Gate("G2", zoo)
th = Thread(target=gate.run)
th.start()
gate = Gate("G3", zoo)
th = Thread(target=gate.run)
th.start()




