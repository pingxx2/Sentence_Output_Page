from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmark/<int:sentence_id>/', views.vote_bookmark, name="bookmark"),
]