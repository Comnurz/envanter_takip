from django.urls import path
from envanter_takip.views import UrunListView, HomePageView

urlpatterns = [
    path(r'', HomePageView.as_view(), name='ana_sayfa'),
    path(r'urunler', UrunListView.as_view(), name='urun_listesi'),
]
