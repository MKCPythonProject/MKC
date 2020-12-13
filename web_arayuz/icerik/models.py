from django.db import models

# Create your models here.
class kisiler(models.Model):
    kisi_id=models.AutoField (primary_key=True,verbose_name="Kişi No")
    adi_soyadi=models.TextField(verbose_name="Ad Soyad")
    tckimlik=models.BigIntegerField(unique=True,verbose_name="TC Kimlik")
    tel=models.IntegerField(verbose_name="Telefon")
    foto=models.TextField()
    kisi_tipi=models.IntegerField()

class Girisler(models.Model):
    giris_id = models.AutoField (primary_key=True,verbose_name="Giriş No")
    tarih = models.DateField(verbose_name="Tarih")
    saat= models.TimeField(verbose_name="Saat")
    kisi= models.ForeignKey(kisiler, on_delete=models.CASCADE)
    v_isi=models.FloatField(verbose_name="Vücut ısısı")

class Giris_iptal(models.Model):
    giris_iptal_id = models.AutoField (primary_key=True,verbose_name="Giriş No")
    tarih = models.DateField(verbose_name="Tarih")
    kisi= models.ForeignKey(kisiler, on_delete=models.CASCADE)
    v_isi=models.FloatField(verbose_name="Vücut ısısı")
