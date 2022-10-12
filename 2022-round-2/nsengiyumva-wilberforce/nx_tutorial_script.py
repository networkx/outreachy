import networkx as nx
import matplotlib.pyplot as plt

#create a DiGraph object
DG = nx.DiGraph()
#list of edges between corresponding nodes
edges_between_nodes = [
        (1,2),
        (2, "wilber"),("wilber", "seth"),
        ("seth", (2,'m')), 
        ((2, 'm'), 1), 
        (2,"seth"), 
        ((2, 'm'), 2), 
        ("wilber",1)
]
#add edges to DG        ]
DG.add_edges_from(edges_between_nodes)
#show the list of shortest path
print(dict(nx.all_pairs_shortest_path(DG)))
#Draw the DiGraph
nx.draw(DG, nx.circular_layout(DG),edge_color="green", node_color="yellow",with_labels=True, width=3, font_weight='bold')
#display the DiGraph
plt.show()