  
from django.urls import path
from . import views

app_name = 'Calculator'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('calculator/', views.calculator, name='calculator'),
]