from django.urls import path
from envanter_takip.views import UrunListView, HomePageView, KategoriListView

urlpatterns = [
    path(r'', HomePageView.as_view(), name='ana_sayfa'),
    path(r'urunler', UrunListView.as_view(), name='urun_listesi'),
    path(r'kategoriler', KategoriListView.as_view(), name='kategoriler'),
]
