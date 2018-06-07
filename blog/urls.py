
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/<int:id>/', views.show),
    #re_path(r'posts/(?P<id>[0-9]+)$', views.show),
]
