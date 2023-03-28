import networkx as nx

G = nx.DiGraph()

nodeList = [1,"Outreachy","Purvi","Networkx",("t1","t2"),8] # 6 Nodes in total of different type - int, str, tuple

G.add_nodes_from(nodeList)  # Adding all nodes from nodeList

edgeList = [(1,8),(1,("t1","t2")),("Purvi","Networkx"),                 
            ("Outreachy",8),("Purvi","Outreachy"),("Networkx","Outreachy"),
            ("Outreachy", 1),("Networkx",("t1","t2"))]

G.add_edges_from(edgeList)  # Adding edges from edgeList

nx.draw(G, with_labels=True, font_weight='bold')  # Drawing the graph

shortestPaths = dict(nx.all_pairs_shortest_path(G))  # Finding shortest paths for all pairs of nodes in G
for key in shortestPaths:
  print(shortestPaths[key])