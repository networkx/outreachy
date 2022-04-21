"""
========================
Importing libraries
========================
"""
import networkx as nx
import matplotlib.pyplot as plt

"""
====================================================
Creating a DiGraph Object and adding nodes and edges
====================================================
"""
G = nx.DiGraph()
G.add_nodes_from([1, 2, (3,4), "root", 1.5, (7,8,9), 99, 34, "fire", "naruto"])
G.add_edges_from([(1,2), ("root", "fire"), (1.5, (3,4)), (34,"naruto"), ("fire", 99),
                 ("naruto", 99), (2,34),(2,"naruto"),((7,8,9),(3,4)),(1.5, 34)])

"""
=============================================================
Printing shortest path taken between any node and other nodes
=============================================================
"""
print(nx.shortest_path(G))

"""
========================
Plotting
========================
"""
pos = nx.shell_layout(G)
nx.draw(G,  pos = pos , with_labels = True, node_color = 'maroon' , font_color ='white',
       node_size = 2000, font_size = 14)