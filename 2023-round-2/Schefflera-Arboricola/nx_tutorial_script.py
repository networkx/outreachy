import networkx as nx
import matplotlib.pyplot as plt

# Creating a NetworkX DiGraph (Directed Graph) object
G=nx.DiGraph()

# Adding nodes of different types
nodes = [1, 'A', (3, 4), 'B', 5, 'C', (6, 7), 8, 'D', 'E']

G.add_nodes_from(nodes)

# Adding multiple edges between nodes
edges = [(1, 'A'), ('A', (3, 4)), ('A', 5), ((3, 4), 'B'), (5, 'B'), ('B', 8), (8, 'C'), ('C', 'D'), ('D', 'E'), ('E', 1)]

G.add_edges_from(edges)

# Finding the shortest path between all pairs of nodes
shortest_paths=dict(nx.all_pairs_shortest_path(G))

# Printing the shortest paths
for source_node, paths in shortest_paths.items():
    for target_node,path in paths.items():
        if source_node!=target_node:
            print("Shortest path from node",source_node, "to node",target_node, "is : ", path)

# Plotting the graph using networkx.draw
pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500)
plt.title('Directed Graph')
plt.show()