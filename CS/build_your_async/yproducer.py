from collections import deque
import time
import heapq

class Awaitable:
    def __await__(self):
        yield

def switch():
    return Awaitable()

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.current = None
        self.sleeping = []
        self.counter = 0

    def new_task(self, coro):
        self.ready.append(coro)

    async def sleep(self, delay):
        deadline = time.time() + delay
        self.counter += 1
        heapq.heappush(self.sleeping, (deadline, self.counter, self.current))
        self.current = None
        await switch()

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                deadline, _, coro = heapq.heappop(self.sleeping)
                delta =  deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(coro)

            self.current = self.ready.popleft()
            try:
                self.current.send(None)
                if self.current:
                    self.ready.append(self.current)
            except StopIteration:
                pass

class AsyncQueue:
    def __init__(self):
        self.q = deque()
        self.waiting = deque()

    async def put(self, item):
        self.q.append(item)
        if self.waiting:
            sched.ready.append(self.waiting.popleft())
        
    async def get(self):
        if not self.q:
            self.waiting.append(sched.current)
            sched.current = None
            await switch()
        return self.q.popleft()


# ----
async def producer(q, n):
    for i in range(n):
        print("Producing", i)
        await q.put(i)
        await sched.sleep(1)
    await q.put(None)

async def consumer(q):
    while True:
        item = await q.get()
        if item is None:
            break
        print("Consuming", item)

q = AsyncQueue()
sched = Scheduler()
sched.new_task(producer(q, 10))
sched.new_task(consumer(q))
sched.run()