import time
from collections import deque

class Scheduler:
    def __init__(self):
        self.waiting = deque()
        self.current = None

    def new_task(self, gen):
        self.waiting.append(gen)

    def run(self):
        while self.waiting:
            self.current = self.waiting.popleft()
            try:
                next(self.current)
                if self.current:
                    self.waiting.append(self.current)
            except StopIteration:
                pass


def countdown(n):
    while n>0:
        print('Down', n)
        time.sleep(1)
        yield
        n -= 1

def countup(stop):
    x = 0
    while x < stop:
        print('Up', x)
        time.sleep(1)
        yield
        x += 1

sched = Scheduler()
sched.new_task(countdown(5))
sched.new_task(countup(5))
sched.run()