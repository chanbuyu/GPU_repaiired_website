from django.urls import path
from base.views import *
from . import views


urlpatterns = [
    path('', home),
    path('order/<str:pk>/', order_detail, name='order'),
]