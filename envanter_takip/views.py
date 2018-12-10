from django.shortcuts import render
from envanter_takip.models import Urun
from django.views.generic import View, DetailView, ListView, TemplateView


# Create your views here.
class UrunListView(ListView):
    context_object_name = 'urun_listesi'
    template_name = 'envanter_takip/urunler.html'

    def get_queryset(self):
        urunler = Urun.objects.all()
        urun_listesi = []
        for urun in urunler:
            urun_ = {}
            urun_['fatura'] = urun.fatura
            urun_['urun_kod'] = urun.urun_kod
            urun_['urun_no'] = urun.urun_no
            urun_['urun_ozellik'] = urun.ozellik
            urun_['marka'] = urun.marka
            urun_['kategori'] = urun.kategori
            urun_['zimmet'] = urun.zimmet
            urun_listesi.append(urun_)
        return urun_listesi
