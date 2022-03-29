'''
-----------------------------------
        NX_TUTORIAL_SCRIPT
-----------------------------------
'''

import networkx as nx


'''
Declaration of Directed Graph
'''
NetworkX=nx.DiGraph()

# Adding edges will automatically declare the nodes

NetworkX.add_edge(5,6)
NetworkX.add_edge(1,(10,11))
NetworkX.add_edge("spam",5)
NetworkX.add_edge((10,11),1)
NetworkX.add_edge("test",6)
NetworkX.add_edge(5,1)
NetworkX.add_edge(1.5,"test")
NetworkX.add_edge("spam",(10,11))


'''
Finding shortest path
'''
Shortest_Path= nx.shortest_path(NetworkX)


'''
Plotting the directed graph
'''
layout=nx.planar_layout(NetworkX)

nx.draw(NetworkX,pos=layout,arrows=True,with_labels=True,node_size=2600,node_color='#4ABF8C',
        node_shape='8',width=1.5)

