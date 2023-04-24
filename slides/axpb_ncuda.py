import time
import numpy as np
from numba import cuda


@cuda.jit
def axpb(y, x, a, b):
    i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    if i < y.size:
        y[i] = a*x[i] + b


n = 1000000
x = np.linspace(0, 1, n)
y = np.zeros_like(x)
a = 2.0
b = 3.0

xd = cuda.to_device(x)
yd = cuda.to_device(y)

threads = 1
blocks = int(np.ceil(n/threads))

axpb[blocks, threads](yd, xd, a, b)
repeat = 100
#t1 = time.perf_counter()
#for i in range(repeat):
#    axpb[blocks, threads](yd, xd, a, b)

#print((time.perf_counter() - t1)/repeat)

#yd.copy_to_host(y)
#print(y)
#cuda.detect()
