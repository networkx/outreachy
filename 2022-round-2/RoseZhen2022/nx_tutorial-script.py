import networkx as nx
import matplotlib.pyplot as plt
import random


# Create a NetworkX directed graph object
DG = nx.DiGraph()

# Create a list contain multiple type of nodes and add this nodes to the graph
nodes_list = [1, 2, 'moon', 'star', (3, 'cs'), (4, 'ml')]
DG.add_nodes_from(nodes_list)

# Create a edges list and add to graph
edges_list = [(1, 2), (1, "star"), (1, (3, "cs")), 
            (2, "moon"), (2, 'star'), (2, (4, 'ml')),
            ('moon', (4, 'ml')), ('star', 2),
            ((3, "cs"), 'star'), ((4, 'ml'), 1)
            ]
DG.add_edges_from(edges_list)


# Find the shortest path between all pairs of nodes in this graph and print them.
sp = dict(nx.all_pairs_shortest_path(DG))
for n, v in sp.items():
    for v, p in v.items():
        print(f'shortest path between {n} and {v} is {p}')


# Plot the graph
nx.draw(DG, pos=nx.spring_layout(DG), with_labels=True, font_size=10, node_color='green', node_size=1000)
plt.show()




