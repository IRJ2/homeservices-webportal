from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_login/', views.clientLogin, name='client_login'),
    path('expert_login/', views.expertLogin, name='expert_login'),
    path('home_client/', views.homeClient, name='home_client'),
    path('home_expert/', views.homeExpert, name='home_expert'),
    path('client_signup/', views.clientSignup, name='client_signup'),
    path('client_profile/', views.clientProfile, name='client_profile'),
    path('expert_profile/', views.expertProfile, name='expert_profile'),
    path('expert_signup/', views.expertSignup, name='expert_signup'),
    path('expert_dis_profile/', views.expertDisplayProfile, name='expert_display_profile'),
    path('plumbing_service/', views.PlumbingListView.as_view(), name='plumbing_list'),
    path('ac_service/', views.ACServicingListView.as_view(), name='ac_list'),
    path('carpentry_service/', views.CarpentryListView.as_view(), name='carpentry_list'),
    path('electricworks_service/', views.ElectricWorksListView.as_view(), name='electricworks_list'),
    path('homecleaning_service/', views.HomeCleaningListView.as_view(), name='homecleaning_list'),
    path('laptoprepair_service/', views.LaptopRepairListView.as_view(), name='laptoprepair_list'),
    path('plumbing_service/<str:pk>', views.ExpertDetailView.as_view(), name='expert_detail'),
    path('logout/', views.logout, name='logout'),
]
