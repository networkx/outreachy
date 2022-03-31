import networkx as nx
import matplotlib.pyplot as plt

#Creating a networkX digraph
G=nx.DiGraph()
#Adding nodes of int, str and tuple type
G.add_node(1)
G.add_node("string1")
G.add_node((6,2))
G.add_node('string2')
G.add_nodes_from([2,3,5])
G.add_nodes_from([(4,{'color':'red'})])
#Adding edges between the nodes
G.add_edge(4,1)
G.add_edges_from([(1,2),(1,3),(1,'string1'),(2,3),('string2',1),(1,'string2'),(1,(6,2)),(2,5),((6,2),'string2'),('string2',4)])
#Calculating shortest path between all nodes in the graph
p=nx.shortest_path(G)
print('Printing shortest path')
#Storing existing nodes in the graph
G_node_list = G.nodes
for index,node in enumerate(G_node_list):
    print('From',node)
    for index2,node2 in enumerate(G_node_list):
        if index!=index2 and nx.has_path(G, node, node2):
            print('To', node2, ':', p[node][node2])
#Plotting the graph
nx.draw(G,pos=nx.circular_layout(G),with_labels=True)
plt.show()

