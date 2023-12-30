import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

edgelist = pd.read_csv('edgelist.csv', header=None).to_numpy()
G = nx.from_edgelist(edgelist).to_undirected()
pos_f = lambda n: ((n-1)%5 , 5-((n-1)//5))
pos = {n: pos_f(n) for n in G.nodes}
nx.draw_networkx(G, pos)
plt.savefig('library_labyrinth.png')
