from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customer, Order

# Create your views here.
def home(request):
    return render(request, 'home.html')