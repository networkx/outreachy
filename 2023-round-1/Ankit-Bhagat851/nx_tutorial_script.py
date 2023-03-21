<<<<<<< HEAD
#importing library
import networkx as nx
import matplotlib.pyplot as plt

#initiating a graph
DG = nx.DiGraph()

#adding nodes
DG.add_node(1)
DG.add_node('ankit')
DG.add_node('kumar')
DG.add_node((1,2))
DG.add_nodes_from([7,0])
DG.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

#adding edges
DG.add_edge(1, 'ankit')
DG.add_edge(4, 'ankit')
DG.add_edge('ankit','kumar')
DG.add_edges_from([(5, 7),(4,5)])
DG.add_edge(1, (1,2))
DG.add_edges_from([('ankit' ,0),('kumar',7)])
DG.add_edge((1,2), 0)

# Drawing the DiGraph
nx.draw(DG, with_labels=True)
plt.show()

# Calculating the shortest path and printing it
shortest_path = nx.shortest_path(DG)
print('shortest path: ', shortest_path)

#printing the nodes and edges
print('The nodes are: ',list(DG.nodes))
print('The edges are: ',list(DG.edges))

# Printing the number of nodes and edges
print("Number of Nodes:", DG.number_of_nodes())
print("Number of Edges:", DG.number_of_edges())

#removing node and edges
DG.remove_node('kumar')
DG.remove_edge('ankit',0)

# Drawing the DiGraph
nx.draw(DG, with_labels=True)
plt.show()

=======
#importing library
import networkx as nx
import matplotlib.pyplot as plt

#initiating a graph
DG = nx.DiGraph()

#adding nodes
DG.add_node(1)
DG.add_node('ankit')
DG.add_node('kumar')
DG.add_node((1,2))
DG.add_nodes_from([7,0])
DG.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

#adding edges
DG.add_edge(1, 'ankit')
DG.add_edge(4, 'ankit')
DG.add_edge('ankit','kumar')
DG.add_edges_from([(5, 7),(4,5)])
DG.add_edge(1, (1,2))
DG.add_edges_from([('ankit' ,0),('kumar',7)])
DG.add_edge((1,2), 0)

# Drawing the DiGraph
nx.draw(DG, with_labels=True)
plt.show()

# Calculating the shortest path and printing it
shortest_path = nx.shortest_path(DG)
print('shortest path: ', shortest_path)

#printing the nodes and edges
print('The nodes are: ',list(DG.nodes))
print('The edges are: ',list(DG.edges))

# Printing the number of nodes and edges
print("Number of Nodes:", DG.number_of_nodes())
print("Number of Edges:", DG.number_of_edges())

#removing node and edges
DG.remove_node('kumar')
DG.remove_edge('ankit',0)

# Drawing the DiGraph
nx.draw(DG, with_labels=True)
plt.show()

>>>>>>> fe043f558cf3ad1f9e9811eb24d5ece6794ce4d4
