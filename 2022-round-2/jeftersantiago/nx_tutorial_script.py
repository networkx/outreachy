import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Adds nodes of type int
G.add_node(1)
G.add_node(2)

# Adds nodes of type str
G.add_node('São Paulo')
G.add_node('New York')

# Add nodes of tuples
G.add_nodes_from([(3, 'Beijing'), (4, 'Moscow')])

# Add edges between nodes

G.add_edge(1, 2)
G.add_edge(2, 1)
G.add_edge('São Paulo', 2)
G.add_edge(2, (3, 'Beijing'))
G.add_edge((3, 'Beijing'), 'New York')
G.add_edge((4, 'Moscow'), 'São Paulo')
G.add_edge((4, 'Moscow'), 'New York')

# Calculates the shortest distances between all pairs
path = dict(nx.all_pairs_shortest_path_length(G))


print("Shortest distances between nodes")
for node in G.nodes:
    for i in path[node].items():
        print("Node", str(node), "to node", str(i[0]))
        print("Shortest distance = ", str(i[1]))
nx.draw(G, with_labels = True)
plt.show()
