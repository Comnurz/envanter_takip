from django.urls import path
from django.contrib.auth import views as auth_views
from envanter_takip.views import ProductListView, HomePageView, CategoryListView, BrandListView, InvoiceListView

urlpatterns = [
    path(r'', HomePageView.as_view(), name='ana_sayfa'),
    path(r'urunler', ProductListView.as_view(), name='urunler'),
    path(r'kategoriler', CategoryListView.as_view(), name='kategoriler'),
    path(r'markalar', BrandListView.as_view(), name='markalar'),
    path(r'faturalar', InvoiceListView.as_view(), name='faturalar'),
    path(r'login', auth_views.LoginView.as_view(), name='login'),
    path(r'logout', auth_views.LogoutView.as_view(), name='logout')
]
