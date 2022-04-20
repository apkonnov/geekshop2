from baskets.models import Basket


def basket(request):
    baskets_list = []
    if request.user.is_authenticated:
        baskets_list = Basket.objects.filter(user=request.user).order_by('product__category')
    return {'baskets': baskets_list}
