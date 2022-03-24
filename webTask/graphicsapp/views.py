from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from . import kmeans


def index(request):
    return render(request, 'graphicsapp/index.html')


def dwt_year(request):
    plot = kmeans.Clustering(4, 6, 7, 'DWT', 'YEAR')
    script, div = components(plot)
    return render(request, 'graphicsapp/bokeh.html', {'script': script, 'div': div})


def dwt_size(request):
    plot = kmeans.Clustering(4, 6, 5, 'DWT', 'SIZE')
    script, div = components(plot)
    return render(request, 'graphicsapp/bokeh.html', {'script': script, 'div': div})


def size_year(request):
    plot = kmeans.Clustering(5, 5, 7, 'SIZE', 'YEAR')
    script, div = components(plot)
    return render(request, 'graphicsapp/bokeh.html', {'script': script, 'div': div})