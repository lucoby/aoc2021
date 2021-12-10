from statistics import median

if __name__ == '__main__':
     pos = [int(i) for i in open("input1.txt").readline().strip().split(",")]
     med = median(pos)
     dist = sum([abs(med - p) for p in pos])
     print(dist)
