from django import forms
from .models import Category, Brand, Invoice, Product


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Category
        fields = ('name',)


class BrandForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Brand
        fields = ('name',)


class InvoiceForm(forms.ModelForm):
    number = forms.CharField(max_length=255, required=True)
    date = forms.DateField(required=True)

    class Meta:
        model = Invoice
        fields = ('number', 'date')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
