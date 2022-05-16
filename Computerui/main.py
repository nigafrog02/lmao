import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from com_ui.Mainwindow import Ui_MainWindow
from com_ui.mainwindow2 import Ui_MainWindow2
from com_ui.com_spec1 import Ui_spec1
from com_ui.dialog2 import Ui_spec_2
from com_ui.com_spec3 import Ui_spec_3
from com_ui.welcome import Ui_Welcome
from PyQt5 import QtWidgets



class mainWindow(QMainWindow,Ui_MainWindow):
    #the window for store page in this python file , in this class i store all the variables and functions that are needed for the store page
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.secondwindow = discount_page()

        # default values for each computer
        # default counter values for computer [ number of computer to be order buy user , for multiple purchases]
        mainWindow.price = float(3449)
        mainWindow.price_G15 = float(5349)
        mainWindow.price_M15 = float(8409)
        mainWindow.OS_Inspiron = 'Windows 11 Home'
        mainWindow.OS_G15 = 'Windows 11 Home'
        mainWindow.OS_M15 = 'Windows 11 Home'
        mainWindow.counter_Inspiron = 0
        mainWindow.counter_G15 = 0
        mainWindow.counter_M15 = 0

        # i named my payment page as discount_page()
        self.discount_page = discount_page()
        self.discount_next_button.clicked.connect(self.open_discount)
        self.discount_next_button.setStyleSheet("QPushButton::hover"
                                                "{"
                                                "background-color:lightgreen;""}")#hovers to button becomes green

        #specifications of computer 1
        self.Spec1 = Spec1()
        self.btn_spec1.clicked.connect(self.openspec1)
        self.btn_spec1.setStyleSheet("QPushButton::hover"
                                      "{"
                                      "background-color:lightgreen;""}")
        # specifications of computer 2
        self.Spec2 = Spec2()
        self.btn_spec2.clicked.connect(self.openspec2)
        self.btn_spec2.setStyleSheet("QPushButton::hover"
                                     "{"
                                     "background-color:lightgreen;""}")
        # specifications of computer 3
        self.Spec3 = Spec3()
        self.btn_spec3.clicked.connect(self.openspec3)
        self.btn_spec3.setStyleSheet("QPushButton::hover"
                                     "{"
                                     "background-color:lightgreen;""}")

        #operating System for inspiron
        self.os_com_1.setChecked(True)
        self.os_com_1.toggled.connect(self.os_type)
        #colour for inspiron
        self.colour_com1.setChecked(True)
        self.validation.setVisible(False)
        #Accessories for inspiron
        self.Ac_com_1.stateChanged.connect(self.Dell_Wired_Mouse)
        self.Ac2_com_1.stateChanged.connect(self.Alienware_Wired)
        self.Ac3_com_1.stateChanged.connect(self.ALIENWARE_RGB)
        self.Ac4_com_1.stateChanged.connect(self.Dell_USB_C)
        self.Ac5_com_1.stateChanged.connect(self.Dell_Adaptor)
        self.Ac6_com_1.stateChanged.connect(self.Dell_Adapter)
        # operating system G15
        self.os_com_2.setChecked(True)
        self.colour_com2.setChecked(True)
        self.os_com_2.toggled.connect(self.os_type1)
        #Accessory G15
        self.Ac_com_2.toggled.connect(self.Dell_Alienware)
        self.Ac2_com_2.toggled.connect(self.Alienware_25)
        self.Ac3_com_2.toggled.connect(self.Alienware_27)
        self.Ac4_com_2.stateChanged.connect(self.Dell_UltraSharp)
        self.Ac5_com_2.stateChanged.connect(self.Dell_Premier)
        self.Ac6_com_2.stateChanged.connect(self.Dell_Pro)
        self.rb_none.toggled.connect(self.none)
        #operating system M15
        self.os_com_3.setChecked(True)
        self.colour_com_3.setChecked(True)
        self.validation_2.setVisible(False)
        self.os1_com_3.toggled.connect(self.os_type2)
        #Accessory M15
        self.Ac_com_3.stateChanged.connect(self.Alienware_510H)
        self.Ac2_com_3.stateChanged.connect(self.Headset_AW510H)
        #counter_inspiron
        self.decreasecount_inspiron.clicked.connect(self.dec_inspiron)
        self.increasecount_inspirion.clicked.connect(self.inc_inspiron)
        #counter_G15
        self.decreasecount_G15.clicked.connect(self.dec_G15)
        self.increasecount_G15.clicked.connect(self.inc_G15)
        # counter_M15
        self.decreasecount_M15.clicked.connect(self.dec_M15)
        self.increasecount_M15.clicked.connect(self.inc_M15)
        #stocks , made a validation / limitation of orders for the user
        self.lbl_stock.setVisible(False)
        self.lbl_stock_2.setVisible(False)
        self.lbl_stock_3.setVisible(False)

    #operating system inspiron
    def os_type(self):
        # in this function i checked the status of os_com_1 , if it is checked then minus the price for 300 [because i already set a default value of 300]
        # elif the os2com_1 checkbox status is checked then add 300 to the price .
        if self.os_com_1.isChecked():
            mainWindow.price -= 300
            mainWindow.OS_Inspiron = 'Windows 11 Home'
            self.lbl_inspiron.setNum(mainWindow.price)
        elif self.os2com_1.isChecked():
            mainWindow.price += 300
            mainWindow.OS_Inspiron = 'Windows 11 Home Pro'
            self.lbl_inspiron.setNum(mainWindow.price)
    #Accessory Inspiron
    def Dell_Wired_Mouse(self):
        # in this function i check if Ac_com_1 is checked if yes , then the price will add 174 and the lbl_inspiron will set the price of the computer based on choices of the user
        # elif the price will minus 174 and set the number of the price on lbl_inspiron.
        # this comment applies to all the other functions....
        if self.Ac_com_1.isChecked():
            mainWindow.price += 174
            self.lbl_inspiron.setNum(mainWindow.price)
        else:
            mainWindow.price -=174
            self.lbl_inspiron.setNum(mainWindow.price)
    def Alienware_Wired(self):
        if self.Ac2_com_1.isChecked():
            mainWindow.price += 411.09
            self.lbl_inspiron.setNum(mainWindow.price)
        else:
            mainWindow.price -= 411.09
            self.lbl_inspiron.setNum(mainWindow.price)
    def ALIENWARE_RGB(self):
        if self.Ac3_com_1.isChecked():
            mainWindow.price += 631.50
            self.lbl_inspiron.setNum(mainWindow.price)
        else:
            mainWindow.price -= 631.50
            self.lbl_inspiron.setNum(mainWindow.price)
    def Dell_USB_C(self):
        if self.Ac4_com_1.isChecked():
            mainWindow.price += 201
            self.lbl_inspiron.setNum(mainWindow.price)
        else:
            mainWindow.price -= 201
            self.lbl_inspiron.setNum(mainWindow.price)
    def Dell_Adaptor(self):
        if self.Ac5_com_1.isChecked():
            mainWindow.price += 162
            self.lbl_inspiron.setNum(mainWindow.price)
        else:
            mainWindow.price -= 162
            self.lbl_inspiron.setNum(mainWindow.price)
    def Dell_Adapter(self):
        if self.Ac6_com_1.isChecked():
            mainWindow.price += 158
            self.lbl_inspiron.setNum(mainWindow.price)
        else:
            mainWindow.price -= 158
            self.lbl_inspiron.setNum(mainWindow.price)
    # operating system G15
    def os_type1(self):
        if self.os_com_2.isChecked():
            mainWindow.price_G15 -= 300
            self.lbl_G15.setNum(mainWindow.price_G15)
            mainWindow.OS_G15 = 'Windows 11 Home'
        elif self.os1_com_2.isChecked():
            mainWindow.price_G15 += 300
            self.lbl_G15.setNum(mainWindow.price_G15)
            mainWindow.OS_G15 = 'Windows 11 Home Pro'
            # Accessory G15
    def Dell_Alienware(self):
        if self.Ac_com_2.isChecked():
            mainWindow.price_G15 += 3319
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -= 3319
            self.lbl_G15.setNum(mainWindow.price_G15)
    def Alienware_25(self):
        if self.Ac2_com_2.isChecked():
            mainWindow.price_G15 += 2069
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -= 2069
            self.lbl_G15.setNum(mainWindow.price_G15)
    def Alienware_27(self):
        if self.Ac3_com_2.isChecked():
            mainWindow.price_G15 += 2299
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -= 2299
            self.lbl_G15.setNum(mainWindow.price_G15)
    def Dell_UltraSharp(self):
        if self.Ac4_com_2.isChecked():
            mainWindow.price_G15 += 867.36
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -= 867.36
            self.lbl_G15.setNum(mainWindow.price_G15)
    def Dell_Premier(self):
        if self.Ac5_com_2.isChecked():
            mainWindow.price_G15 += 1146.65
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -= 1146.65
            self.lbl_G15.setNum(mainWindow.price_G15)
    def Dell_Pro(self):
        if self.Ac6_com_2.isChecked():
            mainWindow.price_G15 += 922.96
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -= 922.96
            self.lbl_G15.setNum(mainWindow.price_G15)
    def none(self):
        if self.rb_none.isChecked():
            mainWindow.price_G15 += 0
            self.lbl_G15.setNum(mainWindow.price_G15)
        else:
            mainWindow.price_G15 -=0
            self.lbl_G15.setNum(mainWindow.price_G15)
    #operating system M15
    def os_type2(self):
        if self.os_com_3.isChecked():
            mainWindow.price_M15 -= 300
            mainWindow.OS_M15 = 'Windows 11 Home'
            self.lbl_M15.setNum(mainWindow.price_M15)
        elif self.os1_com_3.isChecked():
            mainWindow.price_M15 += 300
            mainWindow.OS_M15 = 'Windows 11 Home Pro'
            self.lbl_M15.setNum(mainWindow.price_M15)
    #accessory M15
    def Alienware_510H(self):
        if self.Ac_com_3.isChecked():
            mainWindow.price_M15 += 433.30
            self.lbl_M15.setNum(mainWindow.price_M15)
        else:
            mainWindow.price_M15 -= 433.30
            self.lbl_M15.setNum(mainWindow.price_M15)
    def Headset_AW510H(self):
        if self.Ac2_com_3.isChecked():
            mainWindow.price_M15 += 436.80
            self.lbl_M15.setNum(mainWindow.price_M15)
        else:
            mainWindow.price_M15 -= 436.80
            self.lbl_M15.setNum(mainWindow.price_M15)
    #counter inspiron
    def inc_inspiron(self):
        # This function in particularly is to keep track of how many numbers of order does the user wants and limits the user's order amount
        # if the user clicks the button , counter increases by one when the number of count is lesser than 3
        # else [more than 3] , prompt message " no more stock"
        if mainWindow.counter_Inspiron < 3:
            mainWindow.counter_Inspiron += 1
            self.counterinspiron.setNum(mainWindow.counter_Inspiron)
            self.lbl_mw_inspiron.setNum(mainWindow.price * mainWindow.counter_Inspiron)
        else:
            self.lbl_stock.setVisible(True)

    def dec_inspiron(self):
        # this function is to revert the number of orders from the user
        # if the number of count of orders is more than zero , then the count of orders will be minused by 1
        # else [ lesser than 0 ] ,do nothing
        if mainWindow.counter_Inspiron >0:
            mainWindow.counter_Inspiron -= 1
            self.counterinspiron.setNum(mainWindow.counter_Inspiron)
            self.lbl_mw_inspiron.setNum(mainWindow.price * mainWindow.counter_Inspiron)
        else:
            return
    #counter G15
    def dec_G15(self):
        if mainWindow.counter_G15 >0:
            mainWindow.counter_G15 -=1
            self.counterG15.setNum(mainWindow.counter_G15)
            self.lbl_mw_G15.setNum(mainWindow.price_G15 * mainWindow.counter_G15)
        else:
            return
    def inc_G15(self):
        if mainWindow.counter_G15 < 2:
            mainWindow.counter_G15 += 1
            self.counterG15.setNum(mainWindow.counter_G15)
            self.lbl_mw_G15.setNum(mainWindow.price_G15 * mainWindow.counter_G15)
        else:
            self.lbl_stock_2.setVisible(True)
    # counter M15
    def dec_M15(self):
        if mainWindow.counter_M15 >0:
            mainWindow.counter_M15 -=1
            self.counterM15.setNum(mainWindow.counter_M15)
            self.lbl_mw_M15.setNum(mainWindow.price_M15 * mainWindow.counter_M15)
        else:
            return
    def inc_M15(self):
        if mainWindow.counter_M15 < 5:
            mainWindow.counter_M15 += 1
            self.counterM15.setNum(mainWindow.counter_M15)
            self.lbl_mw_M15.setNum(mainWindow.price_M15 * mainWindow.counter_M15)
        else:
            self.lbl_stock_3.setVisible(True)


    def openspec1(self):
        #show com_1 specifications
        self.Spec1.show()
    def openspec2(self):
        #show com_2 specifications
        self.Spec2.show()
    def openspec3(self):
        #show com_3 specifications
        self.Spec3.show()


    def open_discount(self):
        # if user didnt order any item , pop a Qmessage box and ask whether to continue to payment with zero orders.
        if mainWindow.counter_G15 == 0 and mainWindow.counter_Inspiron ==0 and mainWindow.counter_M15 ==0:
            reply = QMessageBox.question(self, "Pls Buy something :(",
                                        "Our shop is very broke now help pls :(\nPress 'OK' to go back\nPress 'No' to proceed to Payment page",
                                        QMessageBox.Ok | QMessageBox.No )
            if reply == QMessageBox.No:#passing information
                self.secondwindow.no_inspiron.setNum(mainWindow.counter_Inspiron)
                self.secondwindow.no_G15.setNum(mainWindow.counter_G15)
                self.secondwindow.no_M15.setNum(mainWindow.counter_M15)
                self.secondwindow.lbl_totalG15.setNum(mainWindow.price_G15 * mainWindow.counter_G15)
                self.secondwindow.lbl_totalinspiron.setNum(mainWindow.price * mainWindow.counter_Inspiron)
                self.secondwindow.lbl_totalM15.setNum(mainWindow.price_M15 * mainWindow.counter_M15)
                self.secondwindow.Total_sumprice.setNum((mainWindow.price_G15 * mainWindow.counter_G15)+(mainWindow.price * mainWindow.counter_Inspiron)+(mainWindow.price_M15 * mainWindow.counter_M15))
                self.secondwindow.show()
        else:
            reply2 = QMessageBox.question(self, "Proceeding to Payment page",
                                         "Are you sure you want to continue?\nPress 'Yes' to proceed to payment page\nPress 'No' to go back",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply2 == QMessageBox.Yes:#passing information
                self.secondwindow.no_inspiron.setNum(mainWindow.counter_Inspiron)
                self.secondwindow.no_G15.setNum(mainWindow.counter_G15)
                self.secondwindow.no_M15.setNum(mainWindow.counter_M15)
                self.secondwindow.lbl_totalG15.setNum(mainWindow.price_G15 * mainWindow.counter_G15)
                self.secondwindow.lbl_totalinspiron.setNum(mainWindow.price * mainWindow.counter_Inspiron)
                self.secondwindow.lbl_totalM15.setNum(mainWindow.price_M15 * mainWindow.counter_M15)
                self.secondwindow.Total_sumprice.setNum(
                    (mainWindow.price_G15 * mainWindow.counter_G15) + (mainWindow.price * mainWindow.counter_Inspiron) + (
                                mainWindow.price_M15 * mainWindow.counter_M15))
                self.secondwindow.lbl_finalosinspiron.setText(mainWindow.OS_Inspiron)
                self.secondwindow.lbl_finalosG15.setText(mainWindow.OS_G15)
                self.secondwindow.lbl_finalosM15.setText(mainWindow.OS_M15)
                self.secondwindow.show()


class discount_page(QMainWindow,Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




class welcome_page(QMainWindow,Ui_Welcome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Next_store.clicked.connect(self.next_store)
        self.main_window = mainWindow()
        self.Next_store.setStyleSheet("QPushButton::hover"
                                                "{"
                                                "background-color:lightgreen;""}")

    def next_store(self):
        self.main_window.show()


class Spec1(QDialog,Ui_spec1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Spec2(QDialog,Ui_spec_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Spec3(QDialog,Ui_spec_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


#main program
if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    screen1 = welcome_page()
    screen2 = mainWindow()
    screen3 = discount_page()
    widget.addWidget(screen1)
    widget.addWidget(screen2)
    widget.addWidget(screen3)
    widget.setFixedHeight(900)
    widget.setFixedWidth(1500)



    widget.show()
    app.exec_()

