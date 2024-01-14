import time
from collections import deque
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = []
        self._counter = 0

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        deadline = time.time() + delay
        heapq.heappush(self.sleeping, (deadline, self._counter, func))
        self._counter += 1

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                if self.sleeping[0][0] <= time.time():
                    _, func = heapq.heappop(self.sleeping)
                    func()
            else:
                func = self.ready.popleft()
                func()
        

sched = Scheduler()

def countdown(n):
    if n > 0:
        print('Down', n)
        sched.call_later(4, lambda : countdown(n-1))

def countup(stop):
    def inner(x):
        if x < stop:
            print('Up', x)
            sched.call_later(1, lambda: inner(x+1))
    inner(0)

sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(20))
sched.run()