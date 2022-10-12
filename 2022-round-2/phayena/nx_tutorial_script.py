# import the library
import networkx as nx
import matplotlib.pyplot as plt

#creating null graph structure
G = nx.DiGraph()

# adding a int type node
G.add_node(2)
G.add_node(3)


# adding a string type node
G.add_node("boy")


# adding a list type node
G.add_nodes_from([20,25])

#adding a tuple type node
G.add_nodes_from([(5,{4:"father"})])

#growing G by adding edges
G.add_edge(2,3)
G.add_edge(3,2)
G.add_edge(3,"boy")
G.add_edges_from("boy")
G.add_edges_from(2,[20,25])
G.add_edges_from(3,[20,25],"boy")
G.add_edges_from([20,25],(5,{4:"father"}))
G.add_edges_from((5,{4:"father"}),2)

#print number of nodes
print(G.number_of_nodes())

#print number of edges
print(G.number_of_edges())


# finding the shortest path between all pairs of nodes 
shortest_path_g=nx.shortest_path(G)
print(shortest_path_g)

#drawing the Graph
nx.draw(G, with_labels = True,font_weight='bold')
plt.title("Direction of graph")
#showing the graph
plt.show()








