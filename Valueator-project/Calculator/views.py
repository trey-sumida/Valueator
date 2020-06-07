from django.shortcuts import render, redirect
from .models import Income, Expenditure, Topics

#Get income and expenditure and display them
def calculator(request):
    try:
        latest_income_list = Income.objects.get(user = request.user)
        latest_expenditure_list = Expenditure.objects.filter(user = request.user)
        topics_list = Topics.objects.all()
        totalExpenditureCost = 0
        for expense_cost in latest_expenditure_list:
            totalExpenditureCost += expense_cost.expenditure_price
        remainingIncome = latest_income_list.income_text - totalExpenditureCost
        context = {
            'latest_income': latest_income_list,
            'latest_expenditure': latest_expenditure_list,
            'topics_list': topics_list,
            'totalExpenditureCost': totalExpenditureCost,
            'remainingIncome': remainingIncome
        }
        return render(request, "Calculator/calculator.html", context)
    except:
        return render(request, "Calculator/calculator.html")

def addIncome(request):
    if request.method == 'POST':
        user_income_input = request.POST["income_text"]
        try:
            prev_income = Income.objects.get(user = request.user)
            prev_income.income_text = user_income_input
            prev_income.save()
        except:
            input = Income.objects.create(income_text = user_income_input, user = request.user)
        return redirect("Calculator:calculator")

def addExpenditure(request):
    if request.method == 'POST':
        user_expenditure = request.POST["expenditure_text"]
        user_expenditure_price = request.POST["expenditure_price"]
        expenditure_topic = Topics.objects.get(topic_text = request.POST["topic_text"])
        input_name = Expenditure.objects.create(expenditure_text = user_expenditure, expenditure_price = user_expenditure_price, topic = expenditure_topic, user = request.user)
        return redirect("Calculator:calculator")



