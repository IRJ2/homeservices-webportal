from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_login/', views.clientLogin, name='client_login'),
    path('expert_login/', views.expertLogin, name='expert_login'),
    path('experts/', views.expertsList, name='experts_list'),
    path('detail/', views.expertsDetail, name='experts_detail'),
    path('home/', views.home, name='home'),
    path('client_signup/', views.clientSignup, name='client_signup'),
]
