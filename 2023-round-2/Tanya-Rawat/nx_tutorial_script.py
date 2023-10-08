import networkx as nx
import matplotlib.pyplot as plt
di_graph = nx.DiGraph()

# add an int node 
di_graph.add_node(3) 

#adding a String node
di_graph.add_node('T') 

#adding a tuple node
di_graph.add_node(("a", 20, 40, "f"))

#adding edges between the node
di_graph.add_edges_from([
            (3,'T'),
            ('T', 'a'),
            ('a', 20),
            (40,'f'),
            ('f', 'a'),
            (3, 20)
])

nx.draw(di_graph, with_labels=True)
sp = nx.shortest_path(di_graph)
print(sp)
