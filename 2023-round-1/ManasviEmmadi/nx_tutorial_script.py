import networkx as nx
import matplotlib.pyplot as plt
# import networkx.drawing as

DG = nx.DiGraph()

DG = nx.path_graph(8)

DG.add_nodes_from([
    (0, {"color": "red"}),
    (1, {"Time": 2}),
    (2, {"Items": ("Fries", "Pudding")}),
    (3, {"room_service": True}),
    (4, {"Type": "Suite"}),
    (5, {"Checkout": 12}),
    (6, {"laundry": False}),
    (7, {"instructions": ("clean regularly", "change sheets")})
])

edges = [
    (0, 1), (0, 3), (0, 5),
    (1, 2), (1, 4), (1, 7),
    (2, 5), (2, 6), (3, 4),
    (3, 2), (3, 6), (4, 7),
    (4, 1), (5, 0), (5, 3),
    (6, 0), (6, 7), (6, 3)
]
DG.add_edges_from(edges)

sp = dict(nx.all_pairs_shortest_path(DG))
for key in sp:
    print(sp[key])

subax1 = plt.subplot(121)

nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()
