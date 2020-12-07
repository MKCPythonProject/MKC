# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tarih_giris_rapor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tarih_Giris_Rapor(object):
    def setupUi(self, Tarih_Giris_Rapor):
        Tarih_Giris_Rapor.setObjectName("Tarih_Giris_Rapor")
        Tarih_Giris_Rapor.resize(800, 612)
        Tarih_Giris_Rapor.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Tarih_Giris_Rapor)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(200, 40, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(450, 41, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 40, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 100, 521, 481))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 95 10pt \"MS Shell Dlg 2\";")
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.Personel_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Personel_radio.setGeometry(QtCore.QRect(150, 70, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Personel_radio.setFont(font)
        self.Personel_radio.setObjectName("Personel_radio")
        self.Misafir_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.Misafir_radio.setGeometry(QtCore.QRect(300, 70, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Misafir_radio.setFont(font)
        self.Misafir_radio.setObjectName("Misafir_radio")
        self.tum_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.tum_radio.setGeometry(QtCore.QRect(440, 70, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tum_radio.setFont(font)
        self.tum_radio.setObjectName("tum_radio")
        self.iptal_check = QtWidgets.QCheckBox(self.centralwidget)
        self.iptal_check.setGeometry(QtCore.QRect(270, 10, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.iptal_check.setFont(font)
        self.iptal_check.setStyleSheet("color: rgb(255, 0, 0);")
        self.iptal_check.setObjectName("iptal_check")
        Tarih_Giris_Rapor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tarih_Giris_Rapor)
        self.statusbar.setObjectName("statusbar")
        Tarih_Giris_Rapor.setStatusBar(self.statusbar)

        self.retranslateUi(Tarih_Giris_Rapor)
        QtCore.QMetaObject.connectSlotsByName(Tarih_Giris_Rapor)

    def retranslateUi(self, Tarih_Giris_Rapor):
        _translate = QtCore.QCoreApplication.translate
        Tarih_Giris_Rapor.setWindowTitle(_translate("Tarih_Giris_Rapor", "RAPOR EKRANI"))
        self.label.setText(_translate("Tarih_Giris_Rapor", "Başlangıç:"))
        self.label_2.setText(_translate("Tarih_Giris_Rapor", "Bitiş:"))
        self.Personel_radio.setText(_translate("Tarih_Giris_Rapor", "Personel"))
        self.Misafir_radio.setText(_translate("Tarih_Giris_Rapor", "Misafir"))
        self.tum_radio.setText(_translate("Tarih_Giris_Rapor", "Tümü"))
        self.iptal_check.setText(_translate("Tarih_Giris_Rapor", "GİRİŞİ İPTAL OLANLAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tarih_Giris_Rapor = QtWidgets.QMainWindow()
    ui = Ui_Tarih_Giris_Rapor()
    ui.setupUi(Tarih_Giris_Rapor)
    Tarih_Giris_Rapor.show()
    sys.exit(app.exec_())

