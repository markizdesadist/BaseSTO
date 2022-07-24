from PyQt5.QtWidgets import (QLabel, QLineEdit,
                             QFrame, QPushButton)
from PyQt5.QtCore import QRect, QCoreApplication
from templateCSS import CSS


class Car:
    # pushButton_new_client = QPushButton()
    def __int__(self):
        self.pushButton_new_client = QPushButton()
        self.pushButton_save_car = QPushButton()
        self.lineEdit_car_brand = QLineEdit()
        self.lineEdit_car_number = QLineEdit()
        self.lineEdit_car_uzm = QLineEdit()
        self.label_client_full_name_txt = QLabel()
        self.label_client_name_txt = QLabel()

    def set_body(self, frame):
        self.label_client_full_name_txt = QLabel(frame)
        self.label_client_full_name_txt.setEnabled(True)
        self.label_client_full_name_txt.setGeometry(QRect(120, 110, 241, 20))
        self.label_client_full_name_txt.setFont(CSS.set_font(12, True, 75))
        self.label_client_full_name_txt.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_full_name_txt.setObjectName("label_client_full_name_txt")

        self.label_client_name_txt = QLabel(frame)
        self.label_client_name_txt.setEnabled(True)
        self.label_client_name_txt.setGeometry(QRect(120, 80, 241, 20))
        self.label_client_name_txt.setFont(CSS.set_font(12, True, 75))
        self.label_client_name_txt.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_name_txt.setObjectName("label_client_name_txt")

        self.pushButton_new_client = QPushButton(frame)
        self.pushButton_new_client.setEnabled(True)
        self.pushButton_new_client.setGeometry(QRect(365, 80, 36, 51))
        self.pushButton_new_client.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_new_client.setObjectName("pushButton_new_client")

        self.pushButton_save_car = QPushButton(frame)
        self.pushButton_save_car.setEnabled(True)
        self.pushButton_save_car.setGeometry(QRect(320, 380, 81, 51))
        self.pushButton_save_car.setFont(CSS.set_font(12))
        self.pushButton_save_car.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_save_car.setObjectName("pushButton_save_car")

        self.lineEdit_car_brand = QLineEdit(frame)
        self.lineEdit_car_brand.setEnabled(True)
        self.lineEdit_car_brand.setGeometry(QRect(120, 240, 151, 20))
        self.lineEdit_car_brand.setObjectName("lineEdit_car_brand")

        self.lineEdit_car_number = QLineEdit(frame)
        self.lineEdit_car_number.setEnabled(True)
        self.lineEdit_car_number.setGeometry(QRect(280, 240, 121, 20))
        self.lineEdit_car_number.setObjectName("lineEdit_car_number")

        self.lineEdit_car_model = QLineEdit(frame)
        self.lineEdit_car_model.setEnabled(True)
        self.lineEdit_car_model.setGeometry(QRect(120, 270, 281, 20))
        self.lineEdit_car_model.setObjectName("lineEdit_car_model")

        self.lineEdit_car_uzm = QLineEdit(frame)
        self.lineEdit_car_uzm.setEnabled(True)
        self.lineEdit_car_uzm.setGeometry(QRect(120, 300, 281, 20))
        self.lineEdit_car_uzm.setObjectName("lineEdit_car_uzm")

        self.label(frame)
        self.retranslateUi()
        frame.show()

    def label(self, frame):
        line_hcar_1 = QFrame(frame)
        line_hcar_1.setEnabled(True)
        line_hcar_1.setGeometry(QRect(10, 0, 390, 16))
        line_hcar_1.setLineWidth(2)
        line_hcar_1.setFrameShape(QFrame.HLine)
        line_hcar_1.setFrameShadow(QFrame.Sunken)
        line_hcar_1.setObjectName("line_hcar_1")

        line_hcar_2 = QFrame(frame)
        line_hcar_2.setEnabled(True)
        line_hcar_2.setGeometry(QRect(10, 50, 390, 16))
        line_hcar_2.setFrameShape(QFrame.HLine)
        line_hcar_2.setFrameShadow(QFrame.Sunken)
        line_hcar_2.setObjectName("line_hcar_2")

        line_hcar_3 = QFrame(frame)
        line_hcar_3.setEnabled(True)
        line_hcar_3.setGeometry(QRect(10, 190, 390, 16))
        line_hcar_3.setFrameShape(QFrame.HLine)
        line_hcar_3.setFrameShadow(QFrame.Sunken)
        line_hcar_3.setObjectName("line_hcar_3")

        line_hcar_4 = QFrame(frame)
        line_hcar_4.setEnabled(True)
        line_hcar_4.setGeometry(QRect(10, 330, 390, 16))
        line_hcar_4.setFrameShape(QFrame.HLine)
        line_hcar_4.setFrameShadow(QFrame.Sunken)
        line_hcar_4.setObjectName("line_hcar_4")

        line_vcar_1 = QFrame(frame)
        line_vcar_1.setEnabled(True)
        line_vcar_1.setGeometry(QRect(400, 10, 20, 451))
        line_vcar_1.setLineWidth(2)
        line_vcar_1.setFrameShape(QFrame.VLine)
        line_vcar_1.setFrameShadow(QFrame.Sunken)
        line_vcar_1.setObjectName("line_vcar_1")

        self.label_client_name = QLabel(frame)
        self.label_client_name.setEnabled(True)
        self.label_client_name.setGeometry(QRect(10, 80, 105, 20))
        self.label_client_name.setFont(CSS.set_font(12, True, 75))
        self.label_client_name.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_name.setObjectName("label_client_name")

        self.label_client_full_name = QLabel(frame)
        self.label_client_full_name.setEnabled(True)
        self.label_client_full_name.setGeometry(QRect(10, 110, 105, 20))
        self.label_client_full_name.setFont(CSS.set_font(12, True, 75))
        self.label_client_full_name.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_full_name.setObjectName("label_client_full_name")

        self.label_car_brand_number = QLabel(frame)
        self.label_car_brand_number.setEnabled(True)
        self.label_car_brand_number.setGeometry(QRect(10, 240, 105, 20))
        self.label_car_brand_number.setFont(CSS.set_font(12, True, 75))
        self.label_car_brand_number.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_car_brand_number.setObjectName("label_car_brand_number")

        self.label_vin_code = QLabel(frame)
        self.label_vin_code.setEnabled(True)
        self.label_vin_code.setGeometry(QRect(10, 300, 105, 20))
        self.label_vin_code.setFont(CSS.set_font(12, True, 75))
        self.label_vin_code.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_vin_code.setObjectName("label_vin_code")

        self.label_model = QLabel(frame)
        self.label_model.setEnabled(True)
        self.label_model.setGeometry(QRect(10, 270, 105, 20))
        self.label_model.setFont(CSS.set_font(12, True, 75))
        self.label_model.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_model.setObjectName("label_model")

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        self.label_client_full_name_txt.setText(_translate("MainWindow", "полное название компании"))
        self.label_client_full_name.setText(_translate("MainWindow", "Полное название"))
        self.label_client_name_txt.setText(_translate("MainWindow", "краткое название компании"))
        self.label_client_name.setText(_translate("MainWindow", "Клиент"))
        self.label_model.setText(_translate("MainWindow", "Car number"))
        self.pushButton_save_car.setText(_translate("MainWindow", "Save"))
        self.label_vin_code.setText(_translate("MainWindow", "UZM number"))
        self.label_car_brand_number.setText(_translate("MainWindow", "Car model"))
        self.pushButton_new_client.setText(_translate("MainWindow", "Новый\n"
                                                                    "клиент"))