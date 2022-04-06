#import libraries
import networkx as nx

#Digraph object
DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (1, 3)]) # node 1,2,3 and connected them from 1->2->3
DG.add_edge("Hello", "World!")  # node and connecting them "Hello" -> "World!"
DG.add_edge("World!", (5, 6))  # node (5,6) and connecting them "World!" -> (5,6)
DG.add_edge(1, (5, 6))  # edge 1 -> (5,6)
DG.add_edge(1, "World!")  # edge 1 -> "World!"

# DiGraph
nx.draw(DG, with_labels=True)

# Calculate the shortest path and print it
sp = nx.shortest_path(DG)
print(sp)
