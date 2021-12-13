import numpy as np

def count_flashes(a, steps):
    shape = a.shape
    total = 0
    for i in range(steps):
        has_flashed = np.zeros(shape, dtype=bool)
        a += 1
        flashes = (a > 9) & ~has_flashed
        while np.any(flashes):
            for c in np.argwhere(flashes):
                a[max(0, c[0] - 1):min(shape[0], c[0] + 2), max(0, c[1] - 1):min(shape[1], c[1] + 2)] += 1
                has_flashed[c[0], c[1]] = True
                total += 1
            flashes = (a > 9) & ~has_flashed
        a[has_flashed] = 0
    return total

if __name__ == '__main__':
    a = np.array([[int(c) for c in l.strip()] for l in open("input1.txt")])
    flashes = count_flashes(a, 100)
    print(flashes)
