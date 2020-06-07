from django.shortcuts import render, redirect
from .models import Income, Expenditure, Topics

#Get income and expenditure and display them
def calculator(request):
    try:
        latest_income_list = Income.objects.get(user = request.user)
        latest_expenditure_list = Expenditure.objects.filter(user = request.user)
        topics_list = Topics.objects.all()
        totalExpenditureCost = 0
        hourly_rate_list = []
        for expense in latest_expenditure_list:
            totalExpenditureCost += expense.expenditure_price
            if expense.topic.topic_text == "Digital Subscription":
                hourly_rate = expense.expenditure_price/expense.sub_hours
                hourly_rate_list.append(hourly_rate)
            else:
                hourly_rate_list.append(-1)
        remainingIncome = latest_income_list.income_text - totalExpenditureCost
        fusion = zip(latest_expenditure_list, hourly_rate_list)
        context = {
            'latest_income': latest_income_list,
            'fusion': fusion,
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
        user_expenditure_hours = request.POST["sub_hours"]
        expenditure_list = Expenditure.objects.filter(user = request.user)
        exists = False
        for expense in expenditure_list:
            if expense.expenditure_text == user_expenditure:
                expense.expenditure_price += int(user_expenditure_price)
                expense.save()
                exists = True
        if not exists:
            expenditure_topic = Topics.objects.get(topic_text = request.POST["topic_text"])
            input_name = Expenditure.objects.create(expenditure_text = user_expenditure, expenditure_price = user_expenditure_price, sub_hours = user_expenditure_hours, topic = expenditure_topic, user = request.user)
        return redirect("Calculator:calculator")

def deleteExpenditure(request, expenditure_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            expenditure = Expenditure.objects.get(pk=expenditure_id)
            if expenditure.user == request.user:
                expenditure.delete()
                return redirect("Calculator:calculator")
            else:
                raise Http404("You are not authorized to delete this expense")
        else:
            raise Http404("You must login to delete expenses")



