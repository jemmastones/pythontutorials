from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

def home(request):
    #template_name = 'home.html'
    return render(request, 'home.html')