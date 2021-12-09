if __name__ == '__main__':
    x, y = 0, 0
    with open("input1.txt") as f:
        for l in f.readlines():
            direction, amount = l.split(" ")
            amount = int(amount)
            if direction == "forward":
                x += amount
            elif direction == "down":
                y += amount
            elif direction == "up":
                y -= amount
        print(x * y)
