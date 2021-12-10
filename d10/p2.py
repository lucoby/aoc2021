from statistics import median

if __name__ == '__main__':
    with open("input1.txt") as f:
        scores = []
        points = {"(": 1, "[": 2, "{": 3, "<": 4}
        for l in f:
            stack = []
            completed = True
            for c in l.strip():
                if c in {"(", "[", "{", "<"}:
                    stack.append(c)
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == ">" and stack[-1] == "<":
                    stack.pop()
                else:
                    completed = False
                    break

            if completed:
                score = 0
                while len(stack) > 0:
                    score *= 5
                    score += points[stack.pop()]
                scores.append(score)
        print(median(scores))
