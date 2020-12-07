# -*- coding: utf-8 -*-
import os
import sqlite3 as sql

class Vt_Connection():
    def __init__(self):
         veritabani = 'proje_mkc.sqlite'
         dosya_var_mi = os.path.exists(veritabani)
         if dosya_var_mi:
             self.vt = sql.connect(veritabani)
             self.imlec = self.vt.cursor()

