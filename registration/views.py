from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import  reverse
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('register:register'))
    else:
        form = RegisterForm()
    return render(response, "accounts/register.html", {"form": form})

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #Redirect to success page
    else:
        print('a')
        #Return an ivalid login error message


# Create your views here.
