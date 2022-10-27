import networkx as nx


DG = nx.DiGraph()


# adding nodes
DG.add_node(1)
DG.add_node(2)
DG.add_node("3")
DG.add_node("msg")
dg_tuple = ("p", "4", "around", "5")
DG.add_nodes_from(dg_tuple)


# adding edges
dg_edges = [(1, 2, {'weight':2}),
            ('4', "msg", {'weight':4}), 
            ("msg", "p", {'weight':6}), 
            ("p", "4", {'weight':8}), 
            ("4", "around", {'weight':10}), 
            ("around", "5", {'weight':12}),
            ('5',1, {'weight':11}),
            (2,'3', {'weight':9}), 
            ("3", 'msg', {'weight':7}),
            ('5', 'p', {'weight':5}),
            ("4", "around", {'weight':3}),
            ('3', '5', {'weight':13}), 
            ("msg", "around", {'weight':14})] 
            
DG.add_edges_from(dg_edges)

# adding labels
labels = {1: "Quote", 2: "of", 
          '3':"the", 'msg':"day",
          'p':"peace", '4':"all",
          'around':"around", '5':"world"}


paths = nx.shortest_path(DG, weight='weight')
print(paths)

nx.draw(DG, with_labels = True)

