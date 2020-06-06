from django.urls import path
from . import views

app_name = 'Calculator'
urlpatterns = [
    path('', views.calculator, name='calculator'),
]