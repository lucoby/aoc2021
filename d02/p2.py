if __name__ == '__main__':
    x, y, aim = 0, 0, 0
    with open("input1.txt") as f:
        for l in f.readlines():
            direction, amount = l.split(" ")
            amount = int(amount)
            if direction == "forward":
                x += amount
                y += aim * amount
            elif direction == "down":
                aim += amount
            elif direction == "up":
                aim -= amount
        print(x * y)
