#import libraries
import networkx as nx
import matplotlib.pyplot as plt

#create a networkx digraph object
DG = nx.DiGraph()

#adding nodes and edges
#adding nodes and edges
DG.add_edge(1, 2)
DG.add_edge(2, ('foo', 'bar'))
DG.add_edge(4, 'a')
DG.add_edge('a', 3)
DG.add_edge(('foo', 'bar'), 3)
DG.add_edge(4, 2)
DG.add_edge(4, 1)
DG.add_edge(3, 4)

# find the shortest path between all pairs of nodes
shortest_path = nx.shortest_path(DG)
#printing shortest paths
for source_node in shortest_path.keys():
    for dest_node in shortest_path[source_node]:
        print(f'Shortest path from node {source_node} to node {dest_node}: {shortest_path[source_node][dest_node]}')

#plot the graph
nx.draw(DG, with_labels=True, font_weight='bold')


