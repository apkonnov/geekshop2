from django.urls import path

from orders.views import OrderListView, OrderCreateView, \
    OrderDeleteView, OrderDetailView, OrderUpdateView, order_forming_complete

app_name = 'orders'

urlpatterns = [
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]
