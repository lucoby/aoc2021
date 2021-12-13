import networkx as nx


def is_valid_adjacent(adjacent, visited, visited_small_twice):
    return (
            adjacent[0].islower() and adjacent not in visited and visited_small_twice
            or adjacent != "start" and adjacent[0].islower() and not visited_small_twice
            or adjacent[0].isupper()
    )


def find_paths(g, node, visited, visited_small_twice):
    if node == "end":
        return 1

    paths = 0

    for adjacent in g[node]:
        if is_valid_adjacent(adjacent, visited, visited_small_twice):
            new_visited_small_twice = visited_small_twice or adjacent[0].islower() and not visited_small_twice and adjacent in visited
            new_visited = visited.copy()
            new_visited.add(adjacent)
            paths += find_paths(g, adjacent, new_visited, new_visited_small_twice)

    return paths


if __name__ == '__main__':
    G = nx.Graph()
    with open("input1.txt") as f:
        for l in f:
            nodes = l.strip().split("-")
            G.add_edge(*nodes)

    print(find_paths(G, "start", {"start"}, False))
