from django.urls import path
from base.views import *
from . import views


urlpatterns = [
    path('', home),
    path('orders/', OrderView.as_view(), name='orders'),
    path('order/<str:pk>/', order_detail, name='order'),
]