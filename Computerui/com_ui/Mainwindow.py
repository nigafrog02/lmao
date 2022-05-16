# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1499, 935)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-20, 0, 1521, 81))
        self.stackedWidget.setStyleSheet("background-color: rgb(199, 7, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Home = QtWidgets.QLabel(self.page)
        self.Home.setGeometry(QtCore.QRect(550, 10, 381, 51))
        self.Home.setStyleSheet("color: rgb(255, 255, 255);\n"
"font:  25pt \"Microsoft YaHei UI\";")
        self.Home.setObjectName("Home")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.discount_next_button = QtWidgets.QPushButton(self.centralwidget)
        self.discount_next_button.setGeometry(QtCore.QRect(1370, 830, 121, 41))
        self.discount_next_button.setObjectName("discount_next_button")
        self.btn_spec1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_spec1.setGeometry(QtCore.QRect(10, 810, 93, 28))
        self.btn_spec1.setObjectName("btn_spec1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 480, 461, 281))
        self.groupBox_2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 40, 221, 231))
        self.groupBox_10.setStyleSheet("background-color: rgb(90, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox_10.setObjectName("groupBox_10")
        self.Ac_com_1 = QtWidgets.QCheckBox(self.groupBox_10)
        self.Ac_com_1.setGeometry(QtCore.QRect(10, 20, 201, 51))
        self.Ac_com_1.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.Ac_com_1.setObjectName("Ac_com_1")
        self.Ac2_com_1 = QtWidgets.QCheckBox(self.groupBox_10)
        self.Ac2_com_1.setGeometry(QtCore.QRect(10, 70, 201, 61))
        self.Ac2_com_1.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.Ac2_com_1.setObjectName("Ac2_com_1")
        self.Ac3_com_1 = QtWidgets.QCheckBox(self.groupBox_10)
        self.Ac3_com_1.setGeometry(QtCore.QRect(10, 130, 191, 81))
        self.Ac3_com_1.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.Ac3_com_1.setObjectName("Ac3_com_1")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_11.setGeometry(QtCore.QRect(230, 40, 221, 231))
        self.groupBox_11.setStyleSheet("background-color: rgb(90, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_11.setObjectName("groupBox_11")
        self.Ac4_com_1 = QtWidgets.QCheckBox(self.groupBox_11)
        self.Ac4_com_1.setGeometry(QtCore.QRect(10, 30, 191, 41))
        self.Ac4_com_1.setObjectName("Ac4_com_1")
        self.Ac5_com_1 = QtWidgets.QCheckBox(self.groupBox_11)
        self.Ac5_com_1.setGeometry(QtCore.QRect(10, 80, 191, 61))
        self.Ac5_com_1.setObjectName("Ac5_com_1")
        self.Ac6_com_1 = QtWidgets.QCheckBox(self.groupBox_11)
        self.Ac6_com_1.setGeometry(QtCore.QRect(10, 150, 201, 51))
        self.Ac6_com_1.setObjectName("Ac6_com_1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(230, 380, 231, 101))
        self.groupBox_3.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.colour_com1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.colour_com1.setGeometry(QtCore.QRect(10, 30, 171, 21))
        self.colour_com1.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.colour_com1.setObjectName("colour_com1")
        self.validation = QtWidgets.QRadioButton(self.groupBox_3)
        self.validation.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.validation.setObjectName("validation")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 380, 241, 101))
        self.groupBox_4.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.os_com_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.os_com_2.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.os_com_2.setObjectName("os_com_2")
        self.os1_com_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.os1_com_2.setGeometry(QtCore.QRect(10, 60, 161, 21))
        self.os1_com_2.setObjectName("os1_com_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(700, 380, 261, 101))
        self.groupBox_5.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_5.setObjectName("groupBox_5")
        self.colour_com2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.colour_com2.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.colour_com2.setObjectName("colour_com2")
        self.colour2_com2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.colour2_com2.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.colour2_com2.setObjectName("colour2_com2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 80, 20, 881))
        self.line.setStyleSheet("color: rgb(13, 13, 13);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(950, 80, 20, 841))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 380, 231, 101))
        self.groupBox.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox.setObjectName("groupBox")
        self.os_com_1 = QtWidgets.QRadioButton(self.groupBox)
        self.os_com_1.setGeometry(QtCore.QRect(10, 30, 161, 21))
        self.os_com_1.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.os_com_1.setObjectName("os_com_1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.os_com_1)
        self.os2com_1 = QtWidgets.QRadioButton(self.groupBox)
        self.os2com_1.setGeometry(QtCore.QRect(10, 60, 161, 21))
        self.os2com_1.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.os2com_1.setObjectName("os2com_1")
        self.buttonGroup.addButton(self.os2com_1)
        self.lbl_G15 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_G15.setGeometry(QtCore.QRect(680, 770, 71, 31))
        self.lbl_G15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_G15.setObjectName("lbl_G15")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 330, 151, 31))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 330, 151, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.groupBox_12 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(460, 480, 501, 281))
        self.groupBox_12.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 40, 231, 231))
        self.groupBox_6.setStyleSheet("background-color: rgb(90, 0, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.Ac_com_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ac_com_2.setGeometry(QtCore.QRect(10, 60, 191, 41))
        self.Ac_com_2.setObjectName("Ac_com_2")
        self.Ac2_com_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ac2_com_2.setGeometry(QtCore.QRect(10, 100, 211, 51))
        self.Ac2_com_2.setObjectName("Ac2_com_2")
        self.Ac3_com_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ac3_com_2.setGeometry(QtCore.QRect(10, 140, 211, 71))
        self.Ac3_com_2.setObjectName("Ac3_com_2")
        self.rb_none = QtWidgets.QRadioButton(self.groupBox_6)
        self.rb_none.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.rb_none.setObjectName("rb_none")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_13.setGeometry(QtCore.QRect(240, 40, 251, 231))
        self.groupBox_13.setStyleSheet("background-color: rgb(90, 0, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.groupBox_13.setObjectName("groupBox_13")
        self.Ac4_com_2 = QtWidgets.QCheckBox(self.groupBox_13)
        self.Ac4_com_2.setGeometry(QtCore.QRect(10, 30, 221, 41))
        self.Ac4_com_2.setObjectName("Ac4_com_2")
        self.Ac5_com_2 = QtWidgets.QCheckBox(self.groupBox_13)
        self.Ac5_com_2.setGeometry(QtCore.QRect(10, 90, 231, 31))
        self.Ac5_com_2.setObjectName("Ac5_com_2")
        self.Ac6_com_2 = QtWidgets.QCheckBox(self.groupBox_13)
        self.Ac6_com_2.setGeometry(QtCore.QRect(10, 140, 221, 41))
        self.Ac6_com_2.setObjectName("Ac6_com_2")
        self.lbl_inspiron = QtWidgets.QLabel(self.centralwidget)
        self.lbl_inspiron.setGeometry(QtCore.QRect(220, 770, 81, 31))
        self.lbl_inspiron.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_inspiron.setObjectName("lbl_inspiron")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 770, 211, 31))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1180, 330, 151, 31))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.groupBox_14 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_14.setGeometry(QtCore.QRect(960, 380, 281, 101))
        self.groupBox_14.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_14.setFlat(False)
        self.groupBox_14.setCheckable(False)
        self.groupBox_14.setObjectName("groupBox_14")
        self.os_com_3 = QtWidgets.QRadioButton(self.groupBox_14)
        self.os_com_3.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.os_com_3.setObjectName("os_com_3")
        self.os1_com_3 = QtWidgets.QRadioButton(self.groupBox_14)
        self.os1_com_3.setGeometry(QtCore.QRect(10, 60, 161, 21))
        self.os1_com_3.setObjectName("os1_com_3")
        self.groupBox_15 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_15.setGeometry(QtCore.QRect(1240, 380, 261, 101))
        self.groupBox_15.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_15.setObjectName("groupBox_15")
        self.colour_com_3 = QtWidgets.QRadioButton(self.groupBox_15)
        self.colour_com_3.setGeometry(QtCore.QRect(10, 20, 231, 51))
        self.colour_com_3.setObjectName("colour_com_3")
        self.validation_2 = QtWidgets.QRadioButton(self.groupBox_15)
        self.validation_2.setGeometry(QtCore.QRect(10, 70, 101, 21))
        self.validation_2.setObjectName("validation_2")
        self.groupBox_16 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_16.setGeometry(QtCore.QRect(960, 480, 541, 281))
        self.groupBox_16.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(199, 7, 0);")
        self.groupBox_16.setObjectName("groupBox_16")
        self.groupBox_17 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_17.setGeometry(QtCore.QRect(10, 40, 521, 231))
        self.groupBox_17.setStyleSheet("background-color: rgb(90, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_17.setObjectName("groupBox_17")
        self.Ac_com_3 = QtWidgets.QCheckBox(self.groupBox_17)
        self.Ac_com_3.setGeometry(QtCore.QRect(10, 30, 251, 71))
        self.Ac_com_3.setObjectName("Ac_com_3")
        self.Ac2_com_3 = QtWidgets.QCheckBox(self.groupBox_17)
        self.Ac2_com_3.setGeometry(QtCore.QRect(10, 130, 271, 51))
        self.Ac2_com_3.setObjectName("Ac2_com_3")
        self.btn_spec2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_spec2.setGeometry(QtCore.QRect(470, 810, 93, 28))
        self.btn_spec2.setObjectName("btn_spec2")
        self.btn_spec3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_spec3.setGeometry(QtCore.QRect(970, 810, 101, 31))
        self.btn_spec3.setObjectName("btn_spec3")
        self.lbl_M15 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_M15.setGeometry(QtCore.QRect(1180, 770, 81, 31))
        self.lbl_M15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_M15.setObjectName("lbl_M15")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 770, 211, 31))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(970, 770, 211, 31))
        self.label_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.counterinspiron = QtWidgets.QLabel(self.centralwidget)
        self.counterinspiron.setGeometry(QtCore.QRect(370, 800, 16, 31))
        self.counterinspiron.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.counterinspiron.setObjectName("counterinspiron")
        self.decreasecount_inspiron = QtWidgets.QPushButton(self.centralwidget)
        self.decreasecount_inspiron.setGeometry(QtCore.QRect(330, 800, 31, 31))
        self.decreasecount_inspiron.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.decreasecount_inspiron.setObjectName("decreasecount_inspiron")
        self.increasecount_inspirion = QtWidgets.QPushButton(self.centralwidget)
        self.increasecount_inspirion.setGeometry(QtCore.QRect(390, 800, 31, 31))
        self.increasecount_inspirion.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.increasecount_inspirion.setObjectName("increasecount_inspirion")
        self.decreasecount_G15 = QtWidgets.QPushButton(self.centralwidget)
        self.decreasecount_G15.setGeometry(QtCore.QRect(830, 800, 31, 31))
        self.decreasecount_G15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.decreasecount_G15.setObjectName("decreasecount_G15")
        self.increasecount_G15 = QtWidgets.QPushButton(self.centralwidget)
        self.increasecount_G15.setGeometry(QtCore.QRect(890, 800, 31, 31))
        self.increasecount_G15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.increasecount_G15.setObjectName("increasecount_G15")
        self.counterG15 = QtWidgets.QLabel(self.centralwidget)
        self.counterG15.setGeometry(QtCore.QRect(870, 800, 16, 31))
        self.counterG15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.counterG15.setObjectName("counterG15")
        self.decreasecount_M15 = QtWidgets.QPushButton(self.centralwidget)
        self.decreasecount_M15.setGeometry(QtCore.QRect(1250, 800, 31, 31))
        self.decreasecount_M15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.decreasecount_M15.setObjectName("decreasecount_M15")
        self.increasecount_M15 = QtWidgets.QPushButton(self.centralwidget)
        self.increasecount_M15.setGeometry(QtCore.QRect(1310, 800, 31, 31))
        self.increasecount_M15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.increasecount_M15.setObjectName("increasecount_M15")
        self.counterM15 = QtWidgets.QLabel(self.centralwidget)
        self.counterM15.setGeometry(QtCore.QRect(1290, 800, 16, 31))
        self.counterM15.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.counterM15.setObjectName("counterM15")
        self.lbl_stock = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stock.setGeometry(QtCore.QRect(330, 760, 111, 31))
        self.lbl_stock.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_stock.setObjectName("lbl_stock")
        self.lbl_stock_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stock_2.setGeometry(QtCore.QRect(830, 760, 111, 31))
        self.lbl_stock_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_stock_2.setObjectName("lbl_stock_2")
        self.lbl_stock_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stock_3.setGeometry(QtCore.QRect(1250, 760, 111, 31))
        self.lbl_stock_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_stock_3.setObjectName("lbl_stock_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 80, 1491, 301))
        self.stackedWidget_2.setStyleSheet("background-color: rgb(255, 248, 244);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label_12.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(580, 50, 261, 211))
        self.label_11.setStyleSheet("image: url(:/res/img/G 15.jpg);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/res/image/G15.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(1110, 50, 271, 191))
        self.label_13.setStyleSheet("image: url(:/res/img/M15.jpg);")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/res/image/M15.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(110, 70, 231, 151))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/res/image/4zu3_Dell_Inspiron_15_3501.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_11.raise_()
        self.label_10.raise_()
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 850, 251, 31))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lbl_mw_inspiron = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mw_inspiron.setGeometry(QtCore.QRect(370, 850, 81, 31))
        self.lbl_mw_inspiron.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_mw_inspiron.setObjectName("lbl_mw_inspiron")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(700, 850, 201, 31))
        self.label_8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.lbl_mw_G15 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mw_G15.setGeometry(QtCore.QRect(900, 850, 51, 31))
        self.lbl_mw_G15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_mw_G15.setObjectName("lbl_mw_G15")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1070, 850, 201, 31))
        self.label_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.lbl_mw_M15 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mw_M15.setGeometry(QtCore.QRect(1270, 850, 51, 31))
        self.lbl_mw_M15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lbl_mw_M15.setObjectName("lbl_mw_M15")
        self.stackedWidget_2.raise_()
        self.stackedWidget.raise_()
        self.discount_next_button.raise_()
        self.btn_spec1.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.groupBox.raise_()
        self.lbl_G15.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.groupBox_12.raise_()
        self.lbl_inspiron.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.groupBox_14.raise_()
        self.groupBox_15.raise_()
        self.groupBox_16.raise_()
        self.btn_spec2.raise_()
        self.btn_spec3.raise_()
        self.lbl_M15.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.counterinspiron.raise_()
        self.decreasecount_inspiron.raise_()
        self.increasecount_inspirion.raise_()
        self.decreasecount_G15.raise_()
        self.increasecount_G15.raise_()
        self.counterG15.raise_()
        self.decreasecount_M15.raise_()
        self.increasecount_M15.raise_()
        self.counterM15.raise_()
        self.lbl_stock.raise_()
        self.lbl_stock_2.raise_()
        self.lbl_stock_3.raise_()
        self.label_5.raise_()
        self.lbl_mw_inspiron.raise_()
        self.label_8.raise_()
        self.lbl_mw_G15.raise_()
        self.label_9.raise_()
        self.lbl_mw_M15.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1499, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home.setText(_translate("MainWindow", "The Gaming Store"))
        self.discount_next_button.setText(_translate("MainWindow", "Next"))
        self.btn_spec1.setText(_translate("MainWindow", "Specs"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Accessories"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Input Devices"))
        self.Ac_com_1.setText(_translate("MainWindow", "Dell Wired Mouse with \n"
"Fingerprint Reader - MS819"))
        self.Ac2_com_1.setText(_translate("MainWindow", "Alienware Wired/Wireless \n"
"Gaming Mouse | AW610M"))
        self.Ac3_com_1.setText(_translate("MainWindow", "ALIENWARE RGB \n"
"MECHANICAL \n"
"GAMING KEYBOARD\n"
"| AW410K"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Cables"))
        self.Ac4_com_1.setText(_translate("MainWindow", "Dell Adapter \n"
"- USB-C to VGA"))
        self.Ac5_com_1.setText(_translate("MainWindow", "Dell Adaptor- USB-C \n"
"to DisplayPort"))
        self.Ac6_com_1.setText(_translate("MainWindow", "Dell Adapter - USB 3.0 \n"
"to Ethernet PXE Boot"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Colors"))
        self.colour_com1.setText(_translate("MainWindow", "Platinum Silver"))
        self.validation.setText(_translate("MainWindow", "validation"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Operating System"))
        self.os_com_2.setText(_translate("MainWindow", "Windows11 Home "))
        self.os1_com_2.setText(_translate("MainWindow", "Windows11 Home Pro"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Colour"))
        self.colour_com2.setText(_translate("MainWindow", "Phantom Grey with \n"
"speckles"))
        self.colour2_com2.setText(_translate("MainWindow", "Dark shadow grey"))
        self.groupBox.setTitle(_translate("MainWindow", "Operating Systems"))
        self.os_com_1.setText(_translate("MainWindow", "Windows11 Home "))
        self.os2com_1.setText(_translate("MainWindow", "Windows11 Home Pro"))
        self.lbl_G15.setText(_translate("MainWindow", "5349"))
        self.label_2.setText(_translate("MainWindow", "Inspiron 15 Laptop"))
        self.label_3.setText(_translate("MainWindow", "G15 Gaming Laptop"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Accessories"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Monitor"))
        self.Ac_com_2.setText(_translate("MainWindow", "Dell Alienware 25 Monitor \n"
"- AW2521H"))
        self.Ac2_com_2.setText(_translate("MainWindow", "Alienware 25 Gaming Monitor \n"
"- AW2521HF"))
        self.Ac3_com_2.setText(_translate("MainWindow", "Alienware 27 240Hz monitor \n"
"- AW2720HF\n"
"- AW2720HF"))
        self.rb_none.setText(_translate("MainWindow", "None"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Gadgets"))
        self.Ac4_com_2.setText(_translate("MainWindow", "Dell UltraSharp Webcam \n"
"- WB7022"))
        self.Ac5_com_2.setText(_translate("MainWindow", "Dell Premier ANC Wireless \n"
"Headset - WL7022"))
        self.Ac6_com_2.setText(_translate("MainWindow", "Dell Pro Wireless Headset \n"
"- WL5022"))
        self.lbl_inspiron.setText(_translate("MainWindow", "3449"))
        self.label.setText(_translate("MainWindow", "Price for Inspirion 15 [RM]:"))
        self.label_4.setText(_translate("MainWindow", "Alienware M15"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Operating System"))
        self.os_com_3.setText(_translate("MainWindow", "Windows11 Home "))
        self.os1_com_3.setText(_translate("MainWindow", "Windows11 Home Pro"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Colour"))
        self.colour_com_3.setText(_translate("MainWindow", "Dark Side of the Moon with High\n"
"Endurance Clear Coat and \n"
"Silky Smooth Finish"))
        self.validation_2.setText(_translate("MainWindow", "validation"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Accessories"))
        self.groupBox_17.setTitle(_translate("MainWindow", "HeadSets"))
        self.Ac_com_3.setText(_translate("MainWindow", "Alienware 510H 7.1 Gaming \n"
"Headset AW510H \n"
"- Dark Side of the Moon"))
        self.Ac2_com_3.setText(_translate("MainWindow", "Alienware 510H 7.1 Gaming \n"
"Headset AW510H - Lunar Light"))
        self.btn_spec2.setText(_translate("MainWindow", "Specs"))
        self.btn_spec3.setText(_translate("MainWindow", "Specs"))
        self.lbl_M15.setText(_translate("MainWindow", "8409"))
        self.label_6.setText(_translate("MainWindow", "Price for G-15 laptop [RM]:"))
        self.label_7.setText(_translate("MainWindow", "Total for M-15 laptop [RM]:"))
        self.counterinspiron.setText(_translate("MainWindow", "0"))
        self.decreasecount_inspiron.setText(_translate("MainWindow", "-"))
        self.increasecount_inspirion.setText(_translate("MainWindow", "+"))
        self.decreasecount_G15.setText(_translate("MainWindow", "-"))
        self.increasecount_G15.setText(_translate("MainWindow", "+"))
        self.counterG15.setText(_translate("MainWindow", "0"))
        self.decreasecount_M15.setText(_translate("MainWindow", "-"))
        self.increasecount_M15.setText(_translate("MainWindow", "+"))
        self.counterM15.setText(_translate("MainWindow", "0"))
        self.lbl_stock.setText(_translate("MainWindow", "Sry we only have \n"
"3 stocks left"))
        self.lbl_stock_2.setText(_translate("MainWindow", "Sry we only have \n"
"2 stocks left"))
        self.lbl_stock_3.setText(_translate("MainWindow", "Sry we only have \n"
"5 stocks left"))
        self.label_12.setText(_translate("MainWindow", "Store"))
        self.label_5.setText(_translate("MainWindow", "Total Price for Inspirion 15 [RM]:"))
        self.lbl_mw_inspiron.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Total Price for G-15 [RM]:"))
        self.lbl_mw_G15.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Total Price for M-15 [RM]:"))
        self.lbl_mw_M15.setText(_translate("MainWindow", "0"))
from . import res_rc
