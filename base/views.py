from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Customer, Order

# Create your views here.
status = {'have order': '正在清洗中..',
          'have clean': '已清洗，正在修复中..',
          'repaired': '已修复，正在检测中..',
          'finish': '各项检测正常，已发回'}

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    orders_search = None
    if q != '':
        print(q)
        orders_search = Order.objects.filter(customer__telephone__icontains=q)
    data = Order.objects.all()[0:5]
    context = {'orders_search': orders_search, 'order_list': data, 'status': status}
    return render(request, 'base/home.html', context)



class OrderView(TemplateView):
    template_name = 'base/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Order.objects.all()
        context['order_list'] = data
        return context


def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        'order': order
    }
    return render(request, 'base/order.html', context)