from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customer, Order

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    orders = Order.objects.filter(customer__telephone__icontains=q)
    print(orders)
    context = {'orders': orders}
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