import importlib

kmeans = importlib.import_module('k-means')
hierarchy = importlib.import_module('hierarchy')

k_clsDY = kmeans.Clustering(4, 6, 7)
k_clsDS = kmeans.Clustering(4, 6, 5)
k_clsSY = kmeans.Clustering(5, 5, 7)

h_clsDY = hierarchy.Clustering(4, 6, 7)
h_clsDS = hierarchy.Clustering(4, 6, 5)
h_clsSY = hierarchy.Clustering(5, 5, 7)