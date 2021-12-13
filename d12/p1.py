import networkx as nx


def find_paths(g, node, visited):
    if node == "end":
        return 1

    paths = 0

    for adjacent in g[node]:
        if adjacent[0].islower() and adjacent not in visited or adjacent[0].isupper():
            new_visited = visited.copy()
            new_visited.add(adjacent)
            paths += find_paths(g, adjacent, new_visited)

    return paths

if __name__ == '__main__':
    G = nx.Graph()
    with open("input1.txt") as f:
        for l in f:
            nodes = l.strip().split("-")
            G.add_edge(*nodes)

    print(find_paths(G, "start", set(["start"])))
