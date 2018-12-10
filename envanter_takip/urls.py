from django.urls import path
from envanter_takip.views import UrunListView

urlpatterns = [
    path(r'urunler', UrunListView.as_view(), name='urun_listesi'),
]
