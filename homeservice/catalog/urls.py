from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_login/', views.clientLogin, name='client_login'),
    path('worker_login/', views.workerLogin, name='worker_login'),
    path('experts/', views.expertsList, name='experts_list'),
    path('detail/', views.expertsDetail, name='experts_detail'),
]
