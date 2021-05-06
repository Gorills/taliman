
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.serv, name='serv'),
    path('<slug:slug>/', views.serv_detail, name='serv_detail'),
    path('<slug:parent>/<slug:slug>/', views.servchildren_detail, name='servchildren_detail'),
    
]