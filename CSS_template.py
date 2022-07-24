from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPicture, QPixmap

from dbapi import APIAxiomDB


class CSS:
    """Шаблоны для повторяющихся элементов, шрифта, и др."""

    def __int__(self):
        self.btn_pushButton_refresh = QtWidgets.QPushButton()

    @classmethod
    def set_font(cls, size=12, bold=False, weight=0):
        """Установка шрифтов."""
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        font.setWeight(weight)
        return font

    @classmethod
    def set_label_param(cls):
        return (120, 20)

    @classmethod
    def line_widget(cls, frame):
        """Задание характеристик элементов Line, для последующего размещения в фрейме LWidget."""
        line = QtWidgets.QFrame(frame)
        line.setMaximumSize(QtCore.QSize(10, 16777215))
        line.setAutoFillBackground(False)
        line.setStyleSheet("background-color: rgb(255, 255, 0);\nborder-color: rgb(255, 0, 0);")
        line.setLineWidth(1)
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        return line

    @classmethod
    def line_tab(cls, frame):
        line = QtWidgets.QFrame(frame)
        line.setGeometry(QtCore.QRect(3, 280, 551, 20))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line_13")

        line_1 = QtWidgets.QFrame(frame)
        line_1.setGeometry(QtCore.QRect(0, 90, 551, 20))
        line_1.setFrameShape(QtWidgets.QFrame.HLine)
        line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_1.setObjectName("line_14")

        line_2 = QtWidgets.QFrame(frame)
        line_2.setGeometry(QtCore.QRect(10, 460, 551, 20))
        line_2.setFrameShape(QtWidgets.QFrame.HLine)
        line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_2.setObjectName("line_15")

        # pic = QPicture()
        # lcdNumber = QtWidgets.QLCDNumber(frame)
        # lcdNumber.setGeometry(QtCore.QRect(10, 10, 101, 81))
        # lcdNumber.setObjectName("lcdNumber_2")

        # picture = QtWidgets.QLabel(frame)
        # picture.setGeometry(QtCore.QRect(10, 10, 101, 81))
        # picture.setAlignment(Qt.AlignCenter)
        # picture.setPicture(QPicture('photo.jpg'))

    def btn_refresh(self, frame):
        _translate = QtCore.QCoreApplication.translate

        self.btn_pushButton_refresh = QtWidgets.QPushButton(frame)
        self.btn_pushButton_refresh.setGeometry(QtCore.QRect(453, 470, 101, 33))
        self.btn_pushButton_refresh.setFont(CSS.set_font(12, False, 50))
        self.btn_pushButton_refresh.setAutoFillBackground(False)
        self.btn_pushButton_refresh.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_refresh.setObjectName("btn_pushButton_order_close")
        self.btn_pushButton_refresh.setText(_translate("MainWindow", "Очистить"))
        # btn_pushButton_refresh.clicked.connect(lambda: refresh())
        #
        # def refresh():
        #     pass
        #     # txt_label_order_number.setText('0')
        #     # txt_label_order_number_prefix.setText('A')

    @classmethod
    def set_label_car(cls, frame):
        label_car_brand_and_number = QtWidgets.QLabel(frame)
        label_car_brand_and_number.setGeometry(QtCore.QRect(10, 350, 120, 30))
        label_car_brand_and_number.setFont(CSS.set_font(12, False, 50))
        label_car_brand_and_number.setAutoFillBackground(False)
        label_car_brand_and_number.setObjectName("label_car_brand_and_number")

        label_car_vin_code = QtWidgets.QLabel(frame)
        label_car_vin_code.setGeometry(QtCore.QRect(10, 430, 120, 30))
        label_car_vin_code.setFont(CSS.set_font(12, False, 50))
        label_car_vin_code.setAutoFillBackground(False)
        label_car_vin_code.setObjectName("label_car_vin_code")

        label_car_model = QtWidgets.QLabel(frame)
        label_car_model.setGeometry(QtCore.QRect(10, 390, 120, 30))
        label_car_model.setFont(CSS.set_font(12, False, 50))
        label_car_model.setAutoFillBackground(False)
        label_car_model.setObjectName("label_car_model")

        _translate = QtCore.QCoreApplication.translate

        label_car_brand_and_number.setText(_translate("MainWindow", "Машина"))
        label_car_vin_code.setText(_translate("MainWindow", "VIN-код "))
        label_car_model.setText(_translate("MainWindow", "Модель"))


