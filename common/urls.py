from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('bookmark/',views.bookmark, name='bookmark'),
=======
    #path('bookmark/',views.bookmark, name='bookmark'),
>>>>>>> fb34df3c6a43ffedf2cbd4bb1681faed620fab51
]