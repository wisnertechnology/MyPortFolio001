from django.contrib import admin
from django.urls import include, path

from blog import views

app_name ='blog'
urlpatterns = [
    path('', views.acceuil, name='akey'),
    path('index', views.profil, name='profil'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),

]