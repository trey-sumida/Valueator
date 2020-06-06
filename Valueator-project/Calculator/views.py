from django.shortcuts import render
from .models import Income, Expenditure

#Get income and expenditure and display them
def calculator(request):
    latest_income_list = Income.objects.get(user = request.user)
    latest_expenditure_list = Expenditure.objects.filter(user = request.user)
    context = {'latest_income': latest_income_list, 'latest_expenditure': latest_expenditure_list}
    print(context)
    return render(request, "Calculator/calculator.html", context)
