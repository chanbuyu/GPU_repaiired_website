from django.urls import path
from base.views import *
from . import views


urlpatterns = [
    path('', home),
    path('orders/', OrderView.as_view()),
    path('order', order_detail)
]