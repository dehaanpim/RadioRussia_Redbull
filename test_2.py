import networkx as nx
G=nx.Graph()
G.add_node("spam")
G.add_edge(1,2)
print(list(G.nodes()))
[1, 2, 'spam']
print(list(G.edges()))
[(1, 2)]