from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDateTime

from CSS_template import CSS
from datetime import datetime
from dbapi import APIAxiomDB
from databasecreate import CreateDB


class OldOrder:
    def __init__(self):
        self.frame = None
        self.btn_pushButton_data_choice = None
        self.btn_pushButton_order_open = None
        self.btn_pushButton_print = None
        self.listWidget_list = None
        self.frame_data_po = None
        self.dateEdit = None
        self.frame_data = None
        self.dateEdit_1 = None

        self.item_text = None

    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 593))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.set_body()
        
    def set_body(self):
        self.btn_pushButton_data_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_data_choice.setGeometry(QtCore.QRect(210, 50, 151, 33))
        self.btn_pushButton_data_choice.setFont(CSS.set_font(12, True, 75))
        self.btn_pushButton_data_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_data_choice.setObjectName("btn_pushButton_data_choice")

        self.btn_pushButton_order_open = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_order_open.setGeometry(QtCore.QRect(453, 50, 101, 33))
        self.btn_pushButton_order_open.setFont(CSS.set_font(12, False, 50))
        self.btn_pushButton_order_open.setAutoFillBackground(False)
        self.btn_pushButton_order_open.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_order_open.setObjectName("btn_pushButton_order_open")

        self.btn_pushButton_print = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_print.setGeometry(QtCore.QRect(15, 50, 101, 33))
        self.btn_pushButton_print.setFont(CSS.set_font(12, False, 50))
        self.btn_pushButton_print.setAutoFillBackground(False)
        self.btn_pushButton_print.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_print.setObjectName("btn_pushButton_print")

        self.listWidget_list = QtWidgets.QListWidget(self.frame)
        self.listWidget_list.setGeometry(QtCore.QRect(10, 110, 551, 481))
        self.listWidget_list.setFont(CSS.set_font(11))
        self.listWidget_list.setAutoFillBackground(True)
        self.listWidget_list.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.listWidget_list.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_list.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.listWidget_list.setTabKeyNavigation(True)
        self.listWidget_list.setProperty("showDropIndicator", False)
        self.listWidget_list.setAlternatingRowColors(True)
        self.listWidget_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget_list.setObjectName("listWidget_list")

        self.frame_data_po = QtWidgets.QFrame(self.frame)
        self.frame_data_po.setGeometry(QtCore.QRect(310, 0, 251, 41))
        self.frame_data_po.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_data_po.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data_po.setObjectName("frame_data_po")
        
        self.dateEdit = QtWidgets.QDateEdit(self.frame_data_po)
        self.dateEdit.setGeometry(QtCore.QRect(5, 5, 241, 37))
        self.dateEdit.setFont(CSS.set_font(14, True, 75))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setWrapping(True)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(3)
        self.dateEdit.setDate(datetime.now().date())
        self.dateEdit.setObjectName("dateEdit")
        
        self.frame_data = QtWidgets.QFrame(self.frame)
        self.frame_data.setGeometry(QtCore.QRect(10, 0, 251, 41))
        self.frame_data.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_data.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_data.setObjectName("frame_data")

        self.dateEdit_1 = QtWidgets.QDateEdit(self.frame_data)
        self.dateEdit_1.setGeometry(QtCore.QRect(5, 5, 241, 37))
        self.dateEdit_1.setFont(CSS.set_font(14, True, 75))
        self.dateEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_1.setWrapping(True)
        self.dateEdit_1.setFrame(True)
        self.dateEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_1.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dateEdit_1.setProperty("showGroupSeparator", True)
        self.dateEdit_1.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_1.setCalendarPopup(True)
        self.dateEdit_1.setCurrentSectionIndex(3)
        self.dateEdit_1.setDate(datetime.now().date())
        self.dateEdit_1.setObjectName("dateEdit")

        self.add_action()
        self.retranslateUi()

    def add_action(self):
        self.btn_pushButton_data_choice.clicked.connect(lambda: self.print_old_order())
        self.btn_pushButton_order_open.clicked.connect(lambda: self.open_order())
        self.listWidget_list.clicked.connect(lambda: self.get_text(self.listWidget_list.currentItem()))

    def open_order(self):
        upd = CreateDB()
        query = APIAxiomDB()
        if self.item_text:
            old_order_item = self.item_text.split('-')
            upd.close_order(query.get_order_from_id(int(old_order_item[0])), False)
            self.print_old_order()

    def get_text(self, item):
        self.item_text = item.text()

    def print_old_order(self):
        self.listWidget_list.clear()
        query = APIAxiomDB()
        start = QDateTime(self.dateEdit_1.date()).toPyDateTime()
        end = QDateTime(self.dateEdit.date()).toPyDateTime()
        old_order_item_list = query.get_list_old_order(start=start, end=end)
        self.add_order_to_list(old_order_item_list)

    def add_order_to_list(self, list_temp):
        query = APIAxiomDB()
        for old_order_item in list_temp:
            self.listWidget_list.addItem(
                '{act_id}-{prefix}: {data}| {client}:\t {car_number} - {brand}-{model}'.format(
                    act_id=old_order_item.id,
                    prefix=old_order_item.prefix,
                    data=old_order_item.data,
                    client=query.get_client_from_order(old_order_item.id).full_name,
                    car_number=query.get_car_from_order(old_order_item.id).number,
                    brand=query.get_car_from_order(old_order_item.id).name,
                    model=query.get_car_from_order(old_order_item.id).model
                )
            )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_pushButton_data_choice.setText(_translate("MainWindow", "Выбрать период"))
        self.btn_pushButton_order_open.setText(_translate("MainWindow", "Открыть Акт"))
        self.btn_pushButton_print.setText(_translate("MainWindow", "Печать"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d  MMMM   yyyy"))
        self.dateEdit_1.setDisplayFormat(_translate("MainWindow", "d  MMMM   yyyy"))


if __name__ == '__main__':
    pass
