from d06.p1 import get_num_fish

if __name__ == '__main__':
    with open("input1.txt") as f:
        state = [0] * 9
        initial = [int(i) for i in f.readline().strip().split(",")]
        for i in initial:
            state[i] += 1
        print(get_num_fish(state, 256))
