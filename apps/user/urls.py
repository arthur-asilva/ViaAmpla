from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserLogin, name='login'),
    path('logout/', views.UserLogin, name='logout'),
]