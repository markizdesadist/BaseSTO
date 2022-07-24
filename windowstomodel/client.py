from PyQt5.QtWidgets import (QLabel, QLineEdit,
                             QFrame, QTextEdit, QPushButton)
from PyQt5.QtCore import QRect, QCoreApplication
from templateCSS import CSS


class Client:
    def __int__(self):
        self.pushButton_save_client = QPushButton()
        self.textEdit_client_full_name_txt = QTextEdit()
        self.textEdit_client_address_txt = QTextEdit()
        self.lineEdit_client_name_txt = QLineEdit()
        self.lineEdit_client_phone_txt = QLineEdit()
        self.lineEdit_client_mobile_txt = QLineEdit()

    def set_body(self, frame):
        self.pushButton_save_client = QPushButton(frame)
        self.pushButton_save_client.setEnabled(True)
        self.pushButton_save_client.setGeometry(QRect(320, 380, 81, 51))
        self.pushButton_save_client.setFont(CSS.set_font(12))
        self.pushButton_save_client.setStyleSheet("background-color: rgb(205, 205, 205);")
        self.pushButton_save_client.setObjectName("pushButton_save_client")

        self.textEdit_client_full_name_txt = QTextEdit(frame)
        self.textEdit_client_full_name_txt.setEnabled(True)
        self.textEdit_client_full_name_txt.setGeometry(QRect(120, 110, 281, 51))
        self.textEdit_client_full_name_txt.setObjectName("textEdit_client_full_name_txt")

        self.textEdit_client_address_txt = QTextEdit(frame)
        self.textEdit_client_address_txt.setEnabled(True)
        self.textEdit_client_address_txt.setGeometry(QRect(120, 170, 281, 51))
        self.textEdit_client_address_txt.setObjectName("textEdit_client_address_txt")

        self.lineEdit_client_name_txt = QLineEdit(frame)
        self.lineEdit_client_name_txt.setEnabled(True)
        self.lineEdit_client_name_txt.setGeometry(QRect(120, 80, 281, 21))
        self.lineEdit_client_name_txt.setObjectName("lineEdit_client_name_txt")

        self.lineEdit_client_unp = QLineEdit(frame)
        self.lineEdit_client_unp.setEnabled(True)
        self.lineEdit_client_unp.setGeometry(QRect(120, 240, 281, 21))
        self.lineEdit_client_unp.setObjectName("lineEdit_client_unp")

        self.lineEdit_client_phone_txt = QLineEdit(frame)
        self.lineEdit_client_phone_txt.setEnabled(True)
        self.lineEdit_client_phone_txt.setGeometry(QRect(120, 270, 281, 21))
        self.lineEdit_client_phone_txt.setObjectName("lineEdit_client_phone_txt")

        self.lineEdit_client_mobile_txt = QLineEdit(frame)
        self.lineEdit_client_mobile_txt.setEnabled(True)
        self.lineEdit_client_mobile_txt.setGeometry(QRect(120, 300, 281, 21))
        self.lineEdit_client_mobile_txt.setObjectName("lineEdit_client_mobile_txt")

        self.label(frame)
        self.retranslateUi()
        frame.show()

    def label(self, frame):
        line_hclt_1 = QFrame(frame)
        line_hclt_1.setEnabled(True)
        line_hclt_1.setGeometry(QRect(10, 0, 390, 16))
        line_hclt_1.setLineWidth(2)
        line_hclt_1.setFrameShape(QFrame.HLine)
        line_hclt_1.setFrameShadow(QFrame.Sunken)
        line_hclt_1.setObjectName("line_hclt_1")

        line_hclt_2 = QFrame(frame)
        line_hclt_2.setEnabled(True)
        line_hclt_2.setGeometry(QRect(10, 50, 390, 16))
        line_hclt_2.setFrameShape(QFrame.HLine)
        line_hclt_2.setFrameShadow(QFrame.Sunken)
        line_hclt_2.setObjectName("line_hclt_2")

        line_hclt_4 = QFrame(frame)
        line_hclt_4.setEnabled(True)
        line_hclt_4.setGeometry(QRect(10, 330, 390, 16))
        line_hclt_4.setFrameShape(QFrame.HLine)
        line_hclt_4.setFrameShadow(QFrame.Sunken)
        line_hclt_4.setObjectName("line_hclt_4")

        line_vclt_1 = QFrame(frame)
        line_vclt_1.setEnabled(True)
        line_vclt_1.setGeometry(QRect(400, 10, 20, 451))
        line_vclt_1.setLineWidth(2)
        line_vclt_1.setFrameShape(QFrame.VLine)
        line_vclt_1.setFrameShadow(QFrame.Sunken)
        line_vclt_1.setObjectName("line_vclt_1")

        self.label_client_name_clt = QLabel(frame)
        self.label_client_name_clt.setEnabled(True)
        self.label_client_name_clt.setGeometry(QRect(10, 80, 105, 20))
        self.label_client_name_clt.setFont(CSS.set_font(12, True, 75))
        self.label_client_name_clt.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_name_clt.setObjectName("label_client_name_clt")

        self.label_client_name = QLabel(frame)
        self.label_client_name.setEnabled(True)
        self.label_client_name.setGeometry(QRect(10, 170, 105, 20))
        self.label_client_name.setFont(CSS.set_font(12, True, 75))
        self.label_client_name.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_name.setObjectName("label_client_name")

        self.label_client_full_name = QLabel(frame)
        self.label_client_full_name.setEnabled(True)
        self.label_client_full_name.setGeometry(QRect(10, 110, 105, 20))
        self.label_client_full_name.setFont(CSS.set_font(12, True, 75))
        self.label_client_full_name.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_full_name.setObjectName("label_client_full_name")

        self.label_client_address = QLabel(frame)
        self.label_client_address.setEnabled(True)
        self.label_client_address.setGeometry(QRect(10, 170, 105, 20))
        self.label_client_address.setFont(CSS.set_font(12, True, 75))
        self.label_client_address.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_address.setObjectName("label_client_address")

        self.label_client_unp = QLabel(frame)
        self.label_client_unp.setEnabled(True)
        self.label_client_unp.setGeometry(QRect(10, 240, 105, 20))
        self.label_client_unp.setFont(CSS.set_font(12, True, 75))
        self.label_client_unp.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_unp.setObjectName("label_client_unp")

        self.label_client_phone = QLabel(frame)
        self.label_client_phone.setEnabled(True)
        self.label_client_phone.setGeometry(QRect(10, 270, 105, 20))
        self.label_client_phone.setFont(CSS.set_font(12, True, 75))
        self.label_client_phone.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_phone.setObjectName("label_client_phone")

        self.label_client_mobile = QLabel(frame)
        self.label_client_mobile.setEnabled(True)
        self.label_client_mobile.setGeometry(QRect(10, 300, 105, 20))
        self.label_client_mobile.setFont(CSS.set_font(12, True, 75))
        self.label_client_mobile.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.label_client_mobile.setObjectName("label_client_mobile")

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        self.label_client_name_clt.setText(_translate("MainWindow", "Клиент"))
        self.pushButton_save_client.setText(_translate("MainWindow", "Save"))
        self.label_client_full_name.setText(_translate("MainWindow", "Полное название"))
        self.label_client_name.setText(_translate("MainWindow", "Клиент"))
        self.label_client_address.setText(_translate("MainWindow", "Адрес"))
        self.label_client_unp.setText(_translate("MainWindow", "УНП"))
        self.label_client_phone.setText(_translate("MainWindow", "Телефон"))
        self.label_client_mobile.setText(_translate("MainWindow", "Телефон мобильный"))

