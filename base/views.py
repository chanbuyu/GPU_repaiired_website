from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customer, Order

# Create your views here.
def home(request):
    return render(request, 'home.html')


class OrderView(TemplateView):
    template_name = 'order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Order.objects.all()
        context['order_list'] = data
        return context


def order_detail(request):
    num = request.GET.get('id', 1)
    print(num)
    order = Order.objects.get(id=num)
    context = {
        'order': order
    }
    return render(request, 'order.html', context)