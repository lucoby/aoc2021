if __name__ == '__main__':
    increases = 0
    with open("input1.txt") as f:
        prev = int(f.readline().strip())
        for l in f.readlines():
            cur = int(l.strip())
            increases += cur > prev
            prev = cur
    print(increases)
