
from django.urls import path, re_path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.show, name ='show'),
    #re_path(r'posts/(?P<id>[0-9]+)$', views.show),
]
