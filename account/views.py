from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {'form' : form }
    return render(request, 'accounts/login-page.html', context = context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout-page.html')


def Register_view(request):
    form = UserCreationForm(request.POST or None)
    context = {'form' : form}
    print(form)
    if form.is_valid():
        New_User = form.save()
        return redirect('/login/')
    return render(request, 'accounts/register-page.html', context = context)