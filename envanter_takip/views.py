from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin

from envanter_takip.models import Urun, Marka, Kategori, Fatura, Zimmet
from django.views.generic import View, DetailView, ListView, TemplateView
from .forms import KategoriForm, MarkaForm, FaturaForm, UrunForm


# Create your views here.
class HomePageView(TemplateView):
    context_object_name = 'liste'
    template_name = 'envanter_takip/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        urunler = Urun.objects.all()
        markalar = Marka.objects.all()
        kategoriler = Kategori.objects.all()
        faturalar = Fatura.objects.all()
        zimmetler = Zimmet.objects.all()
        context['urunler'] = urunler
        context['markalar'] = markalar
        context['kategoriler'] = kategoriler
        context['faturalar'] = faturalar
        context['zimmet'] = zimmetler
        return context


class UrunListView(TemplateView):
    context_object_name = 'liste'
    template_name = 'envanter_takip/urunler.html'

    def get_context_data(self, **kwargs):
        context = super(UrunListView, self).get_context_data(**kwargs)

        urunler = Urun.objects.all()
        markalar = Marka.objects.all()
        faturalar = Fatura.objects.all()
        kategoriler = Kategori.objects.all()
        context['urunler'] = urunler
        context['markalar'] = markalar
        context['kategoriler'] = kategoriler
        context['faturalar'] = faturalar
        context['form'] = UrunForm(self.request.POST or None)

        return context

    def post(self, request, *args, **kwargs):
        form = UrunForm(request.POST)

        if form.is_valid():
            urun_kod = form.cleaned_data.get('urun_kod')
            urun_no = form.cleaned_data.get('urun_no')
            ozellik = form.cleaned_data.get('ozellik')
            marka_id = form.cleaned_data.get('marka')
            kategori_id = form.cleaned_data.get('kategori')
            fatura_id = form.cleaned_data.get('fatura')
            zimmet_id = form.cleaned_data.get('zimmet')
            urun = Urun(urun_kod=urun_kod, urun_no=urun_no, ozellik=ozellik, marka=marka_id, kategori=kategori_id,
                        fatura=fatura_id, zimmet=zimmet_id)
            urun.save()
        return redirect('urunler')

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

