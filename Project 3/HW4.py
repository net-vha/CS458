import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt


#skipping the distance calculation part and directly using the Distance Matrix
mat = np.array([[0.00,0.1,.41,.55,.35], [.1,0,.64,.47,.98], [.41,.64,0,.44,.85], [.55,.47,.44,0,.76], [.35,.98,.85,.76,0]])
dists = squareform(mat)


#This step is where we mention its "Single Link" Cluster
#replace link and title for desired form and title
linkage_matrix = linkage(dists, 'single')

dendrogram(linkage_matrix, labels=["P1","P2","P3","P4","P5"])
plt.title("Single Link")
plt.show()