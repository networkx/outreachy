import networkx as nx
import matplotlib.pyplot as plt

#creating a Directed Graph using a function in networkx
DG=nx.DiGraph()

#Adding nodes in graph with the help of add_node and add_nodes_from functions
DG.add_node(5)
DG.add_node('a')
DG.add_node("one")
DG.add_nodes_from((1,2))
DG.add_nodes_from([7,8])

#creating edges between the nodes
DG.add_edge(5,'a')
DG.add_edge('a','b')
DG.add_edge(5,(1,2))
DG.add_edge('c','d')
DG.add_edge('c',"one")
DG.add_edge(8,"one")
DG.add_edge(7,8)
DG.add_edge('d',"one")
DG.add_edge("one",(7,8))

#Finding the shortest path and storing the output in dictionary
pairs= dict(nx.all_pairs_shortest_path(DG))


for node in pairs:
    print(pairs[node])

"""
    output of above for loop
{5: [5], 'a': [5, 'a'], (1, 2): [5, (1, 2)], 'b': [5, 'a', 'b']}
{'a': ['a'], 'b': ['a', 'b']}
{'one': ['one'], (7, 8): ['one', (7, 8)]}
{1: [1]}
{2: [2]}
{7: [7], 8: [7, 8], 'one': [7, 8, 'one'], (7, 8): [7, 8, 'one', (7, 8)]}
{8: [8], 'one': [8, 'one'], (7, 8): [8, 'one', (7, 8)]}
{'b': ['b']}
{(1, 2): [(1, 2)]}
{'c': ['c'], 'd': ['c', 'd'], 'one': ['c', 'one'], (7, 8): ['c', 'one', (7, 8)]}
{'d': ['d'], 'one': ['d', 'one'], (7, 8): ['d', 'one', (7, 8)]}
{(7, 8): [(7, 8)]}
"""

#visual plot of above graph
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()


