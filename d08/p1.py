if __name__ == '__main__':
    total = 0
    with open("input1.txt") as f:
        for l in f:
            outputs = l.strip().split(" | ")[1]
            unique = [len(o) in set([2, 3, 4, 7]) for o in outputs.split(" ")]
            total += sum(unique)
        print(total)
