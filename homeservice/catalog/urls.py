from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_login/', views.clientLogin, name='client_login'),
    path('expert_login/', views.expertLogin, name='expert_login'),
    path('experts/', views.expertsList, name='experts_list'),
    path('detail/', views.expertsDetail, name='experts_detail'),
    path('home_client/', views.homeClient, name='home_client'),
    path('home_expert/', views.homeExpert, name='home_expert'),
    path('client_signup/', views.clientSignup, name='client_signup'),
    path('client_profile/', views.clientProfile, name='client_profile'),
    path('expert_profile/', views.expertProfile, name='expert_profile'),
    path('expert_dis_profile/', views.expertDisplayProfile, name='expert_display_profile'),
]
