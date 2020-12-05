# -*- coding: utf-8 -*-

import os
import sqlite3 as sql
import vt_connection as vt_baglan
import datetime 
class Raporlama():
    def __init__(self):
        pass
        
   
    @classmethod
    def Raporla(cls,kisi_tipi):
            baglanti=vt_baglan.Vt_Connection()
            kayitlar=None
            if kisi_tipi!=0:
                print("oldu")
                sorgu="SELECT tarih,saat,tel,v_isi,tel FROM kisiler,girisler where  kisiler.kisi_tipi=? and girisler.kisi_id=kisiler.kisi_id"
                veri=[kisi_tipi]
                kayitlar=baglanti.imlec.execute(sorgu,veri)
            else:
                sorgu="SELECT tarih,saat,adi_soyadi,v_isi,tel FROM girisler,kisiler where girisler.kisi_id=kisiler.kisi_id "    
                kayitlar=baglanti.imlec.execute(sorgu)
            
            return kayitlar