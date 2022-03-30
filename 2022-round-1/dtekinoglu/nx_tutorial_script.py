import networkx as nx

G = nx.Graph()

nodeList = [0,"Outreachy","Dilara","Networkx",("t1","t2"),3] # 6 Nodes in total

G.add_nodes_from(nodeList)  # Adding all nodes from nodeList

edgeList = [(0,3),(0,("t1","t2")),("Dilara","Networkx"),                 
            ("Outreachy",3),("Dilara","Outreachy"),("Networkx","Outreachy"),
            ("Outreachy",0),("Networkx",("t1","t2"))]

G.add_edges_from(edgeList)  # Adding edges from edgeList

nx.draw(G, with_labels=True, font_weight='bold')  # Drawing the graph

shortestPaths = dict(nx.all_pairs_shortest_path(G))  # Finding shortest paths for all pairs of nodes in G
for key in shortestPaths:
  print(shortestPaths[key])