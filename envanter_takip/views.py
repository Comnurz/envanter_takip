from django.shortcuts import render
from envanter_takip.models import Urun, Marka, Kategori, Fatura, Zimmet
from django.views.generic import View, DetailView, ListView, TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'envanter_takip/index.html'
    context_object_name = 'urun_listesi'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        urunler = Urun.objects.all()
        markalar = Marka.objects.all()
        kategoriler = Kategori.objects.all()
        faturalar = Fatura.objects.all()
        context['urunler'] = urunler
        context['markalar'] = markalar
        context['kategoriler'] = kategoriler
        context['faturalar'] = faturalar
        return context


class UrunListView(ListView):
    context_object_name = 'urun_listesi'
    template_name = 'envanter_takip/urunler.html'

    def get_queryset(self):
        return Urun.objects.all()
