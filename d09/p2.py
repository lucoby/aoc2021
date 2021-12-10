import networkx as nx
import numpy as np

if __name__ == '__main__':
    a = np.array([[int(c) for c in l.strip()] for l in open("input1.txt")])

    r, c = a.shape
    g = nx.grid_2d_graph(r, c)
    g = nx.relabel_nodes(g, {(i, j): (i, j, a[i, j]) for i in range(r) for j in range(c)})
    g.remove_nodes_from([(i, j, 9) for i in range(r) for j in range(c)])

    subgraphs = nx.connected_components(g)
    subgraph_sizes = sorted([len(subgraph) for subgraph in subgraphs], reverse=True)
    
    print(subgraph_sizes[0] * subgraph_sizes[1] * subgraph_sizes[2])
