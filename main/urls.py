from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    #path('bookmark/', views.bookmark, name='bookmark'),
=======
    path('bookmark/', views.bookmark, name='bookmark'),
>>>>>>> fb34df3c6a43ffedf2cbd4bb1681faed620fab51
]