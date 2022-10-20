from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('bookmark/<int:bookmark_id>/', views.bookmark_delete, name='bookmark_delete'),
]