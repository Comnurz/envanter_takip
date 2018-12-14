from django import forms
from .models import Kategori


class KategoriForm(forms.ModelForm):
    isim = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Kategori
        fields = ('isim',)
