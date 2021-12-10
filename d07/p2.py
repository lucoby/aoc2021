from statistics import mean

if __name__ == '__main__':
    pos = [int(i) for i in open("input1.txt").readline().strip().split(",")]
    avg = round(mean(pos))
    dists = [sum([(avg + a - p) ** 2 + abs(avg + a - p) for p in pos]) / 2 for a in range(-2, 3)]
    print(min(dists))
