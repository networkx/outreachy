import networkx as nx

# Create a DiGraph
G = nx.DiGraph()

# Add nodes to the graph
nodes = [7, "Nabanita", ("ABCD", 56.8))
G.add_nodes_from(nodes)

# Add edges between the nodes
edges = [ (7, "Nabanita"), ("Nabanita", ("ABCD", 56.8)), (("ABCD", 56.8), 7),
	("Nabanita", 7) ]
G.add_edges_from(edges)

# Find shortest path b/w all pairs of nodes
paths = dict(nx.all_pairs_shortest_path(G))
for path in paths:
	print(path, paths[path])

# Plot the graph
nx.draw(G, with_labels=True, font_weight="bold")
