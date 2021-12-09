from collections import deque

if __name__ == '__main__':
    increases = 0
    window = deque()
    with open("input1.txt") as f:
        for l in f.readlines():
            cur = int(l)
            if len(window) < 3:
                window.append(cur)
                if len(window) == 3:
                    running_sum = sum(window)
            else:
                left = window.popleft()
                increases += running_sum - left + cur > running_sum
                running_sum += cur - left
                window.append(cur)

    print(increases)
