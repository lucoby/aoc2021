import numpy as np

from d05.p1 import Line, get_point

if __name__ == '__main__':
    with open("input1.txt") as f:
        lines = []
        for l in f:
            start, end = l.strip().split(" -> ")
            line = Line(start=get_point(start), end=get_point(end))
            lines.append(line)

        max_x, max_y = 0, 0
        for l in lines:
            max_x = max(max_x, l.start.x, l.end.x)
            max_y = max(max_y, l.start.y, l.end.y)

        map = np.zeros((max_y + 1, max_x + 1))

        for l in lines:
            map[l.get_y_range(), l.get_x_range()] = map[l.get_y_range(), l.get_x_range()] + 1

        print(len(map[map >= 2]))
