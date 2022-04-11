#!/usr/bin/env python
# coding: utf-8

# In[3]:


import networkx as nx
print(nx.__version__)


# #### Create a graph

# In[25]:


my_graph = nx.DiGraph()


# #### Adding nodes

# In[26]:


# add an int node 
my_graph.add_node(1)

# add two string nodes from a list
my_graph.add_nodes_from(["second", "third"])

# add a tuple node
my_graph.add_nodes_from([
    (4, {"food": "fries"}),
    (5, {"food": "salad"}),])


# #### Add weighted edges

# In[35]:


my_graph.add_weighted_edges_from([(1, "second", 3), (1, "third", 5), ("second", "third", 1), ("second", 4, 2), (4, 5, 1), ("third", 5, 6)] )


# #### Find number of nodes and number of edges

# In[36]:


my_graph.number_of_nodes()


# In[37]:


my_graph.number_of_edges()


# #### Find the shortest path between all pairs of nodes

# In[46]:


shortest_path = nx.shortest_path(my_graph)
print(shortest_path)


# #### Plot my_graph

# In[38]:


nx.draw(my_graph, with_labels=True, font_weight='bold')

