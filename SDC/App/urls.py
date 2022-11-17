from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit'),
    path('CodingProfile/', views.coding, name='coding'),
    path('registeration/', views.registeration, name='register'),
]
