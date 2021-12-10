def get_map(ins):
    map = {}
    ins = [set(i) for i in ins.split(" ")]

    d1 = [d for d in ins if len(d) == 2][0]
    d7 = [d for d in ins if len(d) == 3][0]
    d4 = [d for d in ins if len(d) == 4][0]
    d8 = [d for d in ins if len(d) == 7][0]

    d235 = [d for d in ins if len(d) == 5]
    d069 = [d for d in ins if len(d) == 6]

    map["a"] = d7 - d1

    for d in d069:
        if not d >= d1:
            # d is 6
            d6 = d
            map["f"] = d6 & d1
            map["c"] = d1 - map["f"]
        elif not d >= d4:
            d0 = d
            map["d"] = d4 - d0
        else:
            d9 = d
            map["e"] = d8 - d9

    for d in d235:
        if d >= d7:
            d3 = d
            map["b"] = d8 - d3 - map["e"]
            map["g"] = d3 - d7 - d4

    return {k: map[k].pop() for k in map}
    # return map

def map_digit(map, digit):
    if len(digit) == 2:
        return "1"
    elif len(digit) == 3:
        return "7"
    elif len(digit) == 4:
        return "4"
    elif len(digit) == 7:
        return "8"
    elif len(digit) == 6:
        if map["d"] not in digit:
            return "0"
        if map["c"] not in digit:
            return "6"
        return "9"
    elif len(digit) == 5:
        if map["b"] in digit:
            return "5"
        if map["f"] in digit:
            return "3"
        return "2"


def map_output(map, outs):
    digits = "".join([map_digit(map, set(i)) for i in outs.split(" ")])
    return int(digits)


if __name__ == '__main__':
    total = 0
    with open("input1.txt") as f:
        for l in f:
            ins, outs = l.strip().split(" | ")
            map = get_map(ins)
            number = map_output(map, outs)
            total += number
        print(total)
