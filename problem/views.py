# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProblemForm
from django.shortcuts import render
from .models import Problem
from django.template import RequestContext, loader

@staff_member_required
def add_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = Problem(title = form.cleaned_data['title'], description = form.cleaned_data['description'], test_in = form.cleaned_data['test_in'], test_out = form.cleaned_data['test_out'])
            problem.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "problem/add_problem.html.tpl", {'form': form})
            
    else:
        form = ProblemForm()
        return render(request, "problem/add_problem.html.tpl", {'form': form})
