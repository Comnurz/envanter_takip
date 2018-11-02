from django.contrib import admin
from envanter_takip.models import Fatura, Kategori, Marka, Zimmet, Urun


# Register your models here.
admin.site.register(Fatura)
admin.site.register(Kategori)
admin.site.register(Marka)
admin.site.register(Zimmet)
admin.site.register(Urun)
