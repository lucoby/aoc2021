import numpy as np

if __name__ == '__main__':
    a = np.array([[int(c) for c in l.strip()] for l in open("input1.txt")])
    r, c = a.shape
    expanded = np.zeros((r + 2, c + 2)) + 10
    expanded[1:-1, 1:-1] = a
    a = expanded
    total = 0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            up = a[i - 1, j]
            down = a[i + 1, j]
            left = a[i, j - 1]
            right = a[i, j + 1]
            if a[i, j] < up and a[i, j] < down and a[i, j] < left and a[i, j] < right:
                total += a[i, j] + 1
    print(total)
