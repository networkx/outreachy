import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph object
G = nx.DiGraph()

# Add nodes of different types (int, str, tuple)
G.add_node(1)
G.add_node("aam")
G.add_node((3, 4))

# Add multiple edges between nodes
G.add_edge(1, "aam")
G.add_edge("aam", (3, 4))
G.add_edge((3, 4), 4)

# Add more nodes and edges (up to 10 nodes)
G.add_edges_from([('a', 'b'),('aam', 1),(9, (3, 4)), (9, 1),
    ('aam', 9),
    ((3, 4), 0),
    ('a', 9),
    (0, 'b')])

# Find and print the shortest path between all pairs of nodes
for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 != node2:
            if nx.has_path(G, source=node1, target=node2):
                shortest_path = nx.shortest_path(G, source=node1, target=node2)
                print(f"Shortest path from {node1} to {node2}: {shortest_path}")
            else:
                print(f"No path from {node1} to {node2}")

# Plot the graph
pos = nx.spring_layout(G, seed=42)  # Positioning nodes for visualization
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue')
plt.title("Directed Graph")
plt.show()
