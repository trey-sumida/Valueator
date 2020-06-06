from django.shortcuts import render

def homepage(request):
    return render(request, "General/homepage.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, "General/login.html", {'error': "Invalid Login"})
    else:
        return render(request, "General/login.html")
