from django.urls import path
from extras import views

urlpatterns= [
    path('addresslist/', views.GetUserAddresses.as_view(), name='user-address'),
    path('add/', views.AddAddress.as_view(), name='add-address'),
    path('default/', views.SetDefaultAddress.as_view(), name='default-address'),
    path('delete/', views.DeleteAdress.as_view(), name='delete-address'),
    path('me/', views.GetDefaultAddress.as_view(), name='delete-address'),

]