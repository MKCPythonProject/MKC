
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import GirislerForm
import datetime

# Create your views here.
def girisler_index(request, adi_soyadi=None):
    form = GirislerForm(request.POST or None)
    Giris_listesi=None
    if form.is_valid():
        tarih1= form.cleaned_data["tarih1"]
        tarih2=form.cleaned_data["tarih2"]
        print(tarih1)
        #start_date = datetime.date(2020,12,1)
        #end_date = datetime.date(2020,12,13)
        Giris_listesi=Girisler.objects.filter(tarih__lte=tarih2).filter(tarih__gte=tarih1)
    else:
         Giris_listesi=Girisler.objects.all()


    gidecekliste=[]#sayfaya gönderilecek bilgiler
    for giris in Giris_listesi :#önce girisler içinde dön
        Kisi_listesi=kisiler.objects.filter(kisi_id=giris.kisi_id)#giris yapan kisi bilgisini al
        adi_soyadi
        for kisi in Kisi_listesi:#kisinin adını soyadını bul
            adi_soyadi=kisi.adi_soyadi
        gidecekliste.append(#listeye ekle
            {
				'tarih': giris.tarih,
				'saat': giris.saat,
				'adi_soyadi': adi_soyadi,
				'v_isi': giris.v_isi,
                'kisi_id':giris.kisi_id
			})
    context = {
        'form': form,
         'giris_listesi': gidecekliste
    }

    return render(request, "index.html", context)#sayfaya gönder

def kisi_detay(request,id):
    kisi_bilgisi = kisiler.objects.filter(kisi_id=id)
    return render(request, "kisi_detay.html", {'kisi_listesi': kisi_bilgisi})

def girisler_iptal(request, adi_soyadi=None):
    form = GirislerForm(request.POST or None)
    Giris_listesi=None
    if form.is_valid():
        tarih1= form.cleaned_data["tarih1"]
        tarih2=form.cleaned_data["tarih2"]
        print(tarih1)

        Giris_listesi=Giris_iptal.objects.filter(tarih__lte=tarih2).filter(tarih__gte=tarih1)
    else:
         Giris_listesi=Giris_iptal.objects.all()


    gidecekliste=[]#sayfaya gönderilecek bilgiler
    for giris in Giris_listesi :#önce girisler içinde dön
        Kisi_listesi=kisiler.objects.filter(kisi_id=giris.kisi_id)#giris yapan kisi bilgisini al
        adi_soyadi
        for kisi in Kisi_listesi:#kisinin adını soyadını bul
            adi_soyadi=kisi.adi_soyadi
        gidecekliste.append(#listeye ekle
            {
				'tarih': giris.tarih,
				'adi_soyadi': adi_soyadi,
				'v_isi': giris.v_isi,
                'kisi_id':giris.kisi_id
			})
    context = {
        'form': form,
         'giris_iptal_listesi': gidecekliste
    }

    return render(request, "giris_iptal.html", context)#sayfaya gönder