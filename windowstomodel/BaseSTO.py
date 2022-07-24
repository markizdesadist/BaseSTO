# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame,
                             QMenu, QMenuBar, QStatusBar, QAction,
                             QLabel, QPushButton, QWidget)
from mainframe import MainFrame
from client import Client
from order import Order
from car import Car
from logolabael import Logo
from templateCSS import CSS


class Ui_MainWindow(object):


    mainframe = MainFrame(MainWindow)
    client = Client()
    order = Order()
    car = Car()
    logo = Logo()

    def __int__(self, MainWindow):
        mainframe = MainFrame(MainWindow)

    def set_frame(self):
        # self.main_frame = QFrame(parent=self.centralwidget)
        # self.main_frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        # self.main_frame.setFrameShape(QFrame.StyledPanel)
        # self.main_frame.setFrameShadow(QFrame.Raised)
        # self.main_frame.setObjectName("main_frame")



        self.frame_buttom = QFrame(self.mainframe.main_frame)
        self.frame_buttom.setGeometry(QtCore.QRect(0, 520, 801, 41))
        self.frame_buttom.setFrameShape(QFrame.StyledPanel)
        self.frame_buttom.setFrameShadow(QFrame.Raised)
        self.frame_buttom.setObjectName("frame_buttom")



        self.frame_car = QFrame(self.mainframe.main_frame)
        self.frame_car.setEnabled(True)
        self.frame_car.setGeometry(QtCore.QRect(0, 30, 420, 490))
        self.frame_car.setFrameShape(QFrame.StyledPanel)
        self.frame_car.setFrameShadow(QFrame.Raised)
        self.frame_car.setObjectName("frame_car")
        self.frame_car.hide()

        self.frame_client = QFrame(self.mainframe.main_frame)
        self.frame_client.setEnabled(True)
        self.frame_client.setGeometry(QtCore.QRect(0, 30, 420, 491))
        self.frame_client.setFrameShape(QFrame.StyledPanel)
        self.frame_client.setFrameShadow(QFrame.Raised)
        self.frame_client.setObjectName("frame_client")
        self.frame_client.hide()



    def set_bottom(self):
        self.pushButton_quit = QPushButton(self.frame_buttom)
        self.pushButton_quit.setGeometry(QtCore.QRect(720, 15, 56, 21))
        self.pushButton_quit.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_quit.setObjectName("pushButton_quit")

        self.pushButton_old_order_list = QPushButton(self.frame_buttom)
        self.pushButton_old_order_list.setGeometry(QtCore.QRect(10, 15, 80, 21))
        self.pushButton_old_order_list.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_old_order_list.setObjectName("pushButton_old_order_list")

        self.pushButton_client_list = QPushButton(self.frame_buttom)
        self.pushButton_client_list.setGeometry(QtCore.QRect(90, 15, 80, 21))
        self.pushButton_client_list.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_client_list.setObjectName("pushButton_client_list")

        self.pushButton_car_list = QPushButton(self.frame_buttom)
        self.pushButton_car_list.setGeometry(QtCore.QRect(170, 15, 80, 21))
        self.pushButton_car_list.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_car_list.setObjectName("pushButton_car_list")

        self.pushButton_new_order = QPushButton(self.frame_buttom)
        self.pushButton_new_order.setGeometry(QtCore.QRect(250, 15, 80, 21))
        self.pushButton_new_order.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_new_order.setObjectName("pushButton_new_order")

        self.pushButton_help = QPushButton(self.frame_buttom)
        self.pushButton_help.setGeometry(QtCore.QRect(660, 15, 56, 21))
        self.pushButton_help.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_help.setObjectName("pushButton_help")

        self.line_hbot_1 = QFrame(self.frame_buttom)
        self.line_hbot_1.setGeometry(QtCore.QRect(10, 1, 791, 16))
        self.line_hbot_1.setFrameShape(QFrame.HLine)
        self.line_hbot_1.setFrameShadow(QFrame.Sunken)
        self.line_hbot_1.setObjectName("line_hbot_1")

    def set_menu_bar(self, MainWindow):
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 29))
        self.menubar.setObjectName("menubar")

        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        self.menuNewCar = QMenu(self.menuView)
        self.menuNewCar.setObjectName("menuNewCar")

        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        self.menuAbaut = QMenu(self.menubar)
        self.menuAbaut.setObjectName("menuAbaut")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")

        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")

        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionNew_order = QAction(MainWindow)
        self.actionNew_order.setObjectName("actionNew_order")

        self.actionNew_client = QAction(MainWindow)
        self.actionNew_client.setObjectName("actionNew_client")

        self.action_order = QAction(MainWindow)
        self.action_order.setObjectName("action_order")

        self.action_client = QAction(MainWindow)
        self.action_client.setObjectName("action_client")

        self.action_car = QAction(MainWindow)
        self.action_car.setObjectName("action_car")

        self.actionSee_old_order = QAction(MainWindow)
        self.actionSee_old_order.setObjectName("actionSee_old_order")

        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.actionAbaut_of_programm = QAction(MainWindow)
        self.actionAbaut_of_programm.setObjectName("actionAbaut_of_programm")

        self.menuFile.addAction(self.actionFile)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuNewCar.addAction(self.action_order)
        self.menuNewCar.addAction(self.action_client)
        self.menuNewCar.addAction(self.action_car)
        self.menuView.addAction(self.menuNewCar.menuAction())
        self.menuView.addAction(self.actionSee_old_order)
        self.menuAbaut.addAction(self.actionHelp)
        self.menuAbaut.addSeparator()
        self.menuAbaut.addAction(self.actionAbaut_of_programm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbaut.menuAction())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1024, 600)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../photo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        # self.set_frame()
        Ui_MainWindow.mainframe.main_frame(self.centralwidget)
        Ui_MainWindow.mainframe.set_body()
        self.order.set_body(Ui_MainWindow.mainframe.main_frame)
        # Ui_MainWindow.logo.set_logo()
        # self.set_bottom()
        self.set_menu_bar(MainWindow)
        # self.add_functions()
        #
        # self.frame_order.raise_()
        # self.frame_logo.raise_()
        # self.listWidget_order.raise_()
        # self.listWidget_client.raise_()
        # self.listWidget_car.raise_()
        # self.frame_buttom.raise_()
        # self.line_vfrm_1.raise_()
        # self.line_vfrm_2.raise_()
        # self.label_frame_client.raise_()
        # self.label_frame_car.raise_()
        # self.label_frame_order.raise_()
        # self.pushButton_update_client.raise_()
        # self.pushButton_update_car.raise_()
        # self.pushButton_update_order.raise_()
        # self.frame_client.raise_()
        # self.frame_car.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def add_functions(self):
        # Ui_MainWindow.order.pushButton_print.clicked.connect(lambda: self.action_to_change_window(Ui_MainWindow.order.pushButton_print))
        # Ui_MainWindow.order.pushButton_order_close.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.order.pushButton_order_close)
        # )
        # Ui_MainWindow.order.pushButton_new_client.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.order.pushButton_new_client, 'новый клиент')
        # )
        # Ui_MainWindow.order.pushButton_new_car.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.order.pushButton_new_car, 'новая машина')
        # )

        # Ui_MainWindow.client.pushButton_save_client.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.client.pushButton_save_client)
        # )
        #
        # Ui_MainWindow.car.pushButton_save_car.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.car.pushButton_save_car)
        # )
        # Ui_MainWindow.car.pushButton_new_client.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.car.pushButton_new_client)
        # )

        # Ui_MainWindow.mainframe.pushButton_update_client.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.mainframe.pushButton_update_client)
        # )
        # Ui_MainWindow.mainframe.pushButton_update_order.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.mainframe.pushButton_update_order)
        # )
        # Ui_MainWindow.mainframe.pushButton_update_car.clicked.connect(
        #     lambda: self.action_to_change_window(Ui_MainWindow.mainframe.pushButton_update_car)
        # )
        # self.pushButton_car_list
        # self.pushButton_client_list
        # self.pushButton_old_order_list
        # self.pushButton_new_order.clicked.connect(lambda: self.action_to_change_window(self.pushButton_new_order))
        self.pushButton_quit.clicked.connect(lambda: QApplication.quit())
        # self.pushButton_help.clicked.connect(lambda: self.action_to_change_window(self.pushButton_help))

        self.actionExit.triggered.connect(lambda: QApplication.quit())
        # self.action_client.triggered.connect(lambda: self.action_to_change_window(self.action_client))
        # self.action_car.triggered.connect(lambda: self.action_to_change_window(self.action_car))

    # @classmethod
    # def body_frame(cls, frame: QFrame = None, hide: bool = True):
    #     if hide:
    #         frame.hide()
    #     else:
    #         frame.show()
    #
    # def clicked(self, act):
    #     print(12123)
    #     print(act.text())
    #
    # def action_to_change_window(self, btn, text):
    #     self.body_frame(self.frame_order, hide=True)
    #     self.body_frame(self.frame_client, hide=True)
    #     self.body_frame(self.frame_car, hide=True)
    #     change_body_and_action_dict = {
    #         'новый клиент': lambda: Ui_MainWindow.client.set_body(self.frame_client),
    #         '... client': lambda: Ui_MainWindow.client.set_body(self.frame_client),
    #         'новый акт': lambda: Ui_MainWindow.order.set_body(self.frame_order),
    #         'новая машина': lambda: Ui_MainWindow.car.set_body(self.frame_car),
    #         '... car': lambda: Ui_MainWindow.car.set_body(self.frame_car),
    #         'save': print,
    #         'справка': print,
    #         'quit': QApplication.quit,
    #         'закрыть акт': print
    #     }
    #     if btn.objectName().startswith('pushButton'):
    #         btn.setDown(True)
    #     change_body_and_action_dict[text.lower().strip()]()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BaseSTO"))
        # self.label_logo.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton_old_order_list.setText(_translate("MainWindow", "Старые заказы"))
        self.pushButton_client_list.setText(_translate("MainWindow", "Список клиентов"))
        self.pushButton_car_list.setText(_translate("MainWindow", "Список машин"))
        self.pushButton_new_order.setText(_translate("MainWindow", "Новый Акт"))
        self.pushButton_help.setText(_translate("MainWindow", "Справка"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuNewCar.setTitle(_translate("MainWindow", "New Car"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbaut.setTitle(_translate("MainWindow", "Help"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_order.setText(_translate("MainWindow", "New order"))
        self.actionNew_client.setText(_translate("MainWindow", "New client"))
        self.action_order.setText(_translate("MainWindow", "... order"))
        self.action_client.setText(_translate("MainWindow", "... client"))
        self.action_car.setText(_translate("MainWindow", "... car"))
        self.actionSee_old_order.setText(_translate("MainWindow", "See old order"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbaut_of_programm.setText(_translate("MainWindow", "Abaut of programm"))


def Main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    Main()
