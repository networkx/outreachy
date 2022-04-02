# Importing the libraries
import networkx as nx
import matplotlib.pyplot as plt

# Creating DiGraph object
OG = nx.DiGraph()

# Adding nodes of type int
OG.add_node(1) 
OG.add_nodes_from([2,3]) #adds node through iterating from given list

# Adding nodes of type str
OG.add_node("Smith")
OG.add_node("Sam") 
OG.add_node("Roy") 
OG.add_node("Jil") 

# Adding edges to nodes
OG.add_edge("Roy",1) # Roy-->1
OG.add_edges_from([("Smith","Sam"),("Smith","Roy"),("Smith","Jil")]) # Smith-->Sam | Smith-->Roy | Smith-->Jil
OG.add_edges_from([("Sam",2),("Sam",3)]) # Sam-->2 | Sam-->3
OG.add_edge("Jil",(4,5,6)) # Jil-->(4,5,6)

# Drawing the DiGraph
nx.draw(OG, with_labels=True)

# Calculating the shortest path and printing it
shortest_path = nx.shortest_path(OG)
print(shortest_path)

# Printing the number of nodes and edges
print("Number of Nodes:", OG.number_of_nodes())
print("Number of Edges:", OG.number_of_edges())