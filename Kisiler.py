# -*- coding: utf-8 -*-
import os
import sqlite3 as sql
import vt_connection as vt_baglan
class Kisi():
    def __init__(self,adi_soyadi,tckimlik,tel,foto,kisi_tipi,kisi_id=None):
        self.kisi_id=kisi_id
        self.adi_soyadi=adi_soyadi
        self.tckimlik=tckimlik
        self.tel=tel
        self.foto=foto
        self.kisi_tipi=kisi_tipi
        
  
              
    def kisi_kaydet(self):
        kontrol="Kayıt Başarılı"

        try:
              baglanti=vt_baglan.Vt_Connection()
              sorgu = "INSERT INTO icerik_kisiler (adi_soyadi,tckimlik,tel,foto,kisi_tipi) VALUES(?,?,?,?,?)"
              veri = [self.adi_soyadi, self.tckimlik, self.tel, self.foto, self.kisi_tipi]
              baglanti.imlec.execute(sorgu, veri)
              baglanti.vt.commit()
              baglanti.vt.close()
        except sql.IntegrityError:
            kontrol="!!KAYIT BAŞARISIZ.Aynı Tel veya Tc Kimlik Numaralı Kişi Var."
        except AttributeError:
            kontrol="!!KAYIT BAŞARISIZ.Veritabanına Bağlanılamıyor."
        except:
            kontrol = "!!KAYIT BAŞARISIZ.Foto Çekimi Yapmalısınız veya Bilinmeyen hata."

        return kontrol
    
    @classmethod
    def kisi_bul(cls,tckimlik):
        baglanti=vt_baglan.Vt_Connection()
        sorgu="SELECT * FROM icerik_kisiler where tckimlik=?"
        veri=[tckimlik]
        baglanti.imlec.execute(sorgu, veri)
        kisibilgisi= baglanti.imlec.fetchone()
        baglanti.vt.close()
        return kisibilgisi

    @classmethod
    def kisi_ad_getir(cls,kisi_id):#fotolara eklemek için kişi adlarını
        try:
            baglanti=vt_baglan.Vt_Connection()
            sorgu="SELECT adi_soyadi FROM icerik_kisiler where kisi_id=?"
            veri=[kisi_id]
            baglanti.imlec.execute(sorgu, veri)
            kisibilgisi= baglanti.imlec.fetchone()
            baglanti.vt.close()
            return kisibilgisi[0]
        except TypeError:
            return "yok"

    def kisi_degistir(self):
        kontrol="Kayıt Değiştirildi"
        try:
              baglanti=vt_baglan.Vt_Connection()
              sorgu = "UPDATE icerik_kisiler SET adi_soyadi=?, tckimlik=?, tel=?, foto=?, kisi_tipi=? WHERE kisi_id=?"
              veri = [self.adi_soyadi, self.tckimlik, self.tel, self.foto, self.kisi_tipi,self.kisi_id]
              baglanti.imlec.execute(sorgu, veri)
              baglanti.vt.commit()
              baglanti.vt.close()
        except sql.IntegrityError:
            kontrol="!!KAYIT DEĞİŞTİRELEMEDİ.Aynı Tel veya Tc Kimlik Numaralı Kişi Var."
        except:
            kontrol="!!KAYIT DEĞİŞTİRELEMEDİ.Bilinmeyen Hata."

        return kontrol
    
    
    @classmethod
    def kisi_sil(cls,kisi_id):
        kontrol = "Kayıt Silindi"
        try:
            baglanti=vt_baglan.Vt_Connection()
            sorgu="delete from icerik_kisiler where kisi_id=?"
            veri=[kisi_id]
            baglanti.imlec.execute(sorgu, veri)
            baglanti.vt.commit()
            baglanti.vt.close()
            for i in range(1,10):
                os.remove("kisi_fotolar/" +str(kisi_id) +"."+str(i)+".jpg")
            os.remove("web_arayuz/static/vt_fotolar/"+str(kisi_id) +".9.jpg")
        except:
            kontrol="!!KAYIT SİLİNEMEDİ.Bilinmeyen Hata."
        return kontrol
    
        
    @classmethod
    def son_kisi_id(cls):
        baglanti=vt_baglan.Vt_Connection()
        sorgu="SELECT max(kisi_id) FROM icerik_kisiler"
        baglanti.imlec.execute(sorgu)
        sayi= baglanti.imlec.fetchone()
        baglanti.vt.close()
        return sayi