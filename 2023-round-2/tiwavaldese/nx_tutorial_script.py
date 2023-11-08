import networkx as nx
import matplotlib.pyplot as plt

#Create a DiGraph graph object
G = nx.DiGraph()

#Add multiple nodes of different types
G.add_node(1)
G.add_nodes_from([2,3])
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_nodes_from("spam")

#Add multiple edges between nodes
G.add_edge(1,'s')
G.add_edge('s',(2,3))
G.add_edge(4,'p')
G.add_edge(5,'s')
G.add_edge('p','a')
G.add_edge('a',6)
G.add_edge(1,'m')

# Find the shortest path and print
st_p = nx.shortest_path(G)
print(st_p)

# Plot the Graph
nx.draw(G, with_labels = True, connectionstyle='arc3, rad = 0.1')
