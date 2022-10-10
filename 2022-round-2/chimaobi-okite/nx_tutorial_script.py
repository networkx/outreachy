# load the required libraries
import networkx as nx
import matplotlib.pyplot as plt

# 1) instanstiate a Directional Graph object
DG = nx.DiGraph()

# 2) Add nodes of multiple types to graph object, 
DG.add_nodes_from([1,2,3]) # adds three nodes of type int
DG.add_nodes_from(['A','B', 'Z']) # add nodes of type string
DG.add_nodes_from([('C',4), ('D',5)]) # adds two nodes of type tuple


assert DG.number_of_nodes() <= 10 # check that number of nodes is not gretaer than 10

# 3) Add multiple edges between the nodes above
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 1),
    ('B', 2),
    ('C', 2),
    (1, ('C',4)),
    (2, ('C',4)),
    (2, ('D',5)),
    (3, ('C',4)),
    (('C',4), 'Z'),
    (('D',5), 'Z')
])

# 4) Find the shortest path between all pairs of nodes in this graph and print them.
sp = dict(nx.all_pairs_shortest_path(DG))
for node, sub_nodes in sp.items():
  for sub_node, paths in sub_nodes.items():
    print(f'shortest path between {node} and {sub_node} is  --> {paths}')


# 5) Plot the graph
plt.figure(figsize=(4,4))
plt.title('Plt showing of Directinal Graph')
nx.draw(DG,with_labels=True, font_weight='bold')
plt.show() # show plot