# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:05:26 2022

@author: lenovo
"""
# import networkx and matplotlib library
import networkx as nx
import matplotlib.pyplot as plt
# creating DiGraph object DG
DG = nx.DiGraph()
# creating nodes 1,2,3,4 and connecting nodes 1->2 and 3->4
DG.add_edges_from([(1,2),(3,4)]) 
# connecting node 1 and 4: 4->1
DG.add_edge(4,1)
# creating nodes 'tom' and 'jerry' and connecting 'tom'->'jerry'
DG.add_edge('tom', 'jerry')
# creating nodes 'dog' and 'cat' and connecting 'dog'->'cat'
DG.add_edge('dog','cat')
# connecting node 1 with 'cat'
DG.add_edge(1,'cat')
# creating tuples as nodes 
DG.add_edge((100,121),(216,343))
# connecting str node to tuple node
DG.add_edge('jerry',(216,343))
# connecting 'cat'-> 3
DG.add_edge('cat',3)
# adding weighted graph
DG.add_weighted_edges_from([(1,'tom', 0.5), ('dog',(216,343), 0.75)])
# Drawing the DiGraph
nx.draw(DG, with_labels=True)
plt.draw()

# Calculating the shortest path and printing it
sp = nx.shortest_path(DG)
print("Shortest path: ",sp)