from django import forms
from .models import Kategori, Marka, Fatura


class KategoriForm(forms.ModelForm):
    isim = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Kategori
        fields = ('isim',)


class MarkaForm(forms.ModelForm):
    isim = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Marka
        fields = ('isim',)


class FaturaForm(forms.ModelForm):
    numara = forms.CharField(max_length=255, required=True)
    tarih = forms.DateField()

    class Meta:
        model = Fatura
        fields = ('numara', 'tarih')
