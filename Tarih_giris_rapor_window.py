# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tarih_giris_rapor_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sqlite3 as sql
import Raporlama as raporlama
class Ui_Tarih_Giris_Rapor(object):
    def setupUi(self, Tarih_Giris_Rapor):
        Tarih_Giris_Rapor.setObjectName("Tarih_Giris_Rapor")
        Tarih_Giris_Rapor.resize(800, 612)
        self.centralwidget = QtWidgets.QWidget(Tarih_Giris_Rapor)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(170, 20, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(420, 20, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 80, 521, 481))
        self.tableWidget.setStyleSheet("color: rgb(0, 85, 255);")
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 570, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.Personel_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Personel_radio.setGeometry(QtCore.QRect(160, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Personel_radio.setFont(font)
        self.Personel_radio.setObjectName("Personel_radio")
        self.Misafir_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Misafir_radio.setGeometry(QtCore.QRect(310, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Misafir_radio.setFont(font)
        self.Misafir_radio.setObjectName("Misafir_radio")
        self.tum_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.tum_radio.setGeometry(QtCore.QRect(450, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tum_radio.setFont(font)
        self.tum_radio.setObjectName("tum_radio")
        Tarih_Giris_Rapor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tarih_Giris_Rapor)
        self.statusbar.setObjectName("statusbar")
        Tarih_Giris_Rapor.setStatusBar(self.statusbar)

        self.retranslateUi(Tarih_Giris_Rapor)
        QtCore.QMetaObject.connectSlotsByName(Tarih_Giris_Rapor)

    def retranslateUi(self, Tarih_Giris_Rapor):
        _translate = QtCore.QCoreApplication.translate
        Tarih_Giris_Rapor.setWindowTitle(_translate("Tarih_Giris_Rapor", "MainWindow"))
        self.label.setText(_translate("Tarih_Giris_Rapor", "Başlangıç:"))
        self.label_2.setText(_translate("Tarih_Giris_Rapor", "Bitiş:"))
        self.pushButton.setText(_translate("Tarih_Giris_Rapor", "PushButton"))
        self.Personel_radio.setText(_translate("Tarih_Giris_Rapor", "Personel"))
        self.Misafir_radio.setText(_translate("Tarih_Giris_Rapor", "Misafir"))
        self.tum_radio.setText(_translate("Tarih_Giris_Rapor", "Tümü"))
        #bursan sonrası benden
        self.pushButton.clicked.connect(self.yazdir)
        self.Personel_radio.clicked.connect(self.yazdir_personel)
        self.Misafir_radio.clicked.connect(self.yazdir_mis)
        self.tum_radio.clicked.connect(self.yazdir)
    
    
    def yazdir_personel(self):
          
            kayitlar=raporlama.Raporlama().Raporla(1)
            self.tableWidget.setRowCount(0)
           
            for satir_no,satir_veri in enumerate(kayitlar):
                self.tableWidget.insertRow(satir_no)#belirtilen satirnodan sonra bir satir ekler
                for sutun_no,veri in enumerate(satir_veri):
                    self.tableWidget.setItem(satir_no, sutun_no, QtWidgets.QTableWidgetItem(str(veri)))
           
            baslik=["TARİH","SAAT","AD SOYAD","ISI DEĞERİ","TELEFON"]
            self.tableWidget.setHorizontalHeaderLabels(baslik)
 
    def yazdir_mis(self):
          
            kayitlar=raporlama.Raporlama().Raporla(2)
            self.tableWidget.setRowCount(0)
           
            for satir_no,satir_veri in enumerate(kayitlar):
                self.tableWidget.insertRow(satir_no)#belirtilen satirnodan sonra bir satir ekler
                for sutun_no,veri in enumerate(satir_veri):
                    self.tableWidget.setItem(satir_no, sutun_no, QtWidgets.QTableWidgetItem(str(veri)))
           
            baslik=["TARİH","SAAT","AD SOYAD","ISI DEĞERİ","TELEFON"]
            self.tableWidget.setHorizontalHeaderLabels(baslik)
    
    
         
            
    def yazdir(self):
            kayitlar=raporlama.Raporlama().Raporla(0)
           
            self.tableWidget.setRowCount(0)
           
            for satir_no,satir_veri in enumerate(kayitlar):
                self.tableWidget.insertRow(satir_no)#belirtilen satirnodan sonra bir satir ekler
                for sutun_no,veri in enumerate(satir_veri):
                    self.tableWidget.setItem(satir_no, sutun_no, QtWidgets.QTableWidgetItem(str(veri)))
           
            baslik=["TARİH","SAAT","AD SOYAD","ISI DEĞERİ","TELEFON"]
            self.tableWidget.setHorizontalHeaderLabels(baslik)
       

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tarih_Giris_Rapor = QtWidgets.QMainWindow()
    ui = Ui_Tarih_Giris_Rapor()
    ui.setupUi(Tarih_Giris_Rapor)
    Tarih_Giris_Rapor.show()
    sys.exit(app.exec_())

