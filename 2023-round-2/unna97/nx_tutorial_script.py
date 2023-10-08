import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

print(nx.__version__)


def highlight_path_given(path_highlight, position, color="yellow", alpha=0.8, width=5):
    
    nx.draw_networkx_edges(
        example_directed_graph,
        edgelist=path_highlight,
        pos=position,
        edge_color=color,
        alpha=alpha,
        ax=ax,
        width=width,
    )

    nx.draw(example_directed_graph, pos=position, ax=ax, with_labels=True)


def update_fig(i):
    ax.clear()
    highlight_path_given(path_edges[i], position)
    fig.suptitle(f"Path {i + 1} of {len(path_edges)}")


def create_animation_highlight_paths(path_edges):

    ani = animation.FuncAnimation(
        fig,
        update_fig,
        frames=len(path_edges),
    )

    gif_file_path = r"shortest_paths.gif"
    writergif = animation.PillowWriter(fps=1)
    ani.save(gif_file_path, writer=writergif)
    return ani


if __name__ == "__main__":
    ### Intializing the graph:
    example_directed_graph = nx.DiGraph()

    ### Adding nodes from list:
    random_nodes = {
        'str': ['node_string','blue', 'random_str'],
        'int': [0,2,512],
        'tuple': [(1,'hey',85),((2,4), 41) ],
    }
    ### Adding nodes from dict:
    for key, values in random_nodes.items():
        example_directed_graph.add_nodes_from(values, type=key)


    ### Only unique node_values will be added
    print("nodes added:", example_directed_graph.nodes())
    nodes_in_graph = list(example_directed_graph.nodes())

    ### Adding random edges between nodes:
    for i in range(10):
        example_directed_graph.add_edge(
            random.choice(nodes_in_graph), random.choice(nodes_in_graph)
        )

    ### Edges will be also added only once, above will create at max 10:
    print("edges added:", example_directed_graph.edges())
    print("number of edges added:", example_directed_graph.number_of_edges())

    ### Finding shortest paths between nodes in an unweighted directed graph:
    ###In case of multiple shortest paths between two pair of nodes, only one is returned in methods belows:

    ### Method 1:
    print(
        "Method 1 shortest path between nodes:",
        nx.shortest_path(example_directed_graph),
    )

    ### Method 2: Get the generator of all pairs shortest paths:
    print(
        "Method 2 shortest path between nodes:",
        dict(nx.all_pairs_shortest_path(example_directed_graph)),
    )

    ### Method 3: Get the generator of single source shortest paths (for all nodes):
    for node in example_directed_graph.nodes():
        print(
            f"Method 3 shortest path between {node} and other reachable nodes",
            dict(nx.single_source_shortest_path(example_directed_graph, node)),
        )

    ### Plot the graph:
    nx.draw(
        example_directed_graph, with_labels=True, node_size=100, alpha=1, linewidths=10
    )
    plt.show()

    ### Create a gif, highlighting the shortest paths:
    position = nx.spring_layout(example_directed_graph)
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.close()
    paths = nx.shortest_path(example_directed_graph)
    path_edges = []

    for source_node in paths:
        for target_node in paths[source_node]:
            path = paths[source_node][target_node]
            path_edge = list(zip(path, path[1:]))
            path_edges.append(path_edge)
        print(path_edges)

    create_animation_highlight_paths(path_edges)

    ### All shortest paths between pairs of node:
    print("All shortest paths between all pairs of nodes:\n")

    for source_node in paths:
        for target_node in paths[source_node]:
            print(
                "source_node:",
                source_node,
                "target_node:",
                target_node,
                "\npaths:",
                list(
                    nx.all_shortest_paths(
                        example_directed_graph, source=source_node, target=target_node
                    )
                ),
            )
