# -*- coding: utf-8 -*-

import sys
from typing import Any

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import frame
from frame.CSS_template import CSS
from dbase.databasecreate import CreateDB
from dbase.dbapi import APIAxiomDB
from log_setting import logger


class Ui_MainWindow(QMainWindow):
    old_order = None
    client = None
    car = None
    order = None
    help = None
    btn_frame = None
    menu = None
    list_client = None
    list_car = None
    list_order = None
    logo_frame = None

    @logger.catch
    def add_action(self):
        # self.a = QFont()
        Ui_MainWindow.btn_frame.btn_pushButton_help.clicked.connect(lambda: self.change_tab(4))
        Ui_MainWindow.btn_frame.btn_pushButton_exit.clicked.connect(lambda: QtWidgets.QApplication.exit())
        Ui_MainWindow.order.btn_pushButton_new_car.clicked.connect(lambda: self.change_tab(2))
        Ui_MainWindow.order.btn_pushButton_new_client.clicked.connect(lambda: self.change_tab(1))
        Ui_MainWindow.car.btn_pushButton_new_client.clicked.connect(lambda: self.change_tab(1))
        Ui_MainWindow.client.btn_pushButton_smile.clicked.connect(lambda: self.dialog())

        Ui_MainWindow.list_client.listWidget_list.clicked.connect(
            lambda: self.set_text_from_client(Ui_MainWindow.list_client.listWidget_list.currentItem()))
        Ui_MainWindow.list_car.listWidget_list.clicked.connect(
            lambda: self.set_text_from_car(Ui_MainWindow.list_car.listWidget_list.currentItem()))
        Ui_MainWindow.list_order.listWidget_list.clicked.connect(
            lambda: self.set_text_from_order(Ui_MainWindow.list_order.listWidget_list.currentItem()))
        Ui_MainWindow.order.btn_pushButton_order_close.clicked.connect(
            lambda: self.close_act(Ui_MainWindow.order.txt_label_order_number.text()))

    @classmethod
    @logger.catch
    def close_act(cls, num: int):
        query = CreateDB()
        if not query.isClose(num):
            query.close_order(num, True)
            Ui_MainWindow.order.btn_pushButton_order_close.setStyleSheet("background-color: rgb(85, 170, 0);")
            Ui_MainWindow.order.btn_pushButton_order_close.setText('Открыть акт')
        else:
            query.close_order(num, False)
            Ui_MainWindow.order.btn_pushButton_order_close.setStyleSheet("background-color: rgb(255, 170, 0);")
            Ui_MainWindow.order.btn_pushButton_order_close.setText('Закрыть акт')

    @classmethod
    @logger.catch
    def set_text_from_client(cls, item: QtWidgets.QListWidgetItem) -> None:
        """Устанавливает клиента в лист заявки и лист клиента,
        выводит в виджеты order и car списки зависимых от клиента машин и актов
        """
        query = APIAxiomDB()
        client_item = Ui_MainWindow.list_client.get_item_text_from_list(item)

        Ui_MainWindow.list_order.print_widget(client_item.id)
        Ui_MainWindow.list_car.print_widget(client_item.id)

        Ui_MainWindow.order.driver_item = query.get_list_driver_for_company(client_item.id)
        print(Ui_MainWindow.order.driver_item)
        logger.debug('name', Ui_MainWindow.order.driver_item)
        completer = QtWidgets.QCompleter(Ui_MainWindow.order.driver_item)
        Ui_MainWindow.order.txt_edit_lineEdit_client_owner_name.setCompleter(completer)

        Ui_MainWindow.order.txt_label_client_name.setText(client_item.full_name)
        Ui_MainWindow.order.txt_label_client_identification_number.setText(str(client_item.pan_code))
        Ui_MainWindow.order.txt_label_order_number.setText(str(query.count_act() + 1))
        Ui_MainWindow.order.txt_label_order_number_prefix.setText('A')
        Ui_MainWindow.order.current_id = None
        Ui_MainWindow.order.txt_edit_lineEdit_client_owner_name.setText('')
        Ui_MainWindow.order.txt_edit_lineEdit_client_job_title.setText('')

        Ui_MainWindow.car.txt_label_client_name.setText(client_item.full_name)
        Ui_MainWindow.car.txt_label_client_identification_number.setText(str(client_item.pan_code))

        Ui_MainWindow.client.txt_edit_lineEdit_client_name.setText(client_item.name)
        Ui_MainWindow.client.txt_edit_textEdit_client_full_name.setText(client_item.full_name)
        Ui_MainWindow.client.txt_edit_textEdit_client_address.setText(client_item.address)
        Ui_MainWindow.client.txt_edit_lineEdit_client_identification_number.setText(str(client_item.pan_code))
        Ui_MainWindow.client.txt_edit_lineEdit_client_phone.setText(client_item.telefone)
        Ui_MainWindow.client.txt_edit_lineEdit_client_mobile_phone.setText(client_item.mobile)
        Ui_MainWindow.client.current_id = client_item.id

    @classmethod
    @logger.catch
    def set_text_from_order(cls, item: QtWidgets.QListWidgetItem) -> None:
        """Устанавливает клиента в лист заявки и лист клиента,
        выводит в виджеты order и car списки зависимых от клиента машин и актов
        """
        new = CreateDB()
        query = APIAxiomDB()
        order_item = Ui_MainWindow.list_order.get_item_text_from_list(item)
        driver = query.get_driver(order_item.id)
        client_item = query.get_client_from_order(order_item.id)
        car_item = query.get_car_from_order(order_item.id)

        Ui_MainWindow.order.txt_label_order_number.setText(str(order_item.id))
        Ui_MainWindow.order.txt_label_order_number_prefix.setText(order_item.prefix)
        Ui_MainWindow.order.txt_label_client_name.setText(client_item.full_name)
        Ui_MainWindow.order.txt_label_client_identification_number.setText(str(client_item.pan_code))
        Ui_MainWindow.order.txt_label_brand.setText(car_item.name)
        Ui_MainWindow.order.txt_label_car_number.setText(car_item.number)
        Ui_MainWindow.order.txt_label_model.setText(car_item.model)
        Ui_MainWindow.order.txt_label_vin_code.setText(car_item.vin_code)
        Ui_MainWindow.order.txt_edit_lineEdit_client_owner_name.setText(driver.name)
        Ui_MainWindow.order.txt_edit_lineEdit_client_job_title.setText(driver.job)
        Ui_MainWindow.order.current_id = order_item.id

        Ui_MainWindow.order.checkBox_1_repair_request.setChecked(False)
        Ui_MainWindow.order.checkBox_2_application_order.setChecked(False)
        Ui_MainWindow.order.checkBox_3_act_of_acceptance.setChecked(False)
        Ui_MainWindow.order.checkBox_4_internal_consumption.setChecked(True)

        if not new.isClose(order_item.id):
            Ui_MainWindow.order.btn_pushButton_order_close.setStyleSheet("background-color: rgb(255, 170, 0);")
            Ui_MainWindow.order.btn_pushButton_order_close.setText('Закрыть акт')
        else:
            Ui_MainWindow.order.btn_pushButton_order_close.setStyleSheet("background-color: rgb(85, 170, 0);")
            Ui_MainWindow.order.btn_pushButton_order_close.setText('Открыть акт')

        Ui_MainWindow.list_car.print_one(order_item.id)
        Ui_MainWindow.list_client.print_one(order_item.id)

    @logger.catch
    @classmethod
    def set_text_from_car(cls, item: QtWidgets.QListWidgetItem) -> None:
        """Устанавливает машину в лист заявки и лист машины,
        выводит в виджеты order списки зависимых от машины актов
        """
        query = APIAxiomDB()
        car_item = Ui_MainWindow.list_car.get_item_text_from_list(item.text())
        client_item = query.get_client_from_car_id(car_item.id)

        Ui_MainWindow.list_order.print_widget(car_item.id, 'car')
        Ui_MainWindow.list_client.print_widget(client_item)

        Ui_MainWindow.order.driver_item = query.get_list_driver_for_company(client_item.id)
        completer = QtWidgets.QCompleter(Ui_MainWindow.order.driver_item)
        Ui_MainWindow.order.txt_edit_lineEdit_client_owner_name.setCompleter(completer)

        Ui_MainWindow.order.txt_label_brand.setText(car_item.name)
        Ui_MainWindow.order.txt_label_car_number.setText(car_item.number)
        Ui_MainWindow.order.txt_label_model.setText(car_item.model)
        Ui_MainWindow.order.txt_label_vin_code.setText(car_item.vin_code)
        Ui_MainWindow.order.txt_label_order_number.setText(str(query.count_act() + 1))
        Ui_MainWindow.order.txt_label_order_number_prefix.setText('A')
        Ui_MainWindow.order.current_id = None
        Ui_MainWindow.order.txt_edit_lineEdit_client_owner_name.setText('')
        Ui_MainWindow.order.txt_edit_lineEdit_client_job_title.setText('')
        Ui_MainWindow.order.txt_label_client_name.setText(client_item.full_name)
        Ui_MainWindow.order.txt_label_client_identification_number.setText(str(client_item.pan_code))

        Ui_MainWindow.car.txt_label_brand.setText(car_item.name)
        Ui_MainWindow.car.txt_label_car_number.setText(car_item.number)
        Ui_MainWindow.car.txt_label_model.setText(car_item.model)
        Ui_MainWindow.car.txt_label_vin_code.setText(car_item.vin_code)
        Ui_MainWindow.car.current_id = car_item.id

    @logger.catch
    def change_tab(self, tab: Any) -> None:
        self.tabWidget.setCurrentIndex(tab)
        self.change_logo_text(tab)

    @logger.catch
    def change_logo_text(self, index: Any) -> None:
        Ui_MainWindow.logo_frame.txt_label_logo.clear()
        Ui_MainWindow.logo_frame.txt_label_logo.setText(self.tabWidget.tabText(index))

    @logger.catch
    def set_top_right_tab_widget(self, frame: Any) -> QtWidgets.QTabWidget:
        self.tabWidget = QtWidgets.QTabWidget(frame)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_order = QtWidgets.QWidget()
        self.tab_order.setObjectName("tab_order")

        self.tabWidget.addTab(self.tab_order, "")

        self.tab_client = QtWidgets.QWidget()
        self.tab_client.setObjectName("tab_client")
        self.tabWidget.addTab(self.tab_client, "")

        self.tab_new_car = QtWidgets.QWidget()
        self.tab_new_car.setObjectName("tab_new_car")
        self.tabWidget.addTab(self.tab_new_car, "")

        self.tab_old_order = QtWidgets.QWidget()
        self.tab_old_order.setObjectName("tab_old_order")
        self.tabWidget.addTab(self.tab_old_order, "")

        self.tab_help = QtWidgets.QWidget()
        self.tab_help.setObjectName("tab_help")
        self.tabWidget.addTab(self.tab_help, "")

        self.tabWidget.setCurrentIndex(0)

        return self.tabWidget

    @logger.catch
    def click_tab(self, tab):
        print(tab)
        self.change_logo_text(tab)

    @logger.catch
    def set_top_frame(self, frame):
        self.MainTopFrame = QtWidgets.QFrame(frame)
        self.MainTopFrame.setAutoFillBackground(True)
        self.MainTopFrame.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.MainTopFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainTopFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainTopFrame.setObjectName("MainTopFrame")

        self.gridLayoutWidget_Main = QtWidgets.QWidget(self.MainTopFrame)
        self.gridLayoutWidget_Main.setGeometry(QtCore.QRect(0, 10, 1500, 631))
        self.gridLayoutWidget_Main.setAutoFillBackground(True)
        self.gridLayoutWidget_Main.setObjectName("gridLayoutWidget_Tab")

        self.gridLayout_listWidget_main = QtWidgets.QGridLayout(self.gridLayoutWidget_Main)
        self.gridLayout_listWidget_main.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_listWidget_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_listWidget_main.setHorizontalSpacing(1)
        self.gridLayout_listWidget_main.setVerticalSpacing(1)
        self.gridLayout_listWidget_main.setObjectName("gridLayout_listWidget_tab")

        self.frame_root_tabWidget = QtWidgets.QFrame(self.gridLayoutWidget_Main)
        self.frame_root_tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_root_tabWidget.setAutoFillBackground(True)
        self.frame_root_tabWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_root_tabWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_root_tabWidget.setObjectName("frame_root_tabWidget")

        self.gridLayoutWidget_Tab = QtWidgets.QWidget(self.frame_root_tabWidget)
        self.gridLayoutWidget_Tab.setGeometry(QtCore.QRect(0, 0, 930, 631))
        self.gridLayoutWidget_Tab.setAutoFillBackground(True)
        self.gridLayoutWidget_Tab.setObjectName("gridLayoutWidget_Tab")

        self.gridLayout_listWidget_tab = QtWidgets.QGridLayout(self.gridLayoutWidget_Tab)
        self.gridLayout_listWidget_tab.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_listWidget_tab.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_listWidget_tab.setHorizontalSpacing(1)
        self.gridLayout_listWidget_tab.setVerticalSpacing(1)
        self.gridLayout_listWidget_tab.setObjectName("gridLayout_listWidget_tab")

        self.gridLayout_listWidget_tab.addWidget(self.set_top_right_tab_widget(self.gridLayoutWidget_Tab), 0, 0, 1, 1)

        self.gridLayout_listWidget_main.addWidget(self.frame_root_tabWidget, 0, 0, 1, 1)
        self.gridLayout_listWidget_main.addWidget(self.set_top_left_list_widget(self.gridLayoutWidget_Main), 0, 1, 1, 1)

    @logger.catch
    def set_top_left_list_widget(self, frame):
        self.frame_main_listWidget = QtWidgets.QFrame(frame)
        self.frame_main_listWidget.setMinimumSize(QtCore.QSize(900, 100))
        self.frame_main_listWidget.setMaximumSize(QtCore.QSize(940, 16777215))
        self.frame_main_listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_main_listWidget.setAutoFillBackground(False)
        self.frame_main_listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_main_listWidget.setObjectName("frame_main_listWidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_main_listWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 940, 631))
        self.gridLayoutWidget.setAutoFillBackground(False)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_listWidget = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_listWidget.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_listWidget.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_listWidget.setHorizontalSpacing(1)
        self.gridLayout_listWidget.setVerticalSpacing(1)
        self.gridLayout_listWidget.setObjectName("gridLayout_listWidget")

        self.gridLayout_listWidget.addWidget(CSS.line_widget(self.gridLayoutWidget), 0, 0, 1, 1)
        self.gridLayout_listWidget.addWidget(Ui_MainWindow.list_client.set_frame(self.gridLayoutWidget), 0, 1, 1, 1)
        self.gridLayout_listWidget.addWidget(CSS.line_widget(self.gridLayoutWidget), 0, 2, 1, 1)
        self.gridLayout_listWidget.addWidget(Ui_MainWindow.list_car.set_frame(self.gridLayoutWidget), 0, 3, 1, 1)
        self.gridLayout_listWidget.addWidget(CSS.line_widget(self.gridLayoutWidget), 0, 4, 1, 1)
        self.gridLayout_listWidget.addWidget(Ui_MainWindow.list_order.set_frame(self.gridLayoutWidget), 0, 5, 1, 1)
        self.gridLayout_listWidget.addWidget(CSS.line_widget(self.gridLayoutWidget), 0, 6, 1, 1)

        return self.frame_main_listWidget

    @logger.catch
    def set_root_layout(self, frame):
        self.verticalLayout = QtWidgets.QVBoxLayout(frame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.RootLayout = QtWidgets.QVBoxLayout()
        self.RootLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.RootLayout.setObjectName("RootLayout")

        self.RootLayout.addWidget(Ui_MainWindow.logo_frame.set_frame(self.central_widget))
        self.set_top_frame(self.central_widget)
        self.RootLayout.addWidget(self.MainTopFrame)
        self.RootLayout.addWidget(Ui_MainWindow.btn_frame.set_frame(self.central_widget))

        self.verticalLayout.addLayout(self.RootLayout)

    @logger.catch
    def dialog(self):

        self.setObjectName("Dialog")
        self.resize(400, 300)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 265, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 14, 321, 251))
        self.plainTextEdit.setStyleSheet("background-color: rgb(215, 215, 215);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label.setStyleSheet("background-color: 'green';")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

        def set_text(text, color='green'):
            self.plainTextEdit.setPlainText(text)

    @logger.catch
    def window_create(self):
        self.setObjectName("MainWindow")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(QtCore.QSize(1500, 850))
        self.setMinimumSize(QtCore.QSize(1500, 850))
        self.adjustSize()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(True)

        CreateDB.create_db()

        Ui_MainWindow.old_order = frame.old_order_frame.OldOrder()
        Ui_MainWindow.client = frame.client_frame.Client()
        Ui_MainWindow.car = frame.car_frame.Car()
        Ui_MainWindow.order = frame.order_frame.Order()
        Ui_MainWindow.help = frame.help_frame.Help()
        Ui_MainWindow.btn_frame = frame.button_frame.BtnFrame()
        Ui_MainWindow.menu = frame.menubar.MenuBar()
        Ui_MainWindow.list_client = frame.list_widget_frame.ListWClient()
        Ui_MainWindow.list_car = frame.list_widget_frame.ListWCar()
        Ui_MainWindow.list_order = frame.list_widget_frame.ListWOrder()
        Ui_MainWindow.logo_frame = frame.logo_frame.LogoFrame()

    @logger.catch
    def setupUi(self):
        self.window_create()

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.central_widget.setObjectName("central_widget")

        self.set_root_layout(self.central_widget)

        Ui_MainWindow.order.set_frame(self.tab_order)
        Ui_MainWindow.client.set_frame(self.tab_client)
        Ui_MainWindow.car.set_frame(self.tab_new_car)
        Ui_MainWindow.old_order.set_frame(self.tab_old_order)
        Ui_MainWindow.help.set_body(self.tab_help)
        Ui_MainWindow.menu.set_frame(self)

        Ui_MainWindow.list_client.print()

        self.setCentralWidget(self.central_widget)

        self.retranslateUi()
        self.add_action()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "BaseSTO"))

        self.setWindowTitle(_translate("Dialog", "Dialog"))

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_order),
            _translate("MainWindow", "Новый Акт")
        )
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_order),
            _translate("MainWindow", "Создание нового акта, печать Заказ-нарядов и Внутренних накладных")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_client),
            _translate("MainWindow", "Новый клиент")
        )
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_client),
            _translate("MainWindow", "Внесение данных о новом клиенте")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_new_car),
            _translate("MainWindow", "Новая машина")
        )
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_new_car),
            _translate("MainWindow", "Внесение данных о новой машине клиента")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_old_order),
            _translate("MainWindow", "Закрытые заказ-наряды")
        )
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tab_old_order),
            _translate("MainWindow", "Выписка по закрытым Заказ-нарядам")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_help),
            _translate("MainWindow", "Help")
        )


@logger.catch
def new_work():
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    new_work()
