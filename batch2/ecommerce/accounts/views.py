from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register_user(request):
    """Register user logic."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html',{'form': form})

def login_user(request):
    """Login user logic."""
    if request.method == 'POST':
        # instance of login form
        form = LoginForm(request.POST)
        # checking validation
        if form.is_valid():
            # extracting form data i.e username and password
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # checking whether the given credentials is valid or not
            user = authenticate(request,username=username,password=password)
            # if user is valid then logged in that user
            if user is not None:
                login(request,user)
                return redirect('home-page')
            else:
                return redirect('login_user')
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home-page')
