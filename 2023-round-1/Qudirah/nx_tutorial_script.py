#imports
import networkx as nx

G = nx.DiGraph() #calling on the digraph function

#adding nodes with attributes group and color based on types
G.add_node(1, group='int',color='red')
G.add_node("Outreachy", group='int',color='green')
G.add_node((2,4), group='tuple',color='blue')
G.add_node(3, group='int',color='red')

#adding_edges
G.add_edges_from([(1,3),("Outreachy",(2,4)),(3,"Outreachy"),((2,4),1)])

#getting the shortest_path
shortest_path = nx.shortest_path(G)

#printing the source and destination of each possible paths
for s in shortest_path:
    print("shortest paths from", s, ":")
    for d in shortest_path[s]:
        print( "to", d,":", shortest_path[s][d])

colors = nx.get_node_attributes(G,'color').values() #getting the color attributes of each node

nx.draw_networkx(G,with_labels=True,node_color=colors) #drawing the graph