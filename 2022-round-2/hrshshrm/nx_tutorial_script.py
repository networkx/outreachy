import networkx as nx

# Create a NetworkX DiGraph graph object
DG = nx.DiGraph()

# Add nodes of multiple types to this graph object
listOfNodes = [ 1, 7, ("NetworkX", "Outreachy"), "DiGraph", ("Agent", 47), "2B" ]
DG.add_nodes_from(listOfNodes)

# Add multiple edges between these nodes
listOfEdges = [
    (1, 7),
    (1, "2B"),
    (1, ("Agent", 47)),
    (7, "2B"),
    (7, "DiGraph"),
    (("NetworkX", "Outreachy"), "DiGraph"),
    (("NetworkX", "Outreachy"), 7),
    (("NetworkX", "Outreachy"), ("Agent", 47)),
    (("Agent", 47), 1),
    ("2B", "DiGraph"),
    ("2B", ('NetworkX', 'Outreachy'),)
]
DG.add_edges_from(listOfEdges)

# Find the shortest path between all pairs of nodes in this graph and print them.
shortestPaths = dict(nx.all_pairs_shortest_path(DG))
for key in shortestPaths:
    print(key, shortestPaths[key])

# Plot the graph using networkx.draw
nx.draw(DG, nx.shell_layout(DG), with_labels=True, font_weight="bold")
