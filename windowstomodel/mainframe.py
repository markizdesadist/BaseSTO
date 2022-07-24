from PyQt5.QtWidgets import (QLabel, QFrame,  QPushButton, QListWidget)
from PyQt5.QtCore import QRect, QCoreApplication, Qt

from templateCSS import CSS

class MainFrame:
    main_frame = QFrame()
    def __int__(self, Main):

        self.listWidget_client = QListWidget(self.main_frame)
        self.listWidget_car = QListWidget(self.main_frame)
        self.listWidget_order = QListWidget(self.main_frame)
        self.pushButton_update_client = QPushButton(self.main_frame)
        self.pushButton_update_car = QPushButton(self.main_frame)
        self.pushButton_update_order = QPushButton(self.main_frame)

        self.set_body()

    def set_body(self):
        MainFrame.main_frame.setGeometry(QRect(0, 0, 1024, 600))
        MainFrame.main_frame.setFrameShape(QFrame.StyledPanel)
        MainFrame.main_frame.setFrameShadow(QFrame.Raised)
        MainFrame.main_frame.setObjectName("main_frame")



        # self.listWidget_client = QListWidget(frame)
        self.listWidget_client.setEnabled(True)
        self.listWidget_client.setGeometry(QRect(558, 30, 141, 461))
        self.listWidget_client.setFont(CSS.set_font(12))
        self.listWidget_client.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.listWidget_client.setObjectName("listWidget_client")

        # self.listWidget_car = QListWidget(frame)
        self.listWidget_car.setEnabled(True)
        self.listWidget_car.setGeometry(QRect(780, 30, 111, 461))
        self.listWidget_car.setFont(CSS.set_font(12))
        self.listWidget_car.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.listWidget_car.setObjectName("listWidget_car")

        # self.listWidget_order = QListWidget(frame)
        self.listWidget_order.setEnabled(True)
        self.listWidget_order.setGeometry(QRect(902, 30, 111, 461))
        self.listWidget_order.setFont(CSS.set_font(12))
        self.listWidget_order.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.listWidget_order.setObjectName("listWidget_order")

        # self.pushButton_update_client = QPushButton(frame)
        self.pushButton_update_client.setEnabled(True)
        self.pushButton_update_client.setGeometry(QRect(460, 495, 56, 19))
        self.pushButton_update_client.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_update_client.setObjectName("pushButton_update_client")

        # self.pushButton_update_car = QPushButton(frame)
        self.pushButton_update_car.setEnabled(True)
        self.pushButton_update_car.setGeometry(QRect(595, 495, 56, 19))
        self.pushButton_update_car.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_update_car.setObjectName("pushButton_update_car")

        # self.pushButton_update_order = QPushButton(frame)
        self.pushButton_update_order.setEnabled(True)
        self.pushButton_update_order.setGeometry(QRect(720, 495, 56, 19))
        self.pushButton_update_order.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_update_order.setObjectName("pushButton_update_order")

        self.label()
        self.retranslateUi()
        self.main_frame.show()

    def label(self, ):
        line_vfrm_1 = QFrame(self.main_frame)
        line_vfrm_1.setEnabled(True)
        line_vfrm_1.setGeometry(QRect(556, 10, 20, 481))
        line_vfrm_1.setLineWidth(2)
        line_vfrm_1.setFrameShape(QFrame.VLine)
        line_vfrm_1.setFrameShadow(QFrame.Sunken)
        line_vfrm_1.setObjectName("line_vfrm_1")

        line_vfrm_2 = QFrame(self.main_frame)
        line_vfrm_2.setEnabled(True)
        line_vfrm_2.setGeometry(QRect(676, 10, 20, 481))
        line_vfrm_2.setLineWidth(2)
        line_vfrm_2.setFrameShape(QFrame.VLine)
        line_vfrm_2.setFrameShadow(QFrame.Sunken)
        line_vfrm_2.setObjectName("line_vfrm_2")

        self.label_frame_client = QLabel(self.main_frame)
        self.label_frame_client.setEnabled(True)
        self.label_frame_client.setGeometry(QRect(427, 5, 131, 21))
        self.label_frame_client.setFont(CSS.set_font(14))
        self.label_frame_client.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_frame_client.setAlignment(Qt.AlignCenter)
        self.label_frame_client.setObjectName("label_frame_client")

        self.label_frame_car = QLabel(self.main_frame)
        self.label_frame_car.setEnabled(True)
        self.label_frame_car.setGeometry(QRect(572, 5, 108, 21))
        self.label_frame_car.setFont(CSS.set_font(14))
        self.label_frame_car.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_frame_car.setAlignment(Qt.AlignCenter)
        self.label_frame_car.setObjectName("label_frame_car")

        self.label_frame_order = QLabel(self.main_frame)
        self.label_frame_order.setEnabled(True)
        self.label_frame_order.setGeometry(QRect(692, 5, 103, 21))
        self.label_frame_order.setFont(CSS.set_font(14))
        self.label_frame_order.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_frame_order.setAlignment(Qt.AlignCenter)
        self.label_frame_order.setObjectName("label_frame_order")

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        self.label_frame_client.setText(_translate("MainWindow", "Клиент"))
        self.label_frame_car.setText(_translate("MainWindow", "Машина"))
        self.label_frame_order.setText(_translate("MainWindow", "Открытые акты"))
        self.pushButton_update_client.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_update_car.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_update_order.setText(_translate("MainWindow", "Обновить"))

