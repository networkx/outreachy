# Import the libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create the DiGraph object
DG = nx.DiGraph()

# Add nodes/edges of type int
DG.add_node(1) # add an initial node 1
DG.add_edge(1, 2) # add an edge from 1 to 2

# Add nodes of type str
DG.add_node("alice") # add node "alice" 
DG.add_node("bob") # add node "bob"

# Add nodes/edges of type tuple
DG.add_edge("bob", (3, 4)) # link "bob" to new nodes 3, 4
DG.add_edge(1, ("alice", "bob")) # add an edge from 1 to "alice" and "bob"
DG.add_edge(1, (4, 5)) # link node 1 to 3, 4
DG.add_edges_from([(5, 6), (6, 7)]) # add edges from 5, 6 to 7

# Print the number of nodes and edges
print("The number of nodes in DG:", DG.number_of_nodes())
print("The number of edges in DG:", DG.number_of_edges())

# Draw the DiGraph
nx.draw(DG, with_labels=True)

# Calculate and print out the shortest path in DG
sp = nx.shortest_path(DG)
print("The shortest path in DG: ", sp)