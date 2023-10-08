import networkx as nx
import matplotlib.pyplot as plt

# Create a NetworkX DiGraph graph object
G = nx.DiGraph()

# Add nodes of multiple type
G.add_node(1, node_type='int')
G.add_node('A', node_type='str')
G.add_node((2, 3), node_type='tuple')
G.add_node('B', node_type='str')
G.add_node(4, node_type='int')
G.add_node('C', node_type='str')
G.add_node('D', node_type='str')
G.add_node((5, 6), node_type='tuple')
G.add_node('E', node_type='str')
G.add_node(7, node_type='int')

# Add multiple edges between these nodes
G.add_edge(1, 'A')
G.add_edge('A', (2, 3))
G.add_edge('A', 'B')
G.add_edge('B', 4)
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('C', (5, 6))
G.add_edge('C', 'E')
G.add_edge((5, 6), 7)
G.add_edge(7, 1)

# Find the shortest path between all pairs of nodes in the graph
shortest_paths = dict(nx.all_pairs_shortest_path(G))

# Print shortest paths
for source_node, paths in shortest_paths.items():
    for target_node, path in paths.items():
        if source_node != target_node:
            print(f"Shortest path from {source_node} to {target_node}: {path}")

# Plot the graph using networkx.draw
pos = nx.spring_layout(G, seed=42)  
node_colors = {'int': 'red', 'str': 'blue', 'tuple': 'green'}
node_colors_list = [node_colors[data['node_type']] for _, data in G.nodes(data=True)]
nx.draw(G, pos, with_labels=True, node_color=node_colors_list)
plt.show()