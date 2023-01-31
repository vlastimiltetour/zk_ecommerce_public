from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('mail/', views.mail_letter, name='mail_letter'),
]   