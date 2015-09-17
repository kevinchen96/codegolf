# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print request.POST['username']+" has been added to codegolf"
            user = form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "accounts/register.html.tpl", {'form': form})
            
    else:
        form = UserCreationForm()
        return render(request, "accounts/register.html.tpl", {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print "disabled"
            else:
                print "bad login"
                return render(request, "accounts/login.html.tpl", {'error':"The username and password pair did not match."})
    return render(request, "accounts/login.html.tpl", {})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
