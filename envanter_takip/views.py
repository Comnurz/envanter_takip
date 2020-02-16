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
            product_code = form.cleaned_data.get('product_code')
            product_number = form.cleaned_data.get('product_number')
            feature = form.cleaned_data.get('feature')
            brand = form.cleaned_data.get('brand')
            category = form.cleaned_data.get('category')
            invoice = form.cleaned_data.get('invoice')
            debit = form.cleaned_data.get('debit')
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
            category_name = form.cleaned_data.get('name')
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
            brand_name = form.cleaned_data.get('name')
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
            number = form.cleaned_data.get('number')
            date = form.cleaned_data.get('date')
            invoice = Invoice(number=number, date=date)
            invoice.save()

        return redirect('faturalar')

