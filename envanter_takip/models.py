from django.db import models

from django.contrib.auth.models import User


class Invoice(models.Model):
    number = models.CharField(max_length=16)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.numara)


class Category(models.Model):
    category_code = models.CharField(max_length=7, default='URN', verbose_name='Kategori Kodu')
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.isim)


class Brand(models.Model):
    brand_code = models.CharField(max_length=7, default='URN', verbose_name='Marka Kodu')
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.isim)


class Debit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return str(self.isim)


class Product(models.Model):
    product_code = models.CharField(max_length=15, default='URN', verbose_name='Ürün Kodu')
    product_number = models.PositiveIntegerField(default='1', verbose_name='Ürün No')
    feature = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,)
    debit = models.ForeignKey(Debit, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.urun_kod) + str(self.urun_no)
