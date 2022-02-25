import sqlite3
import sys
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

createExecute = """CREATE TABLE IF NOT EXISTS HClusters(
                    X INT,
                    Y INT);
                    """


def Clustering(count: int, cl1: int, cl2: int):
    connection = sqlite3.connect('vessels.db')
    cursor = connection.cursor()
    cursor.execute(createExecute)
    connection.commit()

    cursor.execute("""delete from HClusters""")

    dataset = pd.read_csv(sys.path[0] + '/s.csv')
    X = dataset.iloc[:, [cl1, cl2]].values

    allClusters = []

    hc = AgglomerativeClustering(n_clusters=count, affinity='euclidean', linkage='ward')
    y_hc = hc.fit_predict(X)

    for i in range(count):
        allClusters.append(X[y_hc == i])

    for cl in allClusters:
        for i in range(len(cl)):
            cursor.execute("INSERT INTO HClusters VALUES({0}, {1});".format(cl[i][0], cl[i][1]))
            connection.commit()
    connection.close()

    return allClusters
