import numpy as np
from numba import cuda


# A device function called from the actual kernel
@cuda.jit(device=True)
def compute(x, y, max_iters):
    c = complex(x, y)
    z = 0.0j
    iters = 0
    while ((z.real*z.real + z.imag*z.imag) < 4) and iters < max_iters:
        z = z**2 + c
        iters += 1
    return iters


@cuda.jit
def mandelbrot(x, y, result, max_iters):
    imax = x.shape[0]
    jmax = x.shape[1]
    i, j = cuda.grid(2)
    if i < imax and j < jmax:
        result[i, j] = compute(x[i, j], y[i, j], max_iters)


nx =  3200
ny = int(nx*3/4)
x, y = np.mgrid[-2.5:1.5:nx*1j, -1.5:1.5:ny*1j]
result = np.zeros((nx, ny))

threads = (32, 8)
blocks = int(np.ceil(nx/threads[0])), int(np.ceil(ny/threads[1]))

mandelbrot[blocks, threads](x, y, result, 40)

from matplotlib import pyplot as plt
plt.imshow(result)
plt.show()
