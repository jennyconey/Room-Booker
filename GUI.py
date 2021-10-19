# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchAvail = QtWidgets.QGroupBox(self.centralwidget)
        self.searchAvail.setGeometry(QtCore.QRect(60, 289, 131, 91))
        self.searchAvail.setObjectName("searchAvail")
        self.availPeriod = QtWidgets.QComboBox(self.searchAvail)
        self.availPeriod.setGeometry(QtCore.QRect(10, 20, 111, 26))
        self.availPeriod.setEditable(True)
        self.availPeriod.setObjectName("availPeriod")
        self.availPeriod.addItem("")
        self.availPeriod.addItem("")
        self.availPeriod.addItem("")
        self.availPeriod.addItem("")
        self.availPeriod.addItem("")
        self.availPeriod.addItem("")
        self.availPeriod.addItem("")
        self.availDate = QtWidgets.QDateEdit(self.searchAvail)
        self.availDate.setGeometry(QtCore.QRect(10, 50, 110, 24))
        self.availDate.setCalendarPopup(True)
        self.availDate.setDate(QtCore.QDate(2019, 9, 10))
        self.availDate.setObjectName("availDate")
        self.searchSpec = QtWidgets.QGroupBox(self.centralwidget)
        self.searchSpec.setGeometry(QtCore.QRect(70, 120, 120, 121))
        self.searchSpec.setObjectName("searchSpec")
        self.specPeriod = QtWidgets.QComboBox(self.searchSpec)
        self.specPeriod.setGeometry(QtCore.QRect(0, 60, 111, 26))
        self.specPeriod.setEditable(True)
        self.specPeriod.setObjectName("specPeriod")
        self.specPeriod.addItem("")
        self.specPeriod.addItem("")
        self.specPeriod.addItem("")
        self.specPeriod.addItem("")
        self.specPeriod.addItem("")
        self.specPeriod.addItem("")
        self.specPeriod.addItem("")
        self.specDate = QtWidgets.QDateEdit(self.searchSpec)
        self.specDate.setGeometry(QtCore.QRect(0, 90, 110, 24))
        self.specDate.setCalendarPopup(True)
        self.specDate.setDate(QtCore.QDate(2019, 9, 10))
        self.specDate.setObjectName("specDate")
        self.specRoom = QtWidgets.QComboBox(self.searchSpec)
        self.specRoom.setGeometry(QtCore.QRect(0, 30, 111, 26))
        self.specRoom.setEditable(True)
        self.specRoom.setObjectName("specRoom")
        self.specRoom.addItem("")
        self.specRoom.addItem("")
        self.specRoom.addItem("")
        self.specRoom.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(210, 70, 521, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(280, 100, 91, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(370, 100, 91, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(460, 100, 91, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(550, 100, 91, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(640, 100, 91, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(280, 130, 91, 51))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(280, 180, 91, 51))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(280, 230, 91, 51))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(280, 280, 91, 51))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(280, 330, 91, 51))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_12.setGeometry(QtCore.QRect(280, 380, 91, 51))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_13.setGeometry(QtCore.QRect(280, 430, 91, 51))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_14.setGeometry(QtCore.QRect(370, 180, 91, 51))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_15.setGeometry(QtCore.QRect(370, 130, 91, 51))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_16.setGeometry(QtCore.QRect(370, 330, 91, 51))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_17.setGeometry(QtCore.QRect(370, 230, 91, 51))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_18.setGeometry(QtCore.QRect(370, 280, 91, 51))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.textBrowser_20 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_20.setGeometry(QtCore.QRect(370, 430, 91, 51))
        self.textBrowser_20.setObjectName("textBrowser_20")
        self.textBrowser_21 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_21.setGeometry(QtCore.QRect(460, 180, 91, 51))
        self.textBrowser_21.setObjectName("textBrowser_21")
        self.textBrowser_22 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_22.setGeometry(QtCore.QRect(460, 130, 91, 51))
        self.textBrowser_22.setObjectName("textBrowser_22")
        self.textBrowser_23 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_23.setGeometry(QtCore.QRect(460, 330, 91, 51))
        self.textBrowser_23.setObjectName("textBrowser_23")
        self.textBrowser_24 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_24.setGeometry(QtCore.QRect(460, 230, 91, 51))
        self.textBrowser_24.setObjectName("textBrowser_24")
        self.textBrowser_25 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_25.setGeometry(QtCore.QRect(460, 280, 91, 51))
        self.textBrowser_25.setObjectName("textBrowser_25")
        self.textBrowser_26 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_26.setGeometry(QtCore.QRect(460, 430, 91, 51))
        self.textBrowser_26.setObjectName("textBrowser_26")
        self.textBrowser_27 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_27.setGeometry(QtCore.QRect(460, 380, 91, 51))
        self.textBrowser_27.setObjectName("textBrowser_27")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_19.setGeometry(QtCore.QRect(550, 180, 91, 51))
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.textBrowser_28 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_28.setGeometry(QtCore.QRect(550, 130, 91, 51))
        self.textBrowser_28.setObjectName("textBrowser_28")
        self.textBrowser_29 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_29.setGeometry(QtCore.QRect(550, 330, 91, 51))
        self.textBrowser_29.setObjectName("textBrowser_29")
        self.textBrowser_30 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_30.setGeometry(QtCore.QRect(550, 230, 91, 51))
        self.textBrowser_30.setObjectName("textBrowser_30")
        self.textBrowser_31 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_31.setGeometry(QtCore.QRect(550, 280, 91, 51))
        self.textBrowser_31.setObjectName("textBrowser_31")
        self.textBrowser_33 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_33.setGeometry(QtCore.QRect(550, 430, 91, 51))
        self.textBrowser_33.setObjectName("textBrowser_33")
        self.textBrowser_39 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_39.setGeometry(QtCore.QRect(640, 180, 91, 51))
        self.textBrowser_39.setObjectName("textBrowser_39")
        self.textBrowser_41 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_41.setGeometry(QtCore.QRect(640, 130, 91, 51))
        self.textBrowser_41.setObjectName("textBrowser_41")
        self.textBrowser_42 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_42.setGeometry(QtCore.QRect(640, 330, 91, 51))
        self.textBrowser_42.setObjectName("textBrowser_42")
        self.textBrowser_43 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_43.setGeometry(QtCore.QRect(640, 230, 91, 51))
        self.textBrowser_43.setObjectName("textBrowser_43")
        self.textBrowser_44 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_44.setGeometry(QtCore.QRect(640, 280, 91, 51))
        self.textBrowser_44.setObjectName("textBrowser_44")
        self.textBrowser_45 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_45.setGeometry(QtCore.QRect(640, 430, 91, 51))
        self.textBrowser_45.setObjectName("textBrowser_45")
        self.textBrowser_46 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_46.setGeometry(QtCore.QRect(640, 380, 91, 51))
        self.textBrowser_46.setObjectName("textBrowser_46")
        self.textBrowser_32 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_32.setGeometry(QtCore.QRect(210, 130, 71, 51))
        self.textBrowser_32.setObjectName("textBrowser_32")
        self.textBrowser_34 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_34.setGeometry(QtCore.QRect(210, 180, 71, 51))
        self.textBrowser_34.setObjectName("textBrowser_34")
        self.textBrowser_35 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_35.setGeometry(QtCore.QRect(210, 230, 71, 51))
        self.textBrowser_35.setObjectName("textBrowser_35")
        self.textBrowser_36 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_36.setGeometry(QtCore.QRect(210, 280, 71, 51))
        self.textBrowser_36.setObjectName("textBrowser_36")
        self.textBrowser_37 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_37.setGeometry(QtCore.QRect(210, 330, 71, 51))
        self.textBrowser_37.setObjectName("textBrowser_37")
        self.textBrowser_38 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_38.setGeometry(QtCore.QRect(210, 380, 71, 51))
        self.textBrowser_38.setObjectName("textBrowser_38")
        self.textBrowser_40 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_40.setGeometry(QtCore.QRect(210, 430, 71, 51))
        self.textBrowser_40.setObjectName("textBrowser_40")
        self.textBrowser_47 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_47.setGeometry(QtCore.QRect(550, 380, 91, 51))
        self.textBrowser_47.setObjectName("textBrowser_47")
        self.textBrowser_48 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_48.setGeometry(QtCore.QRect(370, 380, 91, 51))
        self.textBrowser_48.setObjectName("textBrowser_48")
        self.textBrowser_49 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_49.setGeometry(QtCore.QRect(210, 100, 71, 31))
        self.textBrowser_49.setObjectName("textBrowser_49")
        self.textBrowser_50 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_50.setGeometry(QtCore.QRect(640, 480, 91, 51))
        self.textBrowser_50.setObjectName("textBrowser_50")
        self.textBrowser_51 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_51.setGeometry(QtCore.QRect(550, 430, 91, 101))
        self.textBrowser_51.setObjectName("textBrowser_51")
        self.textBrowser_52 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_52.setGeometry(QtCore.QRect(460, 480, 91, 51))
        self.textBrowser_52.setObjectName("textBrowser_52")
        self.textBrowser_53 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_53.setGeometry(QtCore.QRect(280, 480, 91, 51))
        self.textBrowser_53.setObjectName("textBrowser_53")
        self.textBrowser_54 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_54.setGeometry(QtCore.QRect(210, 480, 71, 51))
        self.textBrowser_54.setObjectName("textBrowser_54")
        self.textBrowser_55 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_55.setGeometry(QtCore.QRect(370, 430, 91, 101))
        self.textBrowser_55.setObjectName("textBrowser_55")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menugui = QtWidgets.QMenu(self.menubar)
        self.menugui.setObjectName("menugui")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menugui.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchAvail.setTitle(_translate("MainWindow", "Search Available"))
        self.availPeriod.setCurrentText(_translate("MainWindow", "period"))
        self.availPeriod.setItemText(0, _translate("MainWindow", "1"))
        self.availPeriod.setItemText(1, _translate("MainWindow", "2"))
        self.availPeriod.setItemText(2, _translate("MainWindow", "3"))
        self.availPeriod.setItemText(3, _translate("MainWindow", "4"))
        self.availPeriod.setItemText(4, _translate("MainWindow", "5"))
        self.availPeriod.setItemText(5, _translate("MainWindow", "6"))
        self.availPeriod.setItemText(6, _translate("MainWindow", "7"))
        self.searchSpec.setTitle(_translate("MainWindow", "Search Specific"))
        self.specPeriod.setCurrentText(_translate("MainWindow", "period"))
        self.specPeriod.setItemText(0, _translate("MainWindow", "1"))
        self.specPeriod.setItemText(1, _translate("MainWindow", "2"))
        self.specPeriod.setItemText(2, _translate("MainWindow", "3"))
        self.specPeriod.setItemText(3, _translate("MainWindow", "4"))
        self.specPeriod.setItemText(4, _translate("MainWindow", "5"))
        self.specPeriod.setItemText(5, _translate("MainWindow", "6"))
        self.specPeriod.setItemText(6, _translate("MainWindow", "7"))
        self.specRoom.setCurrentText(_translate("MainWindow", "room"))
        self.specRoom.setItemText(0, _translate("MainWindow", "ICT2"))
        self.specRoom.setItemText(1, _translate("MainWindow", "ICT3"))
        self.specRoom.setItemText(2, _translate("MainWindow", "Secondary MPR"))
        self.specRoom.setItemText(3, _translate("MainWindow", "Primary MPR"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Room</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">monday</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tuesday</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">wednesday</p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">thursday</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">friday</p></body></html>"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">lunch</span></p></body></html>"))
        self.textBrowser_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">lunch</span></p></body></html>"))
        self.textBrowser_45.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">lunch</span></p></body></html>"))
        self.textBrowser_32.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">7:35-8:25</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P1</span></p></body></html>"))
        self.textBrowser_34.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">8:25-9:15</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P2</span></p></body></html>"))
        self.textBrowser_35.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">9:15-10:05</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P3</span></p></body></html>"))
        self.textBrowser_36.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">10:40-11:30</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P4</span></p></body></html>"))
        self.textBrowser_37.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">11:30-12:20</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P5</span></p></body></html>"))
        self.textBrowser_38.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">12:20-1:10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P6</span></p></body></html>"))
        self.textBrowser_40.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">1:10-2:00</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P7</span></p></body></html>"))
        self.textBrowser_47.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">lunch</span></p></body></html>"))
        self.textBrowser_48.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">lunch</span></p></body></html>"))
        self.textBrowser_49.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">times</p></body></html>"))
        self.textBrowser_51.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">cca</span></p></body></html>"))
        self.textBrowser_54.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">2:00-2:50</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">P7</span></p></body></html>"))
        self.textBrowser_55.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">cca</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menugui.setTitle(_translate("MainWindow", "gui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
