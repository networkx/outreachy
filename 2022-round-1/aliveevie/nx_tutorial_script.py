import networkx as nx
TG = nx.DiGraph()
TG.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
    (6, {"color": "blue"}),
    (7, {"internship":"outreachy"}),
])
TG.add_edges_from([(4, 5), (6, 7)])
sp = dict(nx.all_pairs_shortest_path(TG))
nx.draw(TG)
sp