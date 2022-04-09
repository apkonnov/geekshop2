from django.contrib import admin

from baskets.models import Basket

admin.site.register(Basket)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 1
