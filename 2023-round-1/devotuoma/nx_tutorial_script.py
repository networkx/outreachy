# importing networkx library
import networkx as nx
# printing the version once more
print(nx.__version__)
G = nx.DiGraph() # calling on the diagraph function using G as the global variable
# Graph is always a collection of nodes along with identified pairs of nodes i.e. edges, links, e.t.c
NetworkX, nodes can be any hashable object such as text string, an image, an XML object, another Graph, a customized node object, etc.
#incorporating nodes with attributes group and color based on types
G.add_node(1)
G.add_node(1, group='int',color='red')
G.add_node("Outreachy", group='int',color='green')
G.add_node((2,4), group='tuple',color='blue')
G.add_node(3, group='int',color='red')

#adding edges
G.add_edges_from([(1,3),("Outreachy",(2,4)),(3,"Outreachy"),((2,4),1)])

#getting the shortest_path
shortest_path = nx.shortest_path(G)

#printing the source and destination of each possible paths 
for s in shortest_path:
    print("shortest paths from", s, ":")
    for d in shortest_path[s]:
        print( "to", d,":", shortest_path[s][d])
# Getting the node attributes
colors = nx.get_node_attributes(G,'color').values()
# Analyzing the graphs
G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3)])

G.add_node("spam")       # adds node "spam"

list(nx.connected_components(G))
[{1, 2, 3}, {'spam'}]

sorted(d for n, d in G.degree())
[0, 1, 1, 2]

nx.clustering(G)
{1: 0, 2: 0, 3: 0, 'spam': 0}
# Drawing the graphs while using matplotlib labrary
G = nx.petersen_graph()

subax1 = plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
import matplotlib.pyplot as plt

# PLotting the graph using networkx.drwa 
nx.draw_networkx(G,with_labels=True,node_color=colors) 

