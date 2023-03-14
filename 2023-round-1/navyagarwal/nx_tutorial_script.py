# imports
import networkx as nx
import matplotlib.pyplot as plt

# DiGraph -> Direted graph that can contain self-loops but not parallel edges
G = nx.DiGraph()

# various methods to add nodes of different data types
G.add_node(1)                      # integer
G.add_node('navya')                # string
G.add_node((3, 4))                 # tuple
G.add_nodes_from(['a', 'b'])       # from list
G.add_nodes_from(range(9, 11))     # in range

X = nx.path_graph(2)
Y = nx.complete_graph(3)

G.add_nodes_from(X)                # from graph X
G.add_node(Y)                      # graph Y



# can add individual or multiple edges to graph
G.add_edge(1, 'navya')
G.add_edges_from([
    ('a', 'b'),
    ('navya', 1),
    (X, Y),
    (9, X),
    (Y, 'navya'),
    ('b', 10),
    (10, Y),
    ('navya', 9),
    ((3, 4), 0),
    ('a', 9),
    (0, 'b'),
    (9, 10)])
G.add_edges_from(X.edges)
G.add_edges_from(Y.edges)


nx.draw(G, with_labels = True, node_color = 'yellow')


# printing shortest path between all pairs of nodes if it exists
for source in G:
    for dest in G:
        if(nx.has_path(G, source, dest)):
            print(source, " -> ", dest," : ", nx.shortest_path(G, source, dest))