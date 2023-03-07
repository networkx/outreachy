import networkx as nx

#Creating a Directional Graph
DG1 = nx.DiGraph()

#adding nodes to the directional graph
DG1.add_nodes_from([20, ("EaZy", 32.56), "Naman", 62.21])

#adding edges
edges = [(20, "Naman"), (20, 62.21), (20, ("EaZy", 32.56)), ("Naman",("EaZy", 32.56)), ("Naman", 62.21), (("EaZy", 32.56), 62.21)]

DG1.add_edges_from(edges)

#printing the shortest path
paths = dict(nx.all_pairs_shortest_path(DG1))
for path in paths:
	print(path, paths[path])

#drawing the graph
nx.draw(DG1, with_labels=True)
