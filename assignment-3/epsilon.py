# Rohan Rajesh Kalbag
# Roll: 20D170033


import numpy as np


def get_single_precision_float_epsilon():
    # we define np.float32 constants to emulate single precision floats
    eps = np.array(1.0, dtype=np.float32)
    one = np.array(1.0, dtype=np.float32)
    half = np.array(0.5, dtype=np.float32)

    while (one + eps) > one:
        eps = eps*half
    return eps


def get_double_precision_float_epsilon():
    # regular python floats are double precision
    eps = 1.0

    while (1.0 + eps) > 1.0:
        eps = eps*0.5
    return eps


if __name__ == '__main__':
    single_point_eps = str(get_single_precision_float_epsilon())
    double_point_eps = str(get_double_precision_float_epsilon())
    print(double_point_eps + ", " + single_point_eps)
