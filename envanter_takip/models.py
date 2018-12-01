from django.db import models


# Create your models here.
class Fatura(models.Model):
    numara = models.CharField(max_length=16)
    tarih = models.DateTimeField()

    def __str__(self):
        return str(self.numara)


class Kategori(models.Model):
    isim = models.CharField(max_length=255)

    def __str__(self):
        return str(self.isim)


class Marka(models.Model):
    isim = models.CharField(max_length=255)

    def __str__(self):
        return str(self.isim)


class Zimmet(models.Model):
    isim = models.CharField(max_length=255)
    teslim_tarihi = models.DateTimeField()

    def __str__(self):
        return str(self.isim)


class Urun(models.Model):
    urun_kod = models.CharField(max_length=5, default='URN')
    urun_no = models.PositiveIntegerField(default='1')
    ozellik = models.TextField()
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE,)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE,)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE,)
    zimmet = models.ForeignKey(Zimmet, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.urun_kod) + str(self.urun_no)
