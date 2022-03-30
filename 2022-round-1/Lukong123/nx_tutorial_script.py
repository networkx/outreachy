#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt

# Create a NetworkX DiGraph graph object
DG = nx.DiGraph()

# Adding nodes of multiple type 

# Adding nodes of type int (integer)
DG.add_nodes_from([1, 2, 3,])

# Adding nodes of type str (string)

DG.add_nodes_from(['smile', 'code', 'Consistency'])

# Adding nodes of type typle
DG.add_nodes_from([(5,6), (7, 8), (9, 10)])

# Adding multiple edges between nodes

DG.add_edges_from([(1, 'smile'), (2, 3), (3, (5, 6)), 
('code', (7,8)), ('consistency', (9, 10)),
('smile', 3),((7,8), 3), ('consitency', 'smile'), (1, (5,6)),
((9, 10), 1)])

# Calculating shortest path between all pairs of node

path = dict(nx.all_pairs_shortest_path(DG))
print(path) 

# plotting graph using networkx.draw

nx.draw(DG)
