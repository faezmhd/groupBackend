from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddOrder.as_view(), name='add-order'),
    path('me/', views.UserOrdersBuStatus.as_view(), name='order-list'),
    path('single/', views.OrderDetails.as_view(), name='order-details'),
]