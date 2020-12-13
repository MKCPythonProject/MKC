# -*- coding: utf-8 -*-
import os
import sqlite3 as sql
import vt_connection as vt_baglan
import datetime 
class Raporlama():
    def __init__(self):
        pass
        
   
    @classmethod
    def Raporla(cls,kisi_tipi,tarih1=None,tarih2=None):
            baglanti=vt_baglan.Vt_Connection()
            kayitlar=None
            if kisi_tipi!=0:
                sorgu="SELECT tarih,saat,adi_soyadi,v_isi,tel FROM icerik_kisiler,icerik_girisler where  icerik_kisiler.kisi_tipi=? and icerik_girisler.kisi_id=icerik_kisiler.kisi_id and tarih between ? and ?"
                veri=[kisi_tipi,tarih1,tarih2]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            else:
                sorgu="SELECT tarih,saat,adi_soyadi,v_isi,tel FROM icerik_girisler,icerik_kisiler where icerik_girisler.kisi_id=icerik_kisiler.kisi_id and tarih between ? and ?"
                veri=[str(tarih1),str(tarih2)]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            
            return kayitlar
        
    @classmethod
    def iptal_Raporla(cls,kisi_tipi):
            baglanti=vt_baglan.Vt_Connection()
            kayitlar=None
            if kisi_tipi!=0:
                sorgu="SELECT tarih,adi_soyadi,v_isi,tel FROM icerik_kisiler,icerik_giris_iptal where  icerik_kisiler.kisi_tipi=? and icerik_giris_iptal.kisi_id=icerik_kisiler.kisi_id and (strftime('%d','now')-strftime('%d',tarih))<=14"
                veri=[kisi_tipi]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            else:
                sorgu="SELECT tarih,adi_soyadi,v_isi,tel FROM icerik_giris_iptal,icerik_kisiler where icerik_giris_iptal.kisi_id=icerik_kisiler.kisi_id and (strftime('%d','now')-strftime('%d',tarih))<=14"
                kayitlar=baglanti.imlec.execute(sorgu)
            
            return kayitlar
    
