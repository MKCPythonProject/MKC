import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import socket#packet_tacer iletişim için
import threading#iş olulturmak için
import Giris_islemleri as giris_isleri
import datetime as zaman
import time
import random 

class Ui_kapigiris(QtWidgets.QMainWindow):
    kisi_id=0
    def __init__(self):
        super().__init__()
        Kapigiris_window = self
        Kapigiris_window.setObjectName("Kapigiris_window")
        Kapigiris_window.resize(581, 483)
        self.centralwidget = QtWidgets.QWidget(Kapigiris_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.adsoyadtxt = QtWidgets.QLabel(self.centralwidget)
        self.adsoyadtxt.setGeometry(QtCore.QRect(160, 120, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.adsoyadtxt.setFont(font)
        self.adsoyadtxt.setText("")
        self.adsoyadtxt.setObjectName("adsoyadtxt")
        self.foto_label = QtWidgets.QLabel(self.centralwidget)
        self.foto_label.setGeometry(QtCore.QRect(150, 170, 250, 251))
        self.foto_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.foto_label.setText("")
        self.foto_label.setObjectName("foto_label")
        self.vucutisi_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.vucutisi_lcd.setGeometry(QtCore.QRect(210, 60, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.vucutisi_lcd.setFont(font)
        self.vucutisi_lcd.setStyleSheet("border-color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 255);")
        self.vucutisi_lcd.setSmallDecimalPoint(False)
        self.vucutisi_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.vucutisi_lcd.setProperty("value", 0.0)
        self.vucutisi_lcd.setProperty("intValue", 0)
        self.vucutisi_lcd.setObjectName("vucutisi_lcd")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 430, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.giris_sayisi_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.giris_sayisi_lcd.setGeometry(QtCore.QRect(530, 10, 51, 31))
        self.giris_sayisi_lcd.setStyleSheet("color: rgb(255, 85, 0);")
        self.giris_sayisi_lcd.setLineWidth(0)
        self.giris_sayisi_lcd.setSmallDecimalPoint(False)
        self.giris_sayisi_lcd.setDigitCount(3)
        self.giris_sayisi_lcd.setObjectName("giris_sayisi_lcd")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 0, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("uses.png"))
        self.label_3.setObjectName("label_3")
        Kapigiris_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Kapigiris_window)
        self.statusbar.setObjectName("statusbar")
        Kapigiris_window.setStatusBar(self.statusbar)

        self.retranslateUi(Kapigiris_window)
        QtCore.QMetaObject.connectSlotsByName(Kapigiris_window)

    def retranslateUi(self, Kapigiris_window):
        _translate = QtCore.QCoreApplication.translate
        Kapigiris_window.setWindowTitle(_translate("Kapigiris_window", "Kapı Giriş"))
        self.label.setText(_translate("Kapigiris_window", "Ad Soyad:"))
        self.label_3.setToolTip(_translate("Kapigiris_window", "Bugün Giriş Yapan Kişi Sayısı"))

       
        
       #designer sonrası eklenen
        giris_sayi=giris_isleri.Giris_islemleri().giris_yapan_kisi_sayisi()
        self.giris_sayisi_lcd.display(giris_sayi[0])
        self.t1 = threading.Thread(target=self.veri_oku)
        self.t1.start()
        
    def veri_oku(self):
        while True:
             self.UDP_IP ="192.168.1.29"
             self.UDP_PORT =1234
             self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
             self.sock.bind((self.UDP_IP,self.UDP_PORT))
             data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
             if data is not None: 
                 print(data)
                 #hareket sensörü ile bir ısı geldiğinde önce adam iptalmi bakalım
                 #önce burda yüz tanıma kodları olacak sonra iptalmi vt sorgusu
               
                 
                 #test aşamalı kodlar
                 listem=[39]
                 value=random.choice(listem)
                 self.kisi_id=value
                 foto="kisi_fotolar/"+str(value)+".jpg"
                 pixmap = QtGui.QPixmap(foto)
                 pixmap_resized=pixmap.scaled(250, 250, QtCore.Qt.IgnoreAspectRatio)
                 self.foto_label.setPixmap(pixmap_resized)
                 self.adsoyadtxt.setText("Tuncay SALI")
            
          
                 sayi=giris_isleri.Giris_islemleri().giris_iptal_sorgula(self.kisi_id)
                 
                 if sayi[0]==0:#karantinada değilse 14 gün geçmişse
                        data=str(data).lstrip("b'")
                        data=data.rstrip("'")
                        if float(data)>=37.5:
                            #vucut ısısı 37.5 üzerinde ise iptal alanı=1
                            
                            self.vucutisi_lcd.setStyleSheet("color: rgb(255, 0, 0);")
                            yenigiris=giris_isleri.Giris_islemleri(float(data), self.kisi_id) 
                            deger=yenigiris.giris_iptal_kaydet()
                            self.label_2.setText("Giriş İptal Kaydı Yapıldı")

                        elif float(data)<37.5:#ısı uygunsa veritabanı girislere kaydet
                            self.vucutisi_lcd.setStyleSheet("color: rgb(4, 211, 53);")
                            yenigiris=giris_isleri.Giris_islemleri(float(data), self.kisi_id) 
                            deger=yenigiris.giris_kaydet()
                            self.label_2.setText("Giriş Kaydı Yapıldı")
                            giris_sayi=giris_isleri.Giris_islemleri().giris_yapan_kisi_sayisi()
                            self.giris_sayisi_lcd.display(giris_sayi[0])
                            print(deger)
                        else:
                            self.vucutisi_lcd.setStyleSheet("color: rgb(0, 0, 255);")
                        
                        self.vucutisi_lcd.display(data)
                        data=None
                        time.sleep(1)
                        self.label_2.clear()
                 else:
                    self.vucutisi_lcd.display(0)
                    self.label_2.setText("14 gün Geçmediği için Giriş Yapılamaz") 
                    self.sock.sendto(bytes(2),(self.UDP_IP,self.UDP_PORT))
             
    def closeEvent(self,event):#soketi kapatıyoz
       self.sock.close()
      

        