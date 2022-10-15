import networkx as nx
import matplotlib as plt

G=nx.DiGraph() #calling on the digraph function
node_lists=['Qudirah','Outreachy','intern',5,(2,4)] #creating a list of nodes to add
G.add_nodes_from(node_lists)
edges_list=[('Qudirah','intern',{"length":1}) #creating a list of edges with attribute length
            ,('intern','Outreachy',{"length":0.5}),('Qudirah',(2,4),{"length":5}),('intern',5,{"length":0.452}),('5',(2,4),{"length":10})]
G.add_edges_from(edges_list)
path=dict(nx.all_pairs_dijkstra_path_length(G,weight='length'))
def print_distance(): 
    """function prints each of the nodes with shortest distance to every other node"""
    for i in node_lists:
        for m,n in path[i].items():
            print("Shortest distance between "+str(i)+' and '+str(m)+' is '+str(n))
def plot_network():
    """function to plot the network diagram"""
    nx.draw(G,with_labels=True)

print_distance()
plot_network()
