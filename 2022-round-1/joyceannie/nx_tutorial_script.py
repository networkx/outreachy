#import libraries
import networkx as nx
import matplotlib.pyplot as plt

#create a networkx digraph object
DG = nx.DiGraph()

#adding nodes and edges
DG.add_edge(1, 2)
DG.add_edge('foo', 'bar')
DG.add_edge(1, ('a', 'b'))
DG.add_edge(3, 4)
DG.add_edge(('a', 'b'), 3)
DG.add_edge(('foo', 'bar'), ('a', 'b'))

# find the shortest path between all pairs of nodes
sp = nx.shortest_path(DG)

#plot the graph
nx.draw(DG, with_labels=True, font_weight='bold')


