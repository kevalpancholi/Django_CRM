from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # In case you want to create a separate login page
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]