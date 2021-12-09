if __name__ == '__main__':
    with open("input1.txt") as f:
        for i, l in enumerate(f):
            l = l.strip()
            if i == 0:
                count = [0] * len(l)
            for j, c in enumerate(l):
                count[j] += c == "1"
        gamma = int("".join(["1" if c > i / 2 else "0" for c in count]), 2)
        epsilon = int("".join(["1" if c < i / 2 else "0" for c in count]), 2)
        print(epsilon * gamma)
