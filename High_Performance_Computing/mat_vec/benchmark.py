import numpy as np
import numba as nb
import gemv

import time
import matplotlib.pyplot as plt
batch_sizes = [10, 50, 100, 500, 1000]

for bs in batch_sizes:
    print("BS = ", bs)
    c = []
    d = []

    for i in range(10_000):
        A = np.random.randn(bs, 128)
        x = np.random.randn(128)
        y = np.zeros(bs)
        
        tic = time.perf_counter()
        np.dot(A, x, out=y)
        toc = time.perf_counter()
        c.append(toc-tic)

        tic = time.perf_counter()
        gemv.blis_dgemv(A, x, y)
        toc = time.perf_counter()
        d.append(toc-tic)

        
    mean = round(np.mean(c)*10**6, 4)
    std = round(np.std(c)*10**6, 4)
    print("NMPY", mean, "+-", std)

    mean = round(np.mean(d)*10**6, 4)
    std = round(np.std(d)*10**6, 4)
    print("BLIS", mean, "+-", std)
    
    time.sleep(30)
    print()
    

