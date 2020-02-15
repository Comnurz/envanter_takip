from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin

from envanter_takip.models import Urun, Marka, Kategori, Fatura, Zimmet
from django.views.generic import View, DetailView, ListView, TemplateView
from .forms import KategoriForm, MarkaForm, FaturaForm


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


class KategoriListView(ListView):
    context_object_name = 'kategoriler'
    template_name = 'envanter_takip/kategoriler.html'


    def get_queryset(self):
        return Kategori.objects.all()

    def post(self, request, *args, **kwargs):
        form = KategoriForm(request.POST)

        if form.is_valid():
            kategori_isim = form.cleaned_data.get('isim')
            isim = Kategori(isim=kategori_isim)
            isim.save()
        return redirect('kategoriler')



class MarkaListView(ListView):
    context_object_name = 'markalar'
    template_name = 'envanter_takip/markalar.html'

    def get_queryset(self):
        return Marka.objects.all()

    def post(self, request, *args, **kwargs):
        form = MarkaForm(request.POST)

        if form.is_valid():
            marka_isim = form.cleaned_data.get('isim')
            isim = Marka(isim=marka_isim)
            isim.save()
        return redirect('markalar')


class FaturaListView(ListView):
    context_object_name = 'faturalar'
    template_name = 'envanter_takip/faturalar.html'

    def get_queryset(self):
        return Fatura.objects.all()

    def post(self, request, *args, **kwargs):
        form = FaturaForm(request.POST)

        if form.is_valid():
            numara = form.cleaned_data.get('numara')
            tarih = form.cleaned_data.get('tarih')
            fatura = Fatura(numara=numara, tarih=tarih)
            fatura.save()

        return redirect('faturalar')

