from django.urls import path
from . import views

app_name = 'Calculator'
urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('add_expenditure/', views.addExpenditure, name='addExpenditure'),
    path('add_income/', views.addIncome, name='addIncome')
]