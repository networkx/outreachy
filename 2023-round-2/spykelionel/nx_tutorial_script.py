import networkx as nx
import matplotlib.pyplot as plt

# Create a DiGraph object
G = nx.DiGraph()

# Add nodes of different types
nodes = [1, 'A', (2, 3), 'B', 4, (5, 6), 'C', 7, 'D', (8, 9)]

G.add_nodes_from(nodes)

# Add multiple edges between nodes
edges = [
    (1, 'A'),
    (1, (2, 3)),
    ('A', 'B'),
    ('A', 4),
    ((2, 3), (5, 6)),
    ('B', 'C'),
    ('B', 7),
    (4, 'C'),
    (4, 'D'),
    (7, (8, 9)),
    ('C', 'D'),
    ((5, 6), (8, 9)),
    ('D', (5, 6))
]

G.add_edges_from(edges)

# Find shortest paths between all pairs of nodes
shortest_paths = dict(nx.all_pairs_shortest_path(G))

# Print shortest paths
for source, paths in shortest_paths.items():
    for target, path in paths.items():
        if source != target:
            print(f"Shortest path from {source} to {target}: {path}")

# Plot the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold', font_color='black', edge_color='gray')
plt.title("Graph Visualization")
plt.show()
