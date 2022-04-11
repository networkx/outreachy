'''
-----------------------------------
        NX_TUTORIAL_SCRIPT
-----------------------------------
'''

import networkx as nx


'''
Declaration of Directed Graph
'''
G=nx.DiGraph()

# Adding edges will automatically declare the nodes

G.add_edge(5,6)
G.add_edge(1,(10,11))
G.add_edge("spam",5)
G.add_edge((10,11),1)
G.add_edge("test",6)
G.add_edge(5,1)
G.add_edge(1.5,"test")
G.add_edge("spam",(10,11))


'''
Finding shortest path
'''
Shortest_Path= nx.shortest_path(G)
print(Shortest_Path)

'''
Plotting the directed graph
'''
layout=nx.planar_layout(G)

nx.draw(G,pos=layout,arrows=True,with_labels=True,node_size=2600,node_color='#4ABF8C',
        node_shape='8',width=1.5)