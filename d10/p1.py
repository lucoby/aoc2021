if __name__ == '__main__':
    with open("input1.txt") as f:
        total = 0
        score = {")": 3, "]": 57, "}": 1197, ">": 25137}
        for l in f:
            stack = []
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
                    total += score[c]
                    break
        print(total)
