from django.shortcuts import render

def calculator(request):
    return render(request, "Calculator/calculator.html")
