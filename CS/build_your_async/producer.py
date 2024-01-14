import queue
import threading

def producer(q, n):
    for i in range(n):
        print("Producing", i)
        time.sleep(1)
        q.put(i)


    q.put(None)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("Consuming", item)

q = queue.Queue()
threading.Thread(target=producer, args=(q, 10)).start()
threading.Thread(target=consumer, args=(q, )).start()