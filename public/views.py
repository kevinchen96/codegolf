# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def home(request):
    return render(request, "public/home.html.tpl", {'name': request.user.username})
