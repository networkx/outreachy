import networkx as nx
import matplotlib.pyplot as plt

# networkx Digraph
G=nx.DiGraph()
# added an int node
G.add_node(8)
# added an str node
G.add_node('K')
# added a tuple
G.add_node(('k',2,7,'apple'))

# connected them with distinct edges
G.add_edge(8,'K')
G.add_edge('k','K')
G.add_edge(8,2)
G.add_edge(2,7)
G.add_edge(2,'apple')
G.add_edge('K','apple')


nx.draw(G,with_labels=True)
shortestpath=nx.shortest_path(G)
print(shortestpath)
