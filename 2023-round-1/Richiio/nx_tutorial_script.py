import networkx as nx
import matplotlib.pyplot as plt

print(nx.__version__)
DG = nx.DiGraph()


# 2a) adding nodes
DG.add_node(4)
DG.add_node(6)
DG.add_node("1")
DG.add_node("hello")
dg_tuple = ("p", "sarima", "outreachy", "3")
DG.add_nodes_from(dg_list)

# 2b) We could also have a similar implementation as shown below
DG.add_nodes_from([1,2,3]) # adds three nodes of type int
DG.add_nodes_from(['A','B', 'Z']) # add nodes of type string
DG.add_nodes_from([('C',4), ('D',5)]) # adds two nodes of type tuple

assert DG.number_of_nodes() <= 10 # check that number of nodes is not gretaer than 10

# 3a) adding edges
dg_edges = [(7, 8, {'weight':2}),
            ('4', "hello", {'weight':4}), 
            ("hello", "p", {'weight':6}), 
            ("p", "4", {'weight':8}), 
            ("4", "analysis", {'weight':10}), 
            ("analysis", "5", {'weight':12}),
            ('5',1, {'weight':11}),
            (2,'3', {'weight':9}), 
            ("3", 'hello', {'weight':7}),
            ('5', 'p', {'weight':5}),
            ("4", "analysis", {'weight':3}),
            ('3', '5', {'weight':13}), 
            ("hello", "analysis", {'weight':14})] 
            
DG.add_edges_from(dg_edges)

#3b) Similarly, we can implement task 3 as shown below:
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 1),
    ('B', 2),
    ('C', 2),
    (1, ('C',4)),
    (2, ('C',4)),
    (2, ('D',5)),
    (3, ('C',4)),
    (('C',4), 'Z'),
    (('D',5), 'Z')
])

# adding labels
labels = {1: "Quote", 2: "of", 
          '3':"the", 'msg':"day",
          'p':"peace", '4':"all",
          'around':"around", '5':"world"}


paths = nx.shortest_path(DG, weight='weight')
print(paths)

# Plot the graph
nx.draw(DG, pos=nx.spring_layout(DG), with_labels=True, font_size=10, node_color='green', node_size=1000)
plt.title(')
plt.show()