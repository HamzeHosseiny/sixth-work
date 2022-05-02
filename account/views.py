from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
   # if request.method == "POST":
        
        
    if user is not None:
        login(request, user)
        return render(request, 'accounts/login-page.html')
    else:
        error = "username or password in not right!"
        context = {
            'massage' : error
        }
        return render(request, 'accounts/login-page.html')
