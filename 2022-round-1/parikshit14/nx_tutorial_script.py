import networkx as nx
import matplotlib.pyplot as plt

# creating DiGraph object
DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (2, 3)])  # adding node 1,2,3 and connecting them 1->2->3
DG.add_edge("hello", "world")  # adding node and connecting them "hello" -> "world"
DG.add_edge("world", (5, 6))  # adding node (5,6) and connecting them "world" -> (5,6)
DG.add_edge(1, (5, 6))  # adding edge 1 -> (5,6)
DG.add_edge(1, "world")  # adding edge 1 -> "world"

# Drawing the DiGraph
nx.draw(DG, with_labels=True)

# Calculating the shortest path and printing it
sp = nx.shortest_path(DG)
print(sp)
