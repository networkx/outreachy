import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()
t = ('Hyd', 3)
DG.add_nodes_from([1, 2, 'Delhi', t, 4])
DG.add_edges_from([(1, 'Delhi'), ('Delhi', 1), (1, t), (4, t), (2, 4), (1, 2)])

options = {
    'width': 3,
    'node_size': 1500
}

sp = dict(nx.all_pairs_shortest_path(DG))

for key in sp:
    for val in sp[key]:
        l = len(sp[key][val])-1
        if key != val:
            print("Shortest Distance between {} and {} is {}".format(key, val, l))

nx.draw_networkx(DG, **options)
plt.draw()
plt.show()
