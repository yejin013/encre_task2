from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('registration', views.CreateUser.as_view(), name='registration'),
    path('login', views.Login.as_view(), name='login'),
]