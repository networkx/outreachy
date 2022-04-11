#!/usr/bin/env python
# coding: utf-8

# In[3]:


import networkx as nx
print(nx.__version__)


# #### Create a graph

# In[11]:


my_graph = nx.DiGraph()


# #### Adding nodes

# In[13]:


# add an int node 
my_graph.add_node(1)

# add two string nodes from a list
my_graph.add_nodes_from(["second", "third"])

# add a tuple node
my_graph.add_nodes_from([
    (4, {"food": "fries"}),
    (5, {"food": "salad"}),])


# #### Add edges

# In[ ]:




