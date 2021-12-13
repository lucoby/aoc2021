import numpy as np


def print_arr(a):
    for r in a:
        print("".join(["#" if c else " " for c in r]))


def fold(a, axis, pos):

    if axis == "y":
        part1 = a[:pos, :]
        part2 = a[-1:pos:-1, :]

    if axis == "x":
        part1 = a[:, :pos]
        part2 = a[:, -1:pos:-1]

    folded = part1 | part2
    print(folded.sum())


if __name__ == '__main__':
    with open("input1.txt") as f:
        pixels = []
        folds = []
        for l in f:
            if len(l) > 1 and l.startswith("fold along"):
                folds.append(l[11:].strip().split("="))
            elif len(l) > 1:
                pixels.append([int(i) for i in l.strip().split(",")])

        max_x = max(p[0] for p in pixels) + 1
        max_y = max(p[1] for p in pixels) + 1

        a = np.zeros((max_y, max_x), dtype=bool)

        for p in pixels:
            a[p[1], p[0]] = True

        fold(a, folds[0][0], int(folds[0][1]))

        # print_arr(a)
        # print(folds)
