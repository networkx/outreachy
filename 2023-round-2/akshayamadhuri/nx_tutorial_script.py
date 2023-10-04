import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph object
G = nx.DiGraph()

# Add nodes of different types 
G.add_node(1)
G.add_node("Adam")
G.add_node((2, 3))

# Add multiple edges between nodes
G.add_edge(1, "Adam")
G.add_edge("Adam", (2, 3))
G.add_edge((2, 3), 1)

# Add more nodes and edges 
G.add_nodes_from([4, "Bob", (4, 5), "Charlie", (6, 7), 8])
G.add_edges_from([(4, "Bob"), ("B", (4, 5)), (1, "Charlie"), ((6, 7), 8)])

# Find and print the shortest path between all pairs of nodes
for node1 in G.nodes():
    for node2 in G.nodes():
        if node1 != node2:
            shortest_path = nx.shortest_path(G, source=node1, target=node2)
            print(f"Shortest path from {node1} to {node2}: {shortest_path}")

# Plot the graph
pos = nx.spring_layout(G, seed=42)  # Positioning nodes for visualization
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue')
plt.title("Directed Graph")
plt.show()
