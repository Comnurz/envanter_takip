from django.db import models


# Create your models here.
class Fatura(models.Model):
    numarasi = models.CharField(max_length=16)
    tarih = models.DateTimeField()


class Kategori(models.Model):
    isim = models.CharField(max_length=255)


class Marka(models.Model):
    isim = models.CharField(max_length=255)


class Zimmet(models.Model):
    isim = models.CharField(max_length=255)
    teslim_tarihi = models.DateTimeField()


class Urun(models.Model):
    adet = models.IntegerField()
    ozellik = models.TextField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE,)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE,)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE,)
    zimmet = models.ForeignKey(Zimmet, on_delete=models.CASCADE,)
