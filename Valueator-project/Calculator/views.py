from django.shortcuts import render
from .models import Income, Expenditure

def calculator(request):
    return render(request, "Calculator/calculator.html")
