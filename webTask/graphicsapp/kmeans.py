import sys
import time

import pandas as pd
from sklearn.cluster import KMeans
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, BoxSelectTool
import random


def Clustering(count: int, cl1: int, cl2: int, x_label, y_label):
    colors = ["DarkTurquoise", "Plum", "Peru", "Crimson", "MediumSeaGreen", "MediumSlateBlue"]

    dataset = pd.read_csv(sys.path[0] + '/s.csv')

    X = dataset.iloc[:, [cl1, cl2]].values

    kmeans = KMeans(n_clusters=count, init='k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(X)

    plot = figure(tools="pan,wheel_zoom,box_zoom,reset",
                  plot_width=1000,
                  plot_height=600,
                  title=str(x_label)+str(' отностильно ')+str(y_label),
                  x_axis_label=x_label,
                  y_axis_label=y_label)
    plot.background_fill_color = 'PowderBlue'
    plot.background_fill_alpha = 0.3

    for i in range(count):
        color_index = random.randint(0, len(colors) - 1)
        plot.circle(X[y_kmeans == i, 0], X[y_kmeans == i, 1], size=7, color=colors[color_index])
        plot.circle(kmeans.cluster_centers_[i, 0], kmeans.cluster_centers_[i, 1], size=20, color="yellow")
        colors.remove(colors[color_index])

    return plot
