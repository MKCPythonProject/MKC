import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import socket#packet_tacer iletişim için
import threading#iş olulturmak için
import Giris_islemleri as giris_isleri
import datetime as zaman
import time
class Menu(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        Kapigiris_window = self
        Kapigiris_window.setObjectName("Kapigiris_window")
        Kapigiris_window.resize(507, 433)
        self.centralwidget = QtWidgets.QWidget(Kapigiris_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.adsoyadtxt = QtWidgets.QLabel(self.centralwidget)
        self.adsoyadtxt.setGeometry(QtCore.QRect(160, 90, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.adsoyadtxt.setFont(font)
        self.adsoyadtxt.setText("")
        self.adsoyadtxt.setObjectName("adsoyadtxt")
        self.foto_label = QtWidgets.QLabel(self.centralwidget)
        self.foto_label.setGeometry(QtCore.QRect(150, 120, 250, 251))
        self.foto_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.foto_label.setText("")
        self.foto_label.setObjectName("foto_label")
        self.vucutisi_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.vucutisi_lcd.setGeometry(QtCore.QRect(180, 20, 151, 61))
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
        self.label_2.setGeometry(QtCore.QRect(200, 380, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
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
        #designer sonrası eklenen
        self.t1 = threading.Thread(target=self.veri_oku)
        self.t1.start()
    
    def veri_oku(self):
        while True:
             UDP_IP ="192.168.1.29"
             UDP_PORT =1234
             sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
             sock.bind((UDP_IP,UDP_PORT))
             data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
             if data is not None: 
                 
                 #hareket sensörü ile bir ısı geldiğinde önce adam iptalmi bakalım
                 #önce burda yüz tanıma kodları olacak sonra iptalmi vt sorgusu
                 
                 sayi=giris_isleri.Giris_islemleri().giris_iptal_sorgula(1)
                
                 if sayi[0]==0:#karantinada değilse 14 gün geçmişse
                        data=str(data).lstrip("b'")
                        data=data.rstrip("'")
                        if float(data)>=37.5:
                            #vucut ısısı 37.5 üzerinde ise iptal alanı=1
                            self.vucutisi_lcd.setStyleSheet("color: rgb(255, 0, 0);")
                            yenigiris=giris_isleri.Giris_islemleri(float(data), 1) 
                            deger=yenigiris.giris_iptal_kaydet()
                            self.label_2.setText("Giriş İptal Kaydı Yapıldı")
                    
                        elif float(data)<37.5:#ısı uygunsa veritabanı girislere kaydet
                            self.vucutisi_lcd.setStyleSheet("color: rgb(4, 211, 53);")
                            yenigiris=giris_isleri.Giris_islemleri(float(data), 1) 
                            deger=yenigiris.giris_kaydet()
                            self.label_2.setText("Giriş Kaydı Yapıldı")
                        
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
                    sock.sendto(bytes(2),(UDP_IP,UDP_PORT))
        
 
    
  