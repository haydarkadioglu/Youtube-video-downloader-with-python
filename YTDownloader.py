# this app developed by haydarkadioglu github account

import sys
import os
import wget
from PyQt5 import QtCore, QtGui, QtWidgets

import pytube as yt


class Ui_Widget(object):

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")

        Widget.resize(1100, 600)
        Widget.setMinimumSize(QtCore.QSize(600, 300))

        Widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Widget.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.textBrowser = QtWidgets.QTextBrowser(Widget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 100, 650, 180))

        self.textBrowser.setStyleSheet("blue")
        self.textBrowser.setObjectName("textBrowser")

        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 300, 650, 31))
        self.lineEdit.setProperty("NuLL", QtCore.QTime(-1, -1, -1))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Widget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 350, 650, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 410, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)

        self.videoButton = QtWidgets.QPushButton(Widget)
        self.videoButton.setGeometry(820, 300, 160, 35)

        self.audioButton = QtWidgets.QPushButton(Widget)
        self.audioButton.setGeometry(820, 350, 160, 35)

        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(10, 10, 700, 50)


        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.retranslateUi(Widget)
        self.design_ui(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

        self.videoButton.clicked.connect(self.videoBut)
        self.audioButton.clicked.connect(self.audioBut)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate

        Widget.setWindowTitle(_translate("Widget", "YTDownloader"))

        self.textBrowser.setHtml(_translate("Widget",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">İndirmek istediğiniz YouTube videosunun linkini giriniz...</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Widget", "Link giriniz..."))
        self.pushButton.setText(_translate("Widget", "NULL"))
        self.videoButton.setText(_translate("Widget", "Video"))
        self.audioButton.setText(_translate("Widget", "Müzik"))
        self.label.setText("this app developed by @haydarkadioglu github account")



    def design_ui(self, Widget):

        try:
            os.mkdir("Downloaded Files")
        except:
            pass

        try:
            with open("Downloaded Files/icon.png") as ic:
                pass
        except:
            url = "https://cdn-icons-png.flaticon.com/512/7592/7592560.png"
            wget.download(url, "Downloaded Files/icon.png")

        Widget.setWindowIcon(QtGui.QIcon("Downloaded Files/icon.png"))

        Widget.setStyleSheet(
            "#Widget{background-color: qlineargradient(spread:pad, x2:4, y1:0, x2:1, y2:0, stop:0 rgba(90, 33, 56, 205), stop:1 rgba(25, 143, 211, 255));}")

    def videoBut(self):

        url = self.lineEdit.text()
        try:

            down = yt.YouTube(url)

            self.textBrowser.setText(f"Video ile ilgili bilgiler...\nBaşlık: {down.title}\nKanal: {down.author}\n{down.thumbnail_url}\nVideo olarak indirilecektir...")
            self.down1 = down.streams.filter(progressive=True, file_extension="mp4", type="video")

            i = 1
            self.comboBox_2.clear()
            self.comboBox_2.addItem("Seçiniz...")
            for a, an in enumerate(self.down1):
                self.comboBox_2.addItem(f"{i} -- {an}")
                i += 1

        except Exception as asd:
            self.textBrowser.setText(f"hatalı giriş yaptınız... {asd}")

        self.pushButton.setText("İNDİR")
        self.pushButton.clicked.connect(self.download)

    def audioBut(self):


        url = self.lineEdit.text()
        try:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("Seçiniz...")


            self.down = yt.YouTube(url)

            self.textBrowser.setText(f"Video ile ilgili bilgiler...\nBaşlık: {self.down.title}\nKanal: {self.down.author}\nmp3 olarak indirilecektir...")
            self.down2 = self.down.streams.filter(progressive=False, file_extension="mp4", type="audio")

            i = 1
            for a, an in enumerate(self.down2):
                self.comboBox_2.addItem(f"{i} -- {an}")
                i += 1
        except Exception as ads:
            self.textBrowser.setText(f"Geçersiz ling girdiniz... {ads}")

        self.pushButton.setText("İNDİR")

        self.pushButton.clicked.connect(self.cevirici)

    def download(self):

        cho = self.comboBox_2.currentIndex()

        self.down1[cho - 1].download("Downloaded Files/Video")

        self.textBrowser.append("İNDİRME TAMAMLANDI")

    def cevirici(self):

        cho = self.comboBox_2.currentIndex()

        self.down2[cho - 1].download("Downloaded Files/Music")
        self.oldna = self.down.title + ".mp4"
        self.newna = self.down.title + ".mp3"

        self.textBrowser.append("İNDİRME TAMAMLANDI")

        try:
            os.rename(f"Downloaded Files/Music/{self.oldna}", f"Downloaded Files/Music/{self.newna}")
        except Exception as erro:
            self.textBrowser.append(f"{erro}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Widget()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
