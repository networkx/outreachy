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
G.add_edge(1,(2,3))
G.add_edge((2,3),1)
G.add_edge(1,3)
G.add_edge(3,1)
G.add_edge((2,3),5)
G.add_edge(5,(2,3))
G.add_edge((2,3),6)
G.add_edge(6,(2,3))
G.add_edge(4,5)
G.add_edge(5,4)
G.add_edge(4,'s')
G.add_edge('s',4)
G.add_edge(5,'p')
G.add_edge('p',5)
G.add_edge('a',6)
G.add_edge(6,'a')
G.add_edge(2,'m')
G.add_edge('m',2)

# Find the shortest path and print
st_p = nx.shortest_path(G)
print(st_p)

# Plot the Graph
nx.draw(G, with_labels = True, node_color= 'red')
plt.show()