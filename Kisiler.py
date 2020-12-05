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
              sorgu = "INSERT INTO kisiler (adi_soyadi,tckimlik,tel,foto,kisi_tipi) VALUES(?,?,?,?,?)"
              veri = [self.adi_soyadi, self.tckimlik, self.tel, self.foto, self.kisi_tipi]
              baglanti.imlec.execute(sorgu, veri)
              baglanti.vt.commit()
              baglanti.vt.close()
        except sql.IntegrityError:
            kontrol="!!KAYIT BAŞARISIZ.Aynı Tel veya Tc Kimlik Numaralı Kişi Var."
        except AttributeError:
            kontrol="!!KAYIT BAŞARISIZ.Veritabanına Bağlanılamıyor."
        except:
            kontrol="!!KAYIT BAŞARISIZ.Bilinmeyen Hata."

        return kontrol
    
    @classmethod
    def kisi_bul(cls,tckimlik):
        baglanti=vt_baglan.Vt_Connection()
        sorgu="SELECT * FROM kisiler where tckimlik=?"
        veri=[tckimlik]
        baglanti.imlec.execute(sorgu, veri)
        kisibilgisi= baglanti.imlec.fetchone()
        baglanti.vt.close()
        return kisibilgisi

    def kisi_degistir(self):
        kontrol="Kayıt Değiştirildi"
        try:
              baglanti=vt_baglan.Vt_Connection()
              sorgu = "UPDATE kisiler SET adi_soyadi=?, tckimlik=?, tel=?, foto=?, kisi_tipi=? WHERE kisi_id=?"
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
        kontrol="Kayıt Silindi"
        try:
            baglanti=vt_baglan.Vt_Connection()
            sorgu="delete from kisiler where kisi_id=?"
            veri=[kisi_id]
            baglanti.imlec.execute(sorgu, veri)
            baglanti.vt.commit()
            baglanti.vt.close()
        except:
             kontrol="!!KAYIT SİLİNEMEDİ.Bilinmeyen Hata."
        return kontrol