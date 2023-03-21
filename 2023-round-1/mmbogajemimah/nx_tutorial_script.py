""" Tutorial script @mmbogajemimah """

#Importing Libraries
'''
import the NetworkX library and the pyplot module from the matplotlib library to plot the graph
'''
import networkx as nx
import matplotlib.pyplot as plt

#Create a directed graph
'''
We create a directed graph using the DiGraph() method of NetworkX and assign it to the variable graph
'''
graph = nx.DiGraph()

#Add nodes of different types to the graph
'''
We add nodes of different types to the graph using the add_node() method of NetworkX.
'''
graph.add_node(3, color='yellow') #integer
graph.add_node(4, color='yellow') #integer
graph.add_node(5.89, color='gray') #float
graph.add_node("J", color="blue") #string
graph.add_node("emimah", color='green') #string
graph.add_node((5,6), color='red') #tuple

# Add multiple edges between nodes
graph.add_edges_from([(3, 4), (4, 5.89), ("J", "emimah"), ((5,6), 4), ((5, 6), 3)])

#Plot the graph
'''
We plot the graph using the draw() method of NetworkX and the show() method of pyplot. 
The with_labels parameter is set to True to show the node labels in the plot.
'''
    #Get the node colors
graph_colors = nx.get_node_attributes(graph, 'color').values()


nx.draw(graph, with_labels=True, font_weight='bold', node_color=graph_colors)
plt.show()
#Find the shortest path between all pairs of nodes
'''
find the shortest path between all pairs of nodes using the all_pairs_shortest_path() 
method of NetworkX and assign it to the variable shortest_paths. This method returns a 
dictionary of dictionaries, where the outer dictionary keys are the source nodes and the 
inner dictionary keys are the target nodes, and the values are lists of nodes representing 
the shortest path from the source to the target.
'''
shortest_paths = dict(nx.all_pairs_shortest_path(graph))

# Print the shortest paths between all pairs of nodes
'''
print the shortest paths between all pairs of nodes using nested loops to iterate over the 
keys of the shortest_paths dictionary.
'''
for source in shortest_paths:
    for target in shortest_paths[source]:
        print(f"Shortest path from {source} to {target}: {shortest_paths[source][target]}")
