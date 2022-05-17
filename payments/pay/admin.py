from django.contrib import admin

from .models import Item, Price


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'stripe_price_id', 'price',)


admin.site.register(Item, ProductAdmin)
admin.site.register(Price, PriceAdmin)
