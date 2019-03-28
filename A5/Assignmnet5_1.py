import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


graph = nx.karate_club_graph()
edgeCount = graph.number_of_edges()
maximumClusterThreshold = 5
count = 0
clusterCount = nx.algorithms.number_connected_components(graph)

# Drawing the initial karateclub graph
nx.draw(graph, with_labels=True)
plt.show()

while (edgeCount > 0 and clusterCount < maximumClusterThreshold):
   betweennessDict = nx.algorithms.betweenness.edge_betweenness(graph)
   maximumBetweennessValue = np.max(list(betweennessDict.values()))
   edgeValue = ''
   
   for edge in betweennessDict:
      if betweennessDict[edge] == maximumBetweennessValue:
         edgeValue = edge
         
   print ('Removing Edges...',str(edgeValue[0])+"--->"+str(edgeValue[1]))     
   graph.remove_edge(edgeValue[0], edgeValue[1])

   # Drawing the sequential karateclub graph
   nx.draw(graph, with_labels=True)
   plt.show()

   count = count + 1
   clusterCount = nx.algorithms.number_connected_components(graph)

print('Total flows to separation:',count)
