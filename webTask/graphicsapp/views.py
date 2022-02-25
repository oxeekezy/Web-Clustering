from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from . import kmeans


def index(request):

    return render(request, 'graphicsapp/index.html')


def bokeh(request):
    plot = kmeans.Clustering(4, 6, 7, 'DWT', 'YEAR')

    script, div = components(plot)

    return render(request, 'graphicsapp/bokeh.html', {'script': script, 'div': div})