class BaseClassWidget:
    """Базовый класс для создания виджета ListWidget."""

    def __int__(self):
        self.frame = QtWidgets.QFrame()
        self.size = 200
        self.text = ''
        self.listWidget_list = QtWidgets.QListWidget()
        self.spis = ['None']
        self.query = APIAxiomDB()

    def set(self, text):
        self.listWidget_list.addItem(text)

    def set_frame(self, frame):
        """Установка фрейма виджета."""
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setMaximumSize(QtCore.QSize(self.size, 16777215))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.set_body()
        return self.frame

    def set_body(self):
        """Установка элементов класса во фрейм."""
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.size, 631))
        self.gridLayoutWidget.setAutoFillBackground(False)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_listWidget = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_listWidget.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_listWidget.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_listWidget.setHorizontalSpacing(1)
        self.gridLayout_listWidget.setVerticalSpacing(1)
        self.gridLayout_listWidget.setObjectName("gridLayout_listWidget")

        self.frame_label = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_label.setMaximumSize(QtCore.QSize(self.size, 30))
        self.frame_label.setAutoFillBackground(False)
        self.frame_label.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frame_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label.setObjectName("frame_label")

        self.label_list = QtWidgets.QLabel(self.frame_label)
        self.label_list.setGeometry(QtCore.QRect(0, 0, self.size, 30))
        self.label_list.setMinimumSize(QtCore.QSize(self.size, 30))
        self.label_list.setMaximumSize(QtCore.QSize(self.size, 30))
        self.label_list.setFont(CSS.set_font(14))
        self.label_list.setAutoFillBackground(False)
        self.label_list.setStyleSheet("")
        self.label_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_list.setObjectName("label_list")

        self.frame_listWidget = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_listWidget.setAutoFillBackground(False)
        self.frame_listWidget.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.frame_listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_listWidget.setObjectName("frame_listWidget")

        self.listWidget_list = QtWidgets.QListWidget(self.frame_listWidget)
        self.listWidget_list.setGeometry(QtCore.QRect(0, 0, self.size, 557))
        self.listWidget_list.setMinimumSize(QtCore.QSize(self.size, 0))
        self.listWidget_list.setMaximumSize(QtCore.QSize(self.size, 16777215))
        self.listWidget_list.setFont(CSS.set_font())
        self.listWidget_list.setAutoFillBackground(True)
        self.listWidget_list.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.listWidget_list.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_list.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.listWidget_list.setTabKeyNavigation(True)
        self.listWidget_list.setProperty("showDropIndicator", False)
        self.listWidget_list.setAlternatingRowColors(True)
        self.listWidget_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget_list.setObjectName("listWidget_list")

        self.frame_btn = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_btn.setMinimumSize(QtCore.QSize(self.size, 30))
        self.frame_btn.setMaximumSize(QtCore.QSize(self.size, 30))
        self.frame_btn.setAutoFillBackground(False)
        self.frame_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_btn.setObjectName("frame_btn")

        self.btn_pushButton_update = QtWidgets.QPushButton(self.frame_btn)
        self.btn_pushButton_update.setGeometry(QtCore.QRect(40, 0, 117, 30))
        self.btn_pushButton_update.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_pushButton_update.setFont(CSS.set_font())
        self.btn_pushButton_update.setAutoFillBackground(False)
        self.btn_pushButton_update.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                                 "border-bottom-color: rgb(255, 255, 127);")
        self.btn_pushButton_update.setObjectName("btn_pushButton_update")

        self.gridLayout_listWidget.addWidget(self.frame_label, 0, 0, 1, 1)
        self.gridLayout_listWidget.addWidget(self.frame_listWidget, 1, 0, 1, 1)
        self.gridLayout_listWidget.addWidget(self.frame_btn, 2, 0, 1, 1)

        self.add_action()


        self.retranslateUi()

    def set_item(self, text_a):
        """Запись одного элемента в ListWidget."""
        self.listWidget_list.addItem(text_a)

    def set_items(self, list_a):
        """Запись списка элементов в ListWidget."""
        for elem in list_a:
            self.listWidget_list.addItem(str(elem))

    def clear_items(self):
        """Очистка поля ListWidget."""
        self.listWidget_list.clear()

    def add_action(self):
        """Назначение действия кнопки обновления для ListWidget."""
        self.btn_pushButton_update.clicked.connect(lambda: self.print())
        # self.listWidget_list.clicked.connect(lambda : self.get_item_text_from_list(self.listWidget_list.currentItem()))

    def get_item_text_from_list(self, item):
        pass

    def print(self):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в поле ListWidget."""
        pass

    def print_widget(self, name):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в соседствующие поля ListWidget."""
        pass

    def print_one(self, id_num: int):
        pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_list.setText(_translate("MainWindow", self.text))
        self.frame_btn.setStyleSheet(_translate("MainWindow", "background-color: rgb(85, 170, 0);"))
        self.btn_pushButton_update.setText(_translate("MainWindow", "Обновить"))