from dataclasses import dataclass
import numpy as np


@dataclass
class Point:
    x: int
    y: int

def get_point(s):
    x, y = s.split(",")
    return Point(x=int(x), y=int(y))


@dataclass
class Line:
    start: Point
    end: Point

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x
    
    def get_x_range(self):
        if self.end.x == self.start.x:
            return self.end.x
        step = 1 if self.end.x > self.start.x else -1
        return range(self.start.x, self.end.x + step, step)
    
    def get_y_range(self):
        if self.end.y == self.start.y:
            return self.end.y
        step = 1 if self.end.y > self.start.y else -1
        return range(self.start.y, self.end.y + step, step)


if __name__ == '__main__':
    with open("ex1.txt") as f:
        lines = []
        for l in f:
            start, end = l.strip().split(" -> ")
            line = Line(start=get_point(start), end=get_point(end))
            if line.is_horizontal() or line.is_vertical():
                lines.append(line)

        max_x, max_y = 0, 0
        for l in lines:
            max_x = max(max_x, l.start.x, l.end.x)
            max_y = max(max_y, l.start.y, l.end.y)

        map = np.zeros((max_y + 1, max_x + 1))

        for l in lines:
            map[l.get_y_range(), l.get_x_range()] = map[l.get_y_range(), l.get_x_range()] + 1

        print(len(map[map >= 2]))
