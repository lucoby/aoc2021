def get_num_fish(state, days):
    for i in range(days):
        state = [state[1], state[2], state[3], state[4], state[5], state[6], state[0] + state[7], state[8], state[0]]
    return sum(state)


if __name__ == '__main__':
    with open("input1.txt") as f:
        state = [0] * 9
        initial = [int(i) for i in f.readline().strip().split(",")]
        for i in initial:
            state[i] += 1
        print(get_num_fish(state, 80))
