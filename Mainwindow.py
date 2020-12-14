# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import Kisiler as kisi# kişiler sınıfı içeri alındı
import Kapi_giris_window as kapi_giris_window#kapi giris modulü
import Tarih_giris_rapor_window as Tarih_giris_window
import udp_socket_window as Udp_socket_window
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import foto_ogrenme as foto_ogren
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(76, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.adsoyadtxt = QtWidgets.QLineEdit(self.centralwidget)
        self.adsoyadtxt.setGeometry(QtCore.QRect(170, 30, 291, 20))
        self.adsoyadtxt.setObjectName("adsoyadtxt")
        self.TC = QtWidgets.QLabel(self.centralwidget)
        self.TC.setGeometry(QtCore.QRect(76, 80, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.TC.setFont(font)
        self.TC.setObjectName("TC")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.perradio = QtWidgets.QRadioButton(self.centralwidget)
        self.perradio.setGeometry(QtCore.QRect(170, 180, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.perradio.setFont(font)
        self.perradio.setCheckable(True)
        self.perradio.setChecked(True)
        self.perradio.setObjectName("perradio")
        self.misafirradio = QtWidgets.QRadioButton(self.centralwidget)
        self.misafirradio.setGeometry(QtCore.QRect(340, 180, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.misafirradio.setFont(font)
        self.misafirradio.setObjectName("misafirradio")
        self.tckimliktxt = QtWidgets.QLineEdit(self.centralwidget)
        self.tckimliktxt.setGeometry(QtCore.QRect(170, 80, 221, 20))
        self.tckimliktxt.setObjectName("tckimliktxt")
        self.teltxt = QtWidgets.QLineEdit(self.centralwidget)
        self.teltxt.setGeometry(QtCore.QRect(170, 130, 221, 20))
        self.teltxt.setObjectName("teltxt")
        self.btn_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kaydet.setGeometry(QtCore.QRect(40, 260, 51, 51))
        self.btn_kaydet.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_kaydet.setIcon(icon)
        self.btn_kaydet.setIconSize(QtCore.QSize(48, 48))
        self.btn_kaydet.setDefault(False)
        self.btn_kaydet.setFlat(False)
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_ara = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ara.setGeometry(QtCore.QRect(170, 260, 51, 51))
        self.btn_ara.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("binoculars.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ara.setIcon(icon1)
        self.btn_ara.setIconSize(QtCore.QSize(48, 48))
        self.btn_ara.setDefault(False)
        self.btn_ara.setFlat(False)
        self.btn_ara.setObjectName("btn_ara")
        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(290, 260, 51, 51))
        self.btn_sil.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("fulltrash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sil.setIcon(icon2)
        self.btn_sil.setIconSize(QtCore.QSize(48, 48))
        self.btn_sil.setDefault(False)
        self.btn_sil.setFlat(False)
        self.btn_sil.setObjectName("btn_sil")
        self.btn_fotocek = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fotocek.setGeometry(QtCore.QRect(630, 260, 51, 51))
        self.btn_fotocek.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fotocek.setIcon(icon3)
        self.btn_fotocek.setIconSize(QtCore.QSize(48, 48))
        self.btn_fotocek.setDefault(False)
        self.btn_fotocek.setFlat(False)
        self.btn_fotocek.setObjectName("btn_fotocek")
        self.kisi_id_label = QtWidgets.QLabel(self.centralwidget)
        self.kisi_id_label.setEnabled(True)
        self.kisi_id_label.setGeometry(QtCore.QRect(0, 320, 47, 13))
        self.kisi_id_label.setText("")
        self.kisi_id_label.setObjectName("kisi_id_label")
        self.btn_temizle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_temizle.setGeometry(QtCore.QRect(400, 260, 51, 51))
        self.btn_temizle.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_temizle.setIcon(icon4)
        self.btn_temizle.setIconSize(QtCore.QSize(48, 48))
        self.btn_temizle.setDefault(False)
        self.btn_temizle.setFlat(False)
        self.btn_temizle.setObjectName("btn_temizle")
        self.foto_label = QtWidgets.QLabel(self.centralwidget)
        self.foto_label.setGeometry(QtCore.QRect(530, 10, 250, 250))
        self.foto_label.setAutoFillBackground(False)
        self.foto_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.foto_label.setText("")
        self.foto_label.setObjectName("foto_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuGiri = QtWidgets.QMenu(self.menubar)
        self.menuGiri.setObjectName("menuGiri")
        self.menuRaporlama = QtWidgets.QMenu(self.menubar)
        self.menuRaporlama.setObjectName("menuRaporlama")
        self.menuUDP_Socket_Ayarlar = QtWidgets.QMenu(self.menubar)
        self.menuUDP_Socket_Ayarlar.setObjectName("menuUDP_Socket_Ayarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKisi_Kayit_Duzenle = QtWidgets.QAction(MainWindow)
        self.actionKisi_Kayit_Duzenle.setObjectName("actionKisi_Kayit_Duzenle")
        self.actionKapi_Giris = QtWidgets.QAction(MainWindow)
        self.actionKapi_Giris.setObjectName("actionKapi_Giris")
        self.actionTarih_raporla = QtWidgets.QAction(MainWindow)
        self.actionTarih_raporla.setObjectName("actionTarih_raporla")
        self.actionGiris_iptal_raporla = QtWidgets.QAction(MainWindow)
        self.actionGiris_iptal_raporla.setObjectName("actionGiris_iptal_raporla")
        self.actionIp_Port_degistir = QtWidgets.QAction(MainWindow)
        self.actionIp_Port_degistir.setObjectName("actionIp_Port_degistir")
        self.menuGiri.addAction(self.actionKisi_Kayit_Duzenle)
        self.menuGiri.addAction(self.actionKapi_Giris)
        self.menuRaporlama.addAction(self.actionTarih_raporla)
        self.menuUDP_Socket_Ayarlar.addAction(self.actionIp_Port_degistir)
        self.menubar.addAction(self.menuGiri.menuAction())
        self.menubar.addAction(self.menuRaporlama.menuAction())
        self.menubar.addAction(self.menuUDP_Socket_Ayarlar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personel & Misafir Kayıt Ekranı"))
        self.label.setText(_translate("MainWindow", "ADI SOYADI:"))
        self.TC.setText(_translate("MainWindow", "TC KİMLİK:"))
        self.label_3.setText(_translate("MainWindow", "TELEFON:"))
        self.perradio.setText(_translate("MainWindow", "PERSONEL"))
        self.misafirradio.setText(_translate("MainWindow", "MİSAFİR"))
        self.btn_kaydet.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Kaydet</span></p></body></html>"))
        self.btn_kaydet.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.btn_ara.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Tc Kimlik Ara</span></p></body></html>"))
        self.btn_ara.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.btn_sil.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Sil</span></p></body></html>"))
        self.btn_sil.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.btn_fotocek.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Fotograf Çek</span></p></body></html>"))
        self.btn_fotocek.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.btn_temizle.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Temizle</span></p></body></html>"))
        self.btn_temizle.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuGiri.setTitle(_translate("MainWindow", "Giriş"))
        self.menuRaporlama.setTitle(_translate("MainWindow", "Raporlama"))
        self.menuUDP_Socket_Ayarlar.setTitle(_translate("MainWindow", "UDP Socket Ayarları"))
        self.actionKisi_Kayit_Duzenle.setText(_translate("MainWindow", "Kişi Kayıt_Düzenle"))
        self.actionKapi_Giris.setText(_translate("MainWindow", "Kapı Giriş"))
        self.actionTarih_raporla.setText(_translate("MainWindow", "Giriş Raporları"))
        self.actionGiris_iptal_raporla.setText(_translate("MainWindow", "Girişi İptal Olanlar"))
        self.actionIp_Port_degistir.setText(_translate("MainWindow", "Ip_Port Değiştir"))



#designer sonrası benim kodlar burdan başlıyor
        self.btn_kaydet.clicked.connect(self.kayit_islemi)#kaydet buton tıklandı
        self.btn_ara.clicked.connect(self.kayit_ara)
        self.btn_temizle.clicked.connect(self.temizle)
        self.btn_sil.clicked.connect(self.kayit_sil)
        self.kisi_id_label.hide()
        self.kapi_giris_pencere=kapi_giris_window.Ui_kapigiris()
        self.Tarih_giris_rapor_pencere=Tarih_giris_window.Ui_Tarih_Giris_Rapor()
        self.actionKapi_Giris.triggered.connect(self.kapi_giris_ac)
        self.actionTarih_raporla.triggered.connect(self.tarih_raporla_ac)
        self.btn_fotocek.clicked.connect(self.foto_cek)
        self.udp_socket_pencere= Udp_socket_window.Ui_Ud_psocket_window()
        self.actionIp_Port_degistir.triggered.connect(self.udp_ayar_ac)
  

    
    def foto_cek(self):
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)# Video çekmeye başla
        detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        son_kisi_id=kisi.Kisi.son_kisi_id()#foto ismi için aldım
        if self.kisi_id_label.text() == "":  # yeni kayıtmı
            f=son_kisi_id[0]+1#1 ekleriz
        else:
            f=self.kisi_id_label.text()#değiştirme ise foto ismi korunur
        sampleNum=0
        while(True):#çekmeye başla
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                sampleNum=sampleNum+1
                self.foto_adi="kisi_fotolar/"+ str(f) +'.'+ str(sampleNum) +".jpg"
                cv2.imwrite(self.foto_adi, gray[y:y+h,x:x+w])
                cv2.imshow('YUZ TARAMA VT KAYIT',img)


            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum>10:#10 farklı açı
                break
        #renkli foto kaydı son foto
        ret, img = cam.read()

        self.vt_foto_adi = str(f) + '.' + str(sampleNum) + ".jpg"  # veritabanına yeni kayıt ismi

        #cv2.imwrite("vt_fotolar/"+self.vt_foto_adi, img)
        cv2.imwrite("web_arayuz/static/vt_fotolar/" + self.vt_foto_adi, img)
        cam.release()
        cv2.destroyAllWindows()
        nesne=foto_ogren.foto_ogrenme()#fotoları öğrenmeye gönder
        #labela foto yerleştir
        pixmap = QtGui.QPixmap("web_arayuz/static/vt_fotolar/"+ self.vt_foto_adi)
        pixmap_resized=pixmap.scaled(250, 250, QtCore.Qt.IgnoreAspectRatio)
        self.foto_label.setPixmap(pixmap_resized)
        

     
        
        
        
        
       
        

        
    def kapi_giris_ac(self):
        self.kapi_giris_pencere.show()
        
    def tarih_raporla_ac(self):
        self.Tarih_giris_rapor_pencere.show()

    def udp_ayar_ac(self):
        self.udp_socket_pencere.show()
    
        
    def kayit_islemi(self):
        try:
            tip=0
            if self.perradio.isChecked()==True:
                tip=1
            else:
                tip=2
            if self.kisi_id_label.text()=="":   #kaydetme
                yenikisi=kisi.Kisi(self.adsoyadtxt.text(),
                int(self.tckimliktxt.text()),int(self.teltxt.text()),  self.vt_foto_adi, tip)
                deger=yenikisi.kisi_kaydet()
                QtWidgets.QMessageBox.about(self.centralwidget, "Bursa_MKC", deger)
                if deger=="Kayıt Başarılı":  self.temizle()
            else:#kayıt değitirme
                yenikisi=kisi.Kisi(self.adsoyadtxt.text(),
                int(self.tckimliktxt.text()),int(self.teltxt.text()), self.vt_foto_adi, tip,int(self.kisi_id_label.text()))
                deger=yenikisi.kisi_degistir()
                QtWidgets.QMessageBox.about(self.centralwidget, "Bursa_MKC", deger)
                if deger=="Kayıt Değiştirildi":  self.temizle()     
        except ValueError:
             QtWidgets.QMessageBox.about(  self.centralwidget, "Uyarı", "Telefon ve Tc Kimlik Sayı Olmalı")
   
    def kayit_ara(self):
      try:
        gelenkisi=kisi.Kisi.kisi_bul(int(self.tckimliktxt.text()))
        self.adsoyadtxt.setText(gelenkisi[1])
        self.tckimliktxt.setText(str(gelenkisi[2]))
        self.teltxt.setText(str(gelenkisi[3]))
        self.kisi_id_label.setText(str(gelenkisi[0]))
        self.vt_foto_adi=gelenkisi[4]
        pixmap = QtGui.QPixmap("web_arayuz/static/vt_fotolar/" + gelenkisi[4])
        pixmap_resized = pixmap.scaled(250, 250, QtCore.Qt.IgnoreAspectRatio)
        self.foto_label.setPixmap(pixmap_resized)
        if gelenkisi[5]==1: 
            self.perradio.setChecked(True)
        else:
            self.misafirradio.setChecked(True)
      except TypeError:
          QtWidgets.QMessageBox.about(  self.centralwidget, "Uyarı", "Aradığınız Kişi Yok")
      except ValueError:
          QtWidgets.QMessageBox.about(  self.centralwidget, "Uyarı", "Arama Yapmak için Tc Kimlik Giriniz")
          
           
            
 
            
          
            
    def temizle(self):
        self.adsoyadtxt.clear()
        self.tckimliktxt.clear()
        self.teltxt.clear()
        self.perradio.setChecked(True)
        self.kisi_id_label.clear()
        self.foto_label.clear()


   
    def kayit_sil(self):
     try:
        deger=kisi.Kisi.kisi_sil(int(self.kisi_id_label.text()))
        QtWidgets.QMessageBox.about(self.centralwidget, "Bursa_MKC", deger)
     except ValueError:
          QtWidgets.QMessageBox.about(self.centralwidget, "Uyarı", "Silmek için Öcelikle Tc Numarası ile kayıdı arayınız")
     except:
          QtWidgets.QMessageBox.about(self.centralwidget, "Uyarı", "Bilinmeyen Hata")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

