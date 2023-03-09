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
pairs=dict(nx.shortest_path(DG))


for node in pairs:
    # print("from node ",node,"->")
    for node1 in pairs[node]:
        print("from node ",node,"->",node1," shortest path is:",pairs[node][node1])

"""
    output of above for loop
from node  5 -> 5  shortest path is: [5]
from node  5 -> a  shortest path is: [5, 'a']
from node  5 -> (1, 2)  shortest path is: [5, (1, 2)]
from node  5 -> b  shortest path is: [5, 'a', 'b']
from node  a -> a  shortest path is: ['a']
from node  a -> b  shortest path is: ['a', 'b']
from node  one -> one  shortest path is: ['one']
from node  one -> (7, 8)  shortest path is: ['one', (7, 8)]
from node  1 -> 1  shortest path is: [1]
from node  2 -> 2  shortest path is: [2]
from node  7 -> 7  shortest path is: [7]
from node  7 -> 8  shortest path is: [7, 8]
from node  7 -> one  shortest path is: [7, 8, 'one']
from node  7 -> (7, 8)  shortest path is: [7, 8, 'one', (7, 8)]
from node  8 -> 8  shortest path is: [8]
from node  8 -> one  shortest path is: [8, 'one']
from node  8 -> (7, 8)  shortest path is: [8, 'one', (7, 8)]
from node  b -> b  shortest path is: ['b']
from node  (1, 2) -> (1, 2)  shortest path is: [(1, 2)]
from node  c -> c  shortest path is: ['c']
from node  c -> d  shortest path is: ['c', 'd']
from node  c -> one  shortest path is: ['c', 'one']
from node  c -> (7, 8)  shortest path is: ['c', 'one', (7, 8)]
from node  d -> d  shortest path is: ['d']
from node  d -> one  shortest path is: ['d', 'one']
from node  d -> (7, 8)  shortest path is: ['d', 'one', (7, 8)]
from node  (7, 8) -> (7, 8)  shortest path is: [(7, 8)]
"""

#visual plot of above graph
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()


