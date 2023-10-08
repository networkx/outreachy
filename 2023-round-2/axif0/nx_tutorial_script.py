import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph and add nodes and edges
def create_graph():
    G = nx.DiGraph()
    nodes = ['Outreachy', 1, (1, 2), 1.1, True, 'networkx', (2, 3), 2.2, False, 'asif']
    G.add_nodes_from((node, {'color': 'blue'}) for node in nodes)
    edges = [('Outreachy', 1), (1, (1, 2)), ((1, 2), 1.1), (1.1, True), (True, 'networkx'), ('networkx', (2, 3)), ((2, 3), 2.2), (2.2, False), (False, 'asif'), ('asif', 'Outreachy'), ('Outreachy', 2.2), (1, (2, 3)), ((1, 2), True), (1.1, False)]
    G.add_edges_from((edge[0], edge[1], {'color': 'green'}) for edge in edges)
    return G

#  Calculate the shortest path between all pairs of nodes
def calculate_shortest_path(G):
    paths = nx.floyd_warshall(G)
    for source, targets in paths.items():
        for target, path in targets.items():
            print(f'Shortest path from {source} to {target}: {path}')

# Calculate the degree centrality of the nodes
def calculate_centrality(G):
    centrality = nx.degree_centrality(G)
    print('Degree centrality:', centrality)

# Draw and show the graph
def plot_graph(G):
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color=[data['color'] for node, data in G.nodes(data=True)], edge_color=[data['color'] for _, _, data in G.edges(data=True)])
    plt.show()

def main():
    G = create_graph()
    calculate_shortest_path(G)
    calculate_centrality(G)
    plot_graph(G)

if __name__ == "__main__":
    main()
