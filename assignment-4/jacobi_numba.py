# Rohan Rajesh Kalbag
# Roll: 20D170033


from argparse import ArgumentParser
# import matplotlib.pyplot as plt
import numpy as np
import time
import numba


def command_line_fetcher():
    # function to fetch command line arguments
    parser = ArgumentParser(description="jacobi assignment ae6102")
    parser.add_argument('--size',
                        type=int, required=True, help="size N of matrix")
    parser.add_argument('-n', '--niter',
                        type=int, required=True, help="number of iterations")
    parser.add_argument('--procedure', choices=['loop', 'numba', 'numpy'],
                        required=True, help="the method to be performed")
    parser.add_argument('-o', "--output", required=True,
                        help="file name for output to be printed")
    # parser.add_argument('-v', "--vis", action='store_true',
    #                     help="visualize grid")
    return parser.parse_args()


@numba.njit
def jacobi_loop_numba(grid, N):
    temp_grid = np.empty_like(grid)
    for i in range(1, N-1):
        for j in range(1, N-1):
            temp_grid[i, j] = (grid[i+1, j]
                               + grid[i-1, j]
                               + grid[i, j+1]
                               + grid[i, j-1])*0.25
    grid[1:-1, 1:-1] = temp_grid[1:-1, 1:-1]


@numba.njit
def jacobi_numpy_numba_vectorized(grid):
    grid[1:-1, 1:-1] = (grid[2:, 1:-1]
                        + grid[:-2, 1:-1]
                        + grid[1:-1, 2:]
                        + grid[1:-1, :-2])*0.25


def jacobi_numpy_vectorized(grid):
    grid[1:-1, 1:-1] = (grid[2:, 1:-1]
                        + grid[:-2, 1:-1]
                        + grid[1:-1, 2:]
                        + grid[1:-1, :-2])*0.25


def two_dimensional_laplace_solver():
    # collect all the command line arguments
    args = command_line_fetcher()
    size = args.size
    niter = args.niter
    procedure = args.procedure
    filename = args.output
    # visualize = args.vis
    # initialize the NxN numpy array grid with zeroes
    grid = np.zeros((size, size))
    # top row is assigned to 100
    grid[0] = 100
    # right column is assigned to 100
    grid[:, -1] = 100

    # main jacobi calculation
    if procedure == 'loop':
        # dummy calls to allow numba to analyze code
        jacobi_loop_numba(grid, size)
        benchmark_time = time.perf_counter()
        for i in range(niter):
            jacobi_loop_numba(grid, size)
        benchmark_time = time.perf_counter() - benchmark_time
    elif procedure == 'numpy':
        benchmark_time = time.perf_counter()
        for i in range(niter):
            jacobi_numpy_vectorized(grid)
        benchmark_time = time.perf_counter() - benchmark_time
    else:
        # dummy calls to allow numba to analyze code
        jacobi_numpy_numba_vectorized(grid)
        benchmark_time = time.perf_counter()
        for i in range(niter):
            jacobi_numpy_numba_vectorized(grid)
        benchmark_time = time.perf_counter() - benchmark_time

    print(f"{benchmark_time}")

    # if visualize:
    #     plt.imshow(grid)
    #     plt.colorbar()
    #     plt.show()

    np.savez(filename, grid)


if __name__ == '__main__':
    two_dimensional_laplace_solver()
