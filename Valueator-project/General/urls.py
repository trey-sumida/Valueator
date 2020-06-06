from django.urls import path
from . import views

app_name = 'General'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
]