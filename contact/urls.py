from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('contact_popup/', views.ContactPopupView.as_view(), name='contact_popup'),


    # path('feedback/', views.post_new, name='contactfull'),


    path('thank-you/', views.thank, name='thank'),
    path('review/', views.review, name='review'), 
    path('review/create/', views.ReviewView.as_view(), name='rewiew_create'),
    
]
