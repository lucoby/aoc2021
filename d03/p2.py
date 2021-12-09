import numpy as np
from operator import gt, lt


def filter_diagnostic(filtered, op, take):
    idx = 0
    while filtered.shape[0] > 1:
        count_ones = np.count_nonzero(filtered[:, idx])
        if count_ones == filtered.shape[0] / 2:
            filtered = filtered[filtered[:, idx] == take, :]
        elif op(count_ones, filtered.shape[0] / 2):
            filtered = filtered[filtered[:, idx] == 1, :]
        else:
            filtered = filtered[filtered[:, idx] == 0, :]
        idx += 1
    return int("".join([str(i) for i in filtered[0]]), 2)


if __name__ == '__main__':
    numbers = np.array([[int(c) for c in l.strip()] for l in open("input1.txt")])
    o2 = filter_diagnostic(numbers, gt, 1)
    co2 = filter_diagnostic(numbers, lt, 0)
    print(o2 * co2)
