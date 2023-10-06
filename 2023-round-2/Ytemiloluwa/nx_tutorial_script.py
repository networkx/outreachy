import networkx as nx
import matplotlib.pyplot as plt

# Create a DiGraph graph object
DG = nx.DiGraph()

# Adding nodes of multiple types (int, str, tuple)
DG.add_nodes_from([2, 'nodeA', (1, 1), 3, 'nodeB', (2, 2), 4, 'nodeC', (3, 3), 5])

# Adding multiple edges between nodes
edges = [(2, 'nodeA'), ('nodeA', (1, 1)), (3, 'nodeB'), ('nodeB', (2, 2)), (4, 'nodeC'), ('nodeC', (3, 3)), (5, 2), (5, 'nodeC')]
DG.add_edges_from(edges)

# Finding the shortest path between all pairs of nodes in this graph.
shortestPath = dict(nx.all_pairs_shortest_path(DG))
for source, path in shortestPath.items():
    for destination, path in path.items():
        print("Shortest path from", source, "to ", destination, "is -> ", path)

# Plotting the graph using networkx.draw
pos = nx.spring_layout(DG)
nx.draw(DG, pos, with_labels=True, node_size=500)
plt.title("A DiGraph")
plt.show()

