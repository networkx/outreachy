"""
This script demostrates my familiarity with the networkx tutorial. 
It was created after I went through the networkx introductory tutorial.
    
"""
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a DiGraph 
DG = nx.DiGraph()

# Step 2: Add nodes of multiple types to this graph object, 
# at least one node of each type int, str, tuple. (Maximum 10 nodes)
DG.add_node(1) # node added using int
DG.add_node(2) # node added using int
DG.add_node('Cute') # node added using string
DG.add_node((12, 9)) # node added using tuple
DG.add_nodes_from(['James', 'Samantha', 'Gale']) # add a list of nodes
#print(DG.nodes())

# Step 3: Add multiple edges between the nodes
DG.add_edge(1, 2)
DG.add_edge(1, 'Cute')
DG.add_edge('James', 3)
DG.add_edges_from([('James', 1), ('Samantha', 2), ('Cute', 'Gale')])
DG.add_edge('Cute', (12, 9), weight=0.8) # add an edge with a weight property.

# Step 4: Find the shortest path between all pairs of nodes
# in this graph and print them.
shortest_paths = dict(nx.all_pairs_shortest_path(DG))
print('\nThe shortest paths between nodes:\n')
for node, data in shortest_paths.items():
    for second_node, path in data.items():
        print(f'{node} to {second_node}: {path}')


# Step 5: Plot the graph using networkx.draw
plt.subplot()
plt.title('Plot of a Graph')
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()

