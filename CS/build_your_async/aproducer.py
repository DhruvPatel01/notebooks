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
                    _, _, func = heapq.heappop(self.sleeping)
                    func()
            else:
                func = self.ready.popleft()
                func()

sched = Scheduler()

class AsyncQueue:
    def __init__(self):
        self.q = deque()
        self.waiting = deque()
    
    def put(self, item):
        self.q.append(item)
        if self.waiting:
            sched.call_soon(self.waiting.popleft())


    def get(self, func):
        if self.q:
            item = self.q.popleft()
            func(item)
        else:
            self.waiting.append(lambda: self.get(func))
        

def producer(q, n):
    def inner(x):
        if x < n:
            print("Producing", x)
            q.put(x)
            sched.call_later(1, lambda: inner(x+1))
        else:
            q.put(None)
    inner(0)

def consumer(q):
    def inner(item):
        if item is not None:
            print("Consuming", item)
            sched.call_later(2, lambda: consumer(q))
    q.get(inner)


q = AsyncQueue()
sched.call_soon(lambda: producer(q, 10))
sched.call_soon(lambda: consumer(q))
sched.run()