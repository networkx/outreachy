import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()

# Different types of nodes
nodes = [44, "Reception","Laundry","Room service",(6, 3), 911]

# Adding nodes from nodes
DG.add_nodes_from(nodes)
DG.number_of_nodes()
# Different edges
edges = [(44, "Reception"), (44, "Room service"), ((6, 3), 911),
         ("Room service", "Laundry"), ("Laundry", (6, 3)),
         ("Reception", 911), (44, 911), (911, "Room service")]

# Adding edges from edges
DG.add_edges_from(edges)

# Finding shortest path for each node
sp = dict(nx.all_pairs_shortest_path(DG))
for key in sp:
    print(sp[key])

# Plotting directed graph
subax1 = plt.subplot(121)
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()
