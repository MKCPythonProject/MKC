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
                sorgu="SELECT tarih,saat,adi_soyadi,v_isi,tel FROM kisiler,girisler where  kisiler.kisi_tipi=? and girisler.kisi_id=kisiler.kisi_id and tarih between ? and ?"
                veri=[kisi_tipi,tarih1,tarih2]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            else:
                sorgu="SELECT tarih,saat,adi_soyadi,v_isi,tel FROM girisler,kisiler where girisler.kisi_id=kisiler.kisi_id and tarih between ? and ?"    
                veri=[str(tarih1),str(tarih2)]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            
            return kayitlar
        
    @classmethod
    def iptal_Raporla(cls,kisi_tipi):
            baglanti=vt_baglan.Vt_Connection()
            kayitlar=None
            if kisi_tipi!=0:
                sorgu="SELECT tarih,adi_soyadi,v_isi,tel FROM kisiler,giris_iptal where  kisiler.kisi_tipi=? and giris_iptal.kisi_id=kisiler.kisi_id and (strftime('%d','now')-strftime('%d',tarih))<=14"
                veri=[kisi_tipi]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            else:
                sorgu="SELECT tarih,adi_soyadi,v_isi,tel FROM giris_iptal,kisiler where giris_iptal.kisi_id=kisiler.kisi_id and (strftime('%d','now')-strftime('%d',tarih))<=14"    
                kayitlar=baglanti.imlec.execute(sorgu)
            
            return kayitlar
    