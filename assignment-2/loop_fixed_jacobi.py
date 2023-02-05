# Rohan Rajesh Kalbag
# Roll: 20D170033


from argparse import ArgumentParser
import numpy as np
import time


def command_line_fetcher():
    # function to fetch command line arguments
    parser = ArgumentParser(description="jacobi assignment ae6102")
    parser.add_argument('--size',
                        type=int, required=True, help="size N of matrix")
    parser.add_argument('-n', '--niter',
                        type=int, required=True, help="number of iterations")
    parser.add_argument('--procedure', choices=['loop', 'list', 'numpy'],
                        required=True, help="the method to be performed")
    parser.add_argument('-o', "--output", required=True,
                        help="file name for output to be printed")
    return parser.parse_args()


def jacobi_loop(grid, N):
    temp_grid = np.empty_like(grid)
    for i in range(1, N-1):
        for j in range(1, N-1):
            temp_grid[i, j] = (grid[i+1, j]
                               + grid[i-1, j]
                               + grid[i, j+1]
                               + grid[i, j-1])*0.25
    grid[1:-1, 1:-1] = temp_grid[1:-1, 1:-1]


def jacobi_numpy_vectorized(grid):
    grid[1:-1, 1:-1] = (grid[2:, 1:-1]
                        + grid[:-2, 1:-1]
                        + grid[1:-1, 2:]
                        + grid[1:-1, :-2])*0.25


def jacobi_list_loop(T, niter):
    N = len(T)
    Tn = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(niter):
        for i in range(1, N-1):
            for j in range(1, N-1):
                Tn[i][j] = (T[i+1][j] + T[i-1][j] + T[i]
                            [j+1] + T[i][j-1]) * 0.25

        for i in range(1, N-1):
            for j in range(1, N-1):
                T[i][j] = Tn[i][j]


def two_dimensional_laplace_solver():
    # collect all the command line arguments
    args = command_line_fetcher()
    size = args.size
    niter = args.niter
    procedure = args.procedure
    filename = args.output

    # initialize the NxN numpy array grid with zeroes
    grid = np.zeros((size, size))
    grid_list = [[0 for _ in range(size)] for _ in range(size)]
    # top row is assigned to 100
    grid[0] = 100
    # right column is assigned to 100
    grid[:, -1] = 100
    for i in range(size):
        grid_list[i][-1] = 100
        grid_list[0][i] = 100

    if procedure == 'loop':
        benchmark_time = time.perf_counter()
        for i in range(niter):
            jacobi_loop(grid, size)
        benchmark_time = time.perf_counter() - benchmark_time
    elif procedure == 'numpy':
        benchmark_time = time.perf_counter()
        for i in range(niter):
            jacobi_numpy_vectorized(grid)
        benchmark_time = time.perf_counter() - benchmark_time
    else:
        grid_list = grid.tolist()
        benchmark_time = time.perf_counter()
        jacobi_list_loop(grid_list, niter)
        benchmark_time = time.perf_counter() - benchmark_time
        grid = np.array(grid_list)

    print(benchmark_time)
    np.savez(filename, grid)


if __name__ == '__main__':
    two_dimensional_laplace_solver()
