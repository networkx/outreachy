# import the library
from email.charset import SHORTEST
import networkx as nx
import matplotlib.pyplot as plt

#creating null graph structure
G = nx.DiGraph()

# adding a int type node
G.add_node(2)
G.add_node(3)

# adding a string type node
G.add_node("boy")
G.add_node("girl")

# adding a list type node
G.add_nodes_from([20,25])

#adding a tuple type node
G.add_nodes_from([(5,{4:"father"}),(6,{7:"mother"})])

#growing G by adding edges
G.add_edge(2,3)
G.add_edge(3,2)
G.add_edge("girl",2)
G.add_edge(3,"boy")
G.add_edges_from("girl")
G.add_edges_from(2,[20,25])
G.add_edges_from([[20,25],(5,{4:"father"})])
G.add_edges_from([(6,{7:"mother"}),3])

#print number of nodes
print(G.number_of_nodes())

#print number of edges
print(G.number_of_edges())


# finding the shortest path between all pairs of nodes 
shortest_path_g=nx.shortest_path(G)
print(shortest_path_g)

#drawing the Graph
nx.draw(G, with_labels = True)
#showing the graph
plt.show()








