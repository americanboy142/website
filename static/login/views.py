from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def sub(request):
    return render(request, 'login/home_sub.html')

def globe(request):
    return render(request, 'login/home_globe.html')


def home(request):
    return render(request, 'login/homepage.html')

def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        return render(request, 'login/login.html')
    return render(request, 'login/sign_up.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect("/home")
        else:
            messages.error(request,"Incorrect Username or Password")
            return render(request, 'login/login.html')
    return render(request, 'login/login.html')

def profile(request):
    if request.session.has_key('username'):
        post = request.session["username"]
        query = User.objects.filter(username=posts)
        return render(request, 'login/homepage.html', {'query':query})
    else: 
        return render(request, 'login/login.html', {})

    


            

