#from django.urls import re_path as path 
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('results/<poll_id>/', views.results, name='results'),
    path('vote/<poll_id>/', views.vote, name='vote'),
]