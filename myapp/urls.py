
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('portfolio/', views.PortfolioList.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>/', views.PortfolioDetail.as_view(), name='portfolio_detail'),
]
