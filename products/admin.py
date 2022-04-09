from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'quantity')
    search_fields = ('name',)
    ordering = ('-category', 'name',)
    fields = ('category', 'name', ('price', 'quantity'), 'description', 'image')
    readonly_fields = ('description',)

