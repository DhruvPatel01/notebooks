import time
from collections import deque
import heapq

class Awaitable:
    def __await__(self):
        yield

def switch():
    return Awaitable()

class Scheduler:
    def __init__(self):
        self.waiting = deque()
        self.current = None
        self.sleeping = []
        self.counter = 0

    def new_task(self, coro):
        self.waiting.append(coro)

    async def sleep(self, delay):
        deadline = time.time() + delay
        self.counter += 1
        heapq.heappush(self.sleeping, (deadline, self.counter, self.current))
        self.current = None
        await switch()

    def run(self):
        while self.waiting or self.sleeping:
            if not self.waiting:
                deadline, _, coro = heapq.heappop(self.sleeping)
                delta =  deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.waiting.append(coro)

            self.current = self.waiting.popleft()
            try:
                self.current.send(None)
                if self.current:
                    self.waiting.append(self.current)
            except StopIteration:
                pass


async def countdown(n):
    while n>0:
        print('Down', n)
        await sched.sleep(1)
        n -= 1

async def countup(stop):
    x = 0
    while x < stop:
        print('Up', x)
        await sched.sleep(1)
        x += 1

sched = Scheduler()
sched.new_task(countdown(5))
sched.new_task(countup(5))
sched.run()