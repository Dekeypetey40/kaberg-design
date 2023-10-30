from django.urls import path

from . import views

urlpatterns = [
    path('ping/', views.mailchimp_ping),
    path('', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]