from django.shortcuts import redirect

from envanter_takip.models import Product, Brand, Category, Invoice, Debit
from django.views.generic import ListView, TemplateView
from .forms import CategoryForm, BrandForm, InvoiceForm, ProductForm


class HomePageView(TemplateView):
    context_object_name = 'liste'
    template_name = 'envanter_takip/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        brands = Brand.objects.all()
        categories = Category.objects.all()
        invoices = Invoice.objects.all()
        debits = Debit.objects.all()
        context['urunler'] = products
        context['markalar'] = brands
        context['kategoriler'] = categories
        context['faturalar'] = invoices
        context['zimmet'] = debits
        return context


class ProductListView(TemplateView):
    context_object_name = 'liste'
    template_name = 'envanter_takip/urunler.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        products = Product.objects.all()
        brands = Brand.objects.all()
        invoices = Invoice.objects.all()
        categories = Category.objects.all()
        context['urunler'] = products
        context['markalar'] = brands
        context['kategoriler'] = categories
        context['faturalar'] = invoices
        context['form'] = ProductForm(self.request.POST or None)

        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)

        if form.is_valid():
            product_code = form.cleaned_data.get('urun_kod')
            product_number = form.cleaned_data.get('urun_no')
            feature = form.cleaned_data.get('ozellik')
            brand = form.cleaned_data.get('marka')
            category = form.cleaned_data.get('kategori')
            invoice = form.cleaned_data.get('fatura')
            debit = form.cleaned_data.get('zimmet')
            product = Product(
                product_code=product_code,
                product_number=product_number,
                feature=feature,
                brand=brand,
                category=category,
                invoice=invoice,
                debit=debit
            )
            product.save()
        return redirect('urunler')


class CategoryListView(ListView):
    context_object_name = 'kategoriler'
    template_name = 'envanter_takip/kategoriler.html'

    def get_queryset(self):
        return Category.objects.all()

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)

        if form.is_valid():
            category_name = form.cleaned_data.get('isim')
            name = Category(name=category_name)
            name.save()
        return redirect('kategoriler')


class BrandListView(ListView):
    context_object_name = 'markalar'
    template_name = 'envanter_takip/markalar.html'

    def get_queryset(self):
        return Brand.objects.all()

    def post(self, request, *args, **kwargs):
        form = BrandForm(request.POST)

        if form.is_valid():
            brand_name = form.cleaned_data.get('isim')
            name = Brand(name=brand_name)
            name.save()
        return redirect('markalar')


class InvoiceListView(ListView):
    context_object_name = 'faturalar'
    template_name = 'envanter_takip/faturalar.html'

    def get_queryset(self):
        return Invoice.objects.all()

    def post(self, request, *args, **kwargs):
        form = InvoiceForm(request.POST)

        if form.is_valid():
            number = form.cleaned_data.get('numara')
            date = form.cleaned_data.get('tarih')
            invoice = Invoice(number=number, date=date)
            invoice.save()

        return redirect('faturalar')

