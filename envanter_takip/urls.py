from django.urls import path
from envanter_takip.views import ProductListView, HomePageView, CategoryListView, BrandListView, InvoiceListView

urlpatterns = [
    path(r'', HomePageView.as_view(), name='ana_sayfa'),
    path(r'urunler', ProductListView.as_view(), name='urunler'),
    path(r'kategoriler', CategoryListView.as_view(), name='kategoriler'),
    path(r'markalar', BrandListView.as_view(), name='markalar'),
    path(r'faturalar', InvoiceListView.as_view(), name='faturalar'),
]
