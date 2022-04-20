from django.urls import path

#from orders.views import index, products

app_name = 'orders'

urlpatterns = [
    path('', orders, name='index'),
    # path('category/<int:category_id>/', products, name='category'),
    # path('page/<int:page>/', products, name='page'),
]
