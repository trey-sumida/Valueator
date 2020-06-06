from django.shortcuts import render


def homepage(request):
    return render(request, "Calculator/homepage.html")

def calculator(request):
    return render(request, "Calculator/calculator.html")
