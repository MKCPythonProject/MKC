# -*- coding: utf-8 -*-
import os
import sqlite3 as sql
import vt_connection as vt_baglan
import datetime 
class Giris_islemleri():
    def __init__(self,vucut_isi=None,kisi_id=None):
        self.vucut_isi=vucut_isi
        self.kisi_id=kisi_id
        
    def giris_kaydet(self):
        kontrol="Kayıt Başarılı"
        try:
              baglanti=vt_baglan.Vt_Connection()
              sorgu = "INSERT INTO girisler (tarih,saat,v_isi,kisi_id) VALUES(?,?,?,?)"
              veri = [str(datetime.datetime.now().date()),str(datetime.datetime.now().time()), self.vucut_isi, self.kisi_id]
              baglanti.imlec.execute(sorgu, veri)
              baglanti.vt.commit()
              baglanti.vt.close()
        except AttributeError:
            kontrol="!!KAYIT BAŞARISIZ.Veritabanına Bağlanılamıyor."
        except:
            kontrol="!!KAYIT BAŞARISIZ.Bilinmeyen Hata."

        return kontrol
        
    def giris_iptal_kaydet(self):
        kontrol="Kayıt Başarılı"
        try:
              baglanti=vt_baglan.Vt_Connection()
              sorgu = "INSERT INTO giris_iptal (tarih,v_isi,kisi_id) VALUES(?,?,?)"
              veri = [str(datetime.datetime.now().date()), self.vucut_isi, self.kisi_id]
              baglanti.imlec.execute(sorgu, veri)
              baglanti.vt.commit()
              baglanti.vt.close()
        except AttributeError:
            kontrol="!!KAYIT BAŞARISIZ.Veritabanına Bağlanılamıyor."
        except:
            kontrol="!!KAYIT BAŞARISIZ.Bilinmeyen Hata."

        return kontrol
    
    @classmethod
    def giris_iptal_sorgula(cls,kisi_id):
        baglanti=vt_baglan.Vt_Connection()
        sorgu="SELECT count(*) from Giris_iptal where kisi_id=? and (strftime('%d','now')-strftime('%d',tarih))<=14"
        veri=[kisi_id]
        baglanti.imlec.execute(sorgu, veri)
        sayi= baglanti.imlec.fetchone()
        baglanti.vt.close()
        return sayi