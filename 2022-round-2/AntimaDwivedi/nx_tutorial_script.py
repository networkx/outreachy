#importing the libraries

import networkx as nx
import matplotlib.pyplot as plt

#creating a Directed Graph 
DG = nx.DiGraph()

#Adding nodes in the Graph
DG.add_node(8)
DG.add_node("great")
DG.add_nodes_from("good")
DG.add_nodes_from([2, 3])
DG.add_node((7, 8))

#Adding edges between the nodes
DG.add_edge(8, 'g')
DG.add_edge('g', 'o')
DG.add_edge('d', (7, 8))
DG.add_edge('o', 'd')
DG.add_edge((7, 8), 3)
DG.add_edge(3, 2)
DG.add_edge(2,'great')
DG.add_edge('great',8)
DG.add_edge('d','great')

#Finding the shortest path between all pairs of nodes in this graph
shortest_path = dict(nx.all_pairs_shortest_path(DG))
for each_node in shortest_path:
    print(shortest_path[each_node])

#Output of the print statement
{8: [8], 'g': [8, 'g'], 'o': [8, 'g', 'o'], 'd': [8, 'g', 'o', 'd'], (7, 8): [8, 'g', 'o', 'd', (7, 8)], 'great': [8, 'g', 'o', 'd', 'great'], 3: [8, 'g', 'o', 'd', (7, 8), 3], 2: [8, 'g', 'o', 'd', (7, 8), 3, 2]}
{'great': ['great'], 8: ['great', 8], 'g': ['great', 8, 'g'], 'o': ['great', 8, 'g', 'o'], 'd': ['great', 8, 'g', 'o', 'd'], (7, 8): ['great', 8, 'g', 'o', 'd', (7, 8)], 3: ['great', 8, 'g', 'o', 'd', (7, 8), 3], 2: ['great', 8, 'g', 'o', 'd', (7, 8), 3, 2]}
{'g': ['g'], 'o': ['g', 'o'], 'd': ['g', 'o', 'd'], (7, 8): ['g', 'o', 'd', (7, 8)], 'great': ['g', 'o', 'd', 'great'], 3: ['g', 'o', 'd', (7, 8), 3], 8: ['g', 'o', 'd', 'great', 8], 2: ['g', 'o', 'd', (7, 8), 3, 2]}
{'o': ['o'], 'd': ['o', 'd'], (7, 8): ['o', 'd', (7, 8)], 'great': ['o', 'd', 'great'], 3: ['o', 'd', (7, 8), 3], 8: ['o', 'd', 'great', 8], 2: ['o', 'd', (7, 8), 3, 2], 'g': ['o', 'd', 'great', 8, 'g']}
{'d': ['d'], (7, 8): ['d', (7, 8)], 'great': ['d', 'great'], 3: ['d', (7, 8), 3], 8: ['d', 'great', 8], 2: ['d', (7, 8), 3, 2], 'g': ['d', 'great', 8, 'g'], 'o': ['d', 'great', 8, 'g', 'o']}
{2: [2], 'great': [2, 'great'], 8: [2, 'great', 8], 'g': [2, 'great', 8, 'g'], 'o': [2, 'great', 8, 'g', 'o'], 'd': [2, 'great', 8, 'g', 'o', 'd'], (7, 8): [2, 'great', 8, 'g', 'o', 'd', (7, 8)], 3: [2, 'great', 8, 'g', 'o', 'd', (7, 8), 3]}
{3: [3], 2: [3, 2], 'great': [3, 2, 'great'], 8: [3, 2, 'great', 8], 'g': [3, 2, 'great', 8, 'g'], 'o': [3, 2, 'great', 8, 'g', 'o'], 'd': [3, 2, 'great', 8, 'g', 'o', 'd'], (7, 8): [3, 2, 'great', 8, 'g', 'o', 'd', (7, 8)]}
{(7, 8): [(7, 8)], 3: [(7, 8), 3], 2: [(7, 8), 3, 2], 'great': [(7, 8), 3, 2, 'great'], 8: [(7, 8), 3, 2, 'great', 8], 'g': [(7, 8), 3, 2, 'great', 8, 'g'], 'o': [(7, 8), 3, 2, 'great', 8, 'g', 'o'], 'd': [(7, 8), 3, 2, 'great', 8, 'g', 'o', 'd']}


#Visualization of the graph
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()

![Screenshot (5)](https://user-images.githubusercontent.com/56269029/196000053-22d68177-ce95-4f0f-bf2b-336da21b5032.png)





