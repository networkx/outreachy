import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_node(1)
G.add_node("A")
G.add_node((2, 3))
G.add_node("B")
G.add_node(4)
G.add_node("C")
G.add_node((5, 6))
G.add_node(7)
G.add_node(8)
G.add_node("D")

# Add edges between nodes
G.add_edge(1, "A")
G.add_edge("A", (2, 3))
G.add_edge((2, 3), "A")
G.add_edge("A", "B")
G.add_edge(4, "B")
G.add_edge("C", (5, 6))
G.add_edge(7, 8)
G.add_edge("D", 4)

# Find and print shortest paths between nodes
shortest_paths = dict(nx.all_pairs_shortest_path(G))
for source, paths in shortest_paths.items():
    for target, path in paths.items():
        if source != target:
            print(f"Shortest path from {source} to {target}: {path}")

# Plot the graph
nx.draw(G, with_labels=True)
plt.show()
