from django.urls import path
from base.views import order_view as views

urlpatterns = [
    path('add/', views.addOrderItems, name='orders-add'),
    path('myOrders/', views.getMyOrders, name='myOrders'),

    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
