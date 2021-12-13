import numpy as np
from PIL import Image
from PIL.ImageOps import expand
import pytesseract


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

    return part1 | part2


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

        for f in folds:
            a = fold(a, f[0], int(f[1]))

        img = Image.fromarray(~a)
        factor = 5
        img = expand(img, border=2, fill=1).resize((img.size[0] * factor, img.size[1] * factor))

        # img.show()
        print(pytesseract.image_to_string(img))
