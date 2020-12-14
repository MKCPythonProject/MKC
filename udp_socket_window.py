# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udp_socket_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
import vt_connection as vt_baglan
class Ui_Ud_psocket_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ud_psocket_window=self
        Ud_psocket_window.setObjectName("Ud_psocket_window")
        Ud_psocket_window.resize(408, 198)
        self.centralwidget = QtWidgets.QWidget(Ud_psocket_window)
        self.centralwidget.setObjectName("centralwidget")
        self.ip_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_txt.setGeometry(QtCore.QRect(130, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ip_txt.setFont(font)
        self.ip_txt.setObjectName("ip_txt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.port_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.port_txt.setGeometry(QtCore.QRect(130, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.port_txt.setFont(font)
        self.port_txt.setObjectName("port_txt")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 110, 71, 51))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        Ud_psocket_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ud_psocket_window)
        self.statusbar.setObjectName("statusbar")
        Ud_psocket_window.setStatusBar(self.statusbar)

        self.retranslateUi(Ud_psocket_window)
        QtCore.QMetaObject.connectSlotsByName(Ud_psocket_window)

    def retranslateUi(self, Ud_psocket_window):
        _translate = QtCore.QCoreApplication.translate
        Ud_psocket_window.setWindowTitle(_translate("Ud_psocket_window", "UDP SOCKET İLETİŞİM BİLGİLERİ"))
        self.label.setText(_translate("Ud_psocket_window", "IP Adresi:"))
        self.label_2.setText(_translate("Ud_psocket_window", "Port Numarası:"))
        self.pushButton.clicked.connect(self.kaydet)

    def kaydet(self):

        try:
            baglanti = vt_baglan.Vt_Connection()
            sorgu = "delete from udp_connect"
            baglanti.imlec.execute(sorgu)
            baglanti.vt.commit()
            sorgu = "INSERT INTO udp_connect (ipno,portno) VALUES(?,?)"
            veri = [self.ip_txt.text(),int(self.port_txt.text())]
            baglanti.imlec.execute(sorgu, veri)
            baglanti.vt.commit()
            baglanti.vt.close()
            QtWidgets.QMessageBox.about(self.centralwidget,"OK","KAYIT YAPILDI")
        except ValueError:
            QtWidgets.QMessageBox.about(self.centralwidget, "Uyarı", " port No Sayı olmalı ")
        except AttributeError:
            QtWidgets.QMessageBox.about(self.centralwidget,"Uyarı", "!!KAYIT BAŞARISIZ.Veritabanına Bağlanılamıyor.")
        except:
            QtWidgets.QMessageBox.about(self.centralwidget,"Uyarı", "!!KAYIT BAŞARISIZ.Bilinmeyen Hata.")




