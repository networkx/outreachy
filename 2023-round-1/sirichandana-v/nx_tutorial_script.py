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

sp_dict = dict(nx.all_pairs_shortest_path(DG))

for src in DG.nodes():
    for desti in DG.nodes():
        if src != desti:
            print("Shortest path between {} and {}:".format(src, desti), end=" ")

            if desti in sp_dict[src]:
                path = sp_dict[src][desti]
                first = True
                for ele in path:
                    if first:
                        print("{}".format(ele), end=" ")
                        first = False
                    else:
                        print("-->{}".format(ele), end=" ")
            else:
                print("Doesn't exist")
            print("\n")


nx.draw_networkx(DG, **options)
plt.draw()
plt.show()
