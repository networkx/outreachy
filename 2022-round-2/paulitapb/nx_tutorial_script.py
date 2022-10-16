""" Tutorial script @paulitapb """

#Imports 
import networkx as nx 
import matplotlib.pyplot as plt

G = nx.DiGraph()

#Add nodes with a different color for each data-type
G.add_node(1, color="c")
G.add_node(2, color="c")
G.add_node(3.4, color="blue")
G.add_node("o", color="green")
G.add_node("utreachy", color="pink")
G.add_node((1, 2), color= "yellow")

G.add_edges_from([(1, 2), (2, 3.4), ("o", "utreachy"), ((1,2), 1), ((1,2), 2)])

#Draw the graph

colors = nx.get_node_attributes(G,'color').values() #get the colors of the nodes 

nx.draw(G, with_labels=True, font_weight='bold', node_color=colors)
plt.show()

#Print shortest_path between all pairs of nodes
all_shortest_path = nx.shortest_path(G)

#Pretty print all shortest path
for source in all_shortest_path:
    print("shortest paths from", source, ":")
    for dest in all_shortest_path[source]:
        print( "to", dest,":", all_shortest_path[source][dest])
