from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Customer, Order

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    orders_search = None
    if q != '':
        print(q)
        orders_search = Order.objects.filter(customer__telephone__icontains=q)
    data = Order.objects.all()[0:10]
    context = {'orders_search': orders_search, 'order_list': data, 'q': q}
    return render(request, 'base/home.html', context)



def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        'order': order
    }
    return render(request, 'base/order.html', context)