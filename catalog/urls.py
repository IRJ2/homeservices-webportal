from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_login/', views.client_login, name='client_login'),
    path('worker_login/', views.worker_login, name='worker_login'),
]
