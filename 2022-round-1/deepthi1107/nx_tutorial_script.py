#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the required libraries
import networkx as nx


# In[2]:


#Creating DiGraph
graph1=nx.DiGraph()


# In[3]:


#adding node 11,"N1",1,2,3,(4,5)
graph1.add_node(11)
graph1.add_node("N1")
L=[1,2,3]
graph1.add_nodes_from(L)
graph1.add_node((4,5))


# In[4]:


#view of all the nodes inserted to the DiGraph
graph1.nodes()


# In[5]:


#adding edges 11->"N1",1->2,2->3,3->11,N1->(4,5),(4,5)->1
graph1.add_edge(11,"N1")
graph1.add_edge(1,2)
graph1.add_edge(2,3)
graph1.add_edge(3,11)
graph1.add_edge("N1",(4,5))
graph1.add_edge((4,5),1)


# In[6]:


#view of edges, connecting the nodes
graph1.edges()


# In[7]:


#visualization of DiGraph created
nx.draw(graph1,with_labels=1)


# In[8]:


#finding the shoretes path between the nodes and printing the shortest path
s_path = nx.shortest_path(graph1)
print(s_path)

