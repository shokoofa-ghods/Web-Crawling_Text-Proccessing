import numpy as np
from TextRank import TextRank
import matplotlib.pyplot as plt
import networkx as nx
from slExtractor import story_line,link_extractor

links = link_extractor()
mvst = story_line(links[:5])
print(mvst)

d = {} #keeps title and keywords of storyLine
all = [] #adjacency list for weight of each node
labeldict = {} #to be used in networkx for labeling the nodes

for index, movie in enumerate(mvst):
   title = movie['title']
   labeldict[index]=title
   stry = movie['stry']
   tr = TextRank(stry)
   d[title] = tr.score_provider()

#check for common keywords
for k, v in d.items():
    w = []
    for kk, vv in d.items():
        inter = len(set(v).intersection(set(vv)))
        if k!=kk and inter:
            w.append(inter)
        else:
            w.append(0)

    all.append(w) 
# print(all)


arr = np.array(all) #convert list to numpy array
print(arr)

#assign np array to G graph
G = nx.from_numpy_matrix(np.matrix(arr), create_using=nx.Graph)

layout = nx.spring_layout(G)
nx.draw(G, layout, labels = labeldict, with_labels = True)
nx.draw_networkx_edge_labels(G, pos=layout)
plt.show()


#write graph to csv file 
nx.write_edgelist(G, "edge.csv")