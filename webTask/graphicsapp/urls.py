from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('means-dwt-year', views.dwt_year),
    path('means-dwt-size', views.dwt_size),
    path('means-size-year', views.size_year),

    path('dwt-year', views.dwt_year),
    path('dwt-year', views.dwt_year),
    path('dwt-year', views.dwt_year),

]