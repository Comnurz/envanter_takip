from django import forms
from .models import Kategori, Marka


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
