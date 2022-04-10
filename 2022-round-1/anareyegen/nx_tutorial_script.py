import networkx as nx

DG = nx.DiGraph()

# Adding nodes
DG.add_node("a")
DG.add_node("t")
DG.add_node("w")
DG.add_node("f")
DG.add_node("o")
DG.add_node("q")
DG.add_node("e")


# Adding edges to nodes
DG.add_edges_from([("a","t"),("a","f"),("t","o"),("w","o"), ("f","t"), ("q","e")]) 
DG.add_edges_from([("a",4),("f",8), ("t", 2), ("w", 5), ("f", 7), ("q", 1)])
DG.add_edge("o", 10)
DG.add_edge("w",(1,7))

# Drawing the DiGraph
nx.draw(DG, with_labels=True)

# Find and print the shortest path
shortest_path = nx.shortest_path(DG)
print(shortest_path)
print(list(DG.successors('a')))

# Output:
# print(shortest_path)   {'a': {'a': ['a'], 't': ['a', 't'], 'f': ['a', 'f'], 4: ['a', 4], 
#                 'o': ['a', 't', 'o'], 2: ['a', 't', 2], 8: ['a', 'f', 8], 7: ['a', 'f', 7], 
#                 10: ['a', 't', 'o', 10]}, 't': {'t': ['t'], 'o': ['t', 'o'], 2: ['t', 2], 10: ['t', 'o', 10]}, 
#                 'w': {'w': ['w'], 'o': ['w', 'o'], 5: ['w', 5], (1, 7): ['w', (1, 7)], 10: ['w', 'o', 10]}, 
#                 'f': {'f': ['f'], 't': ['f', 't'], 8: ['f', 8], 7: ['f', 7], 'o': ['f', 't', 'o'], 
#                 2: ['f', 't', 2], 10: ['f', 't', 'o', 10]}, 'o': {'o': ['o'], 10: ['o', 10]}, 
#                 'q': {'q': ['q'], 'e': ['q', 'e'], 1: ['q', 1]}, 'e': {'e': ['e']}, 4: {4: [4]}, 
#                 8: {8: [8]}, 2: {2: [2]}, 5: {5: [5]}, 7: {7: [7]}, 1: {1: [1]}, 10: {10: [10]}, 
#                 (1, 7): {(1, 7): [(1, 7)]}}
# print(list(DG.successors('a'))):  ['t', 'f', 4]