# Importing the libraries
import networkx as nx


# Creating DiGraph object
G = nx.DiGraph()

# Adding nodes of type int
G.add_node(24)
G.add_node(38)

# Adding nodes of type str
G.add_node("Amy")
G.add_node("Jake")
G.add_node("Rosa")
G.add_node("Gina")

# Adding edges to nodes
G.add_edges_from([("Gina","Rosa"),("Gina","Amy"),("Gina","Jake"),("Jake","Amy")]) # Gina-->Rosa | Gina-->Amy | Gina-->Jake | Jake-->Amy
G.add_edges_from([("Gina",24),("Jake",38)]) # Gina-->24 | Jake-->38
G.add_edge("Rosa",38) # Rosa-->38
G.add_edge(24,(16,17)) # 24-->(16,17)
G.add_edge("Rosa",(16,17)) # Rosa-->(16,17)

# Drawing the DiGraph
nx.draw(G, with_labels=True)

# Printing the number of nodes and edges
print("Number of Nodes:", G.number_of_nodes())
print("Number of Edges:", G.number_of_edges())

# Calculating the shortest path and printing it
shortest_path = nx.shortest_path(G)
print(shortest_path)