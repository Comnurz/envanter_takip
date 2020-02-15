from django.contrib import admin
from envanter_takip.models import Invoice, Category, Brand, Debit, Product


# Register your models here.
admin.site.register(Invoice)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Debit)
admin.site.register(Product)
