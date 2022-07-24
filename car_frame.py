from PyQt5 import QtCore, QtWidgets
from CSS_template import CSS
from dbapi import APIAxiomDB
from databasecreate import CreateDB


class Car:
    def __int__(self):
        self.frame = QtWidgets.QFrame()
        self.current_id = None

    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 593))
        self.frame.setMinimumSize(QtCore.QSize(571, 593))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")        
        
        self.set_label()
        self.set_body()

        self.retranslateUi()

        self.add_action()

    def add_action(self):
        self.btn_pushButton_save.clicked.connect(lambda: self.save_new_car())
        self.btn_pushButton_edit.clicked.connect(lambda: self.edit_car())

    def edit_car(self):
        edit = CreateDB()
        try:
            edit.update_car(
                id=self.current_id,
                name=self.txt_edit_lineEdit_car_brand.text(),
                model=self.txt_edit_lineEdit_car_model.text(),
                number=self.txt_edit_lineEdit_car_number.text(),
                vin_code=self.txt_edit_lineEdit_car_vin_code.text()
            )
        except Exception as err:
            print(err)


    def save_new_car(self):
        new = CreateDB()
        client = APIAxiomDB()
        temp = client.get_client_from_unp(int(self.txt_label_client_identification_number.text()))
        try:
            new.car_create(
                name=self.txt_edit_lineEdit_car_brand.text(),
                model=self.txt_edit_lineEdit_car_model.text(),
                number=self.txt_edit_lineEdit_car_number.text(),
                vin_code=self.txt_edit_lineEdit_car_vin_code.text(),
                company_id=temp.id
            )
        except ValueError as err:
            print(err)
        except Exception as err:
            print(err)
        
    def set_body(self):
        self.btn_pushButton_new_client = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_new_client.setGeometry(QtCore.QRect(468, 110, 85, 71))
        self.btn_pushButton_new_client.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_new_client.setObjectName("btn_pushButton_new_client")

        self.btn_pushButton_car_part_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_car_part_choice.setGeometry(QtCore.QRect(225, 310, 85, 33))
        self.btn_pushButton_car_part_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_car_part_choice.setObjectName("btn_pushButton_car_part_choice")

        self.btn_pushButton_car_car_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_car_car_choice.setGeometry(QtCore.QRect(128, 310, 85, 33))
        self.btn_pushButton_car_car_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_car_car_choice.setObjectName("btn_pushButton_car_car_choice")

        self.btn_pushButton_save = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_save.setGeometry(QtCore.QRect(468, 520, 85, 71))
        self.btn_pushButton_save.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_save.setObjectName("btn_pushButton_save")

        self.btn_pushButton_edit = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_edit.setGeometry(QtCore.QRect(468, 350, 85, 71))
        self.btn_pushButton_edit.setAutoFillBackground(False)
        self.btn_pushButton_edit.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_edit.setObjectName("btn_pushButton_new_car")

        self.txt_label_client_name = QtWidgets.QLabel(self.frame)
        self.txt_label_client_name.setGeometry(QtCore.QRect(128, 110, 331, 30))
        self.txt_label_client_name.setFont(CSS.set_font(12, False, 50))
        self.txt_label_client_name.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_client_name.setObjectName("txt_label_client_name")

        self.txt_label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.txt_label_client_identification_number.setGeometry(QtCore.QRect(128, 150, 331, 30))
        self.txt_label_client_identification_number.setFont(CSS.set_font(12, False, 50))
        self.txt_label_client_identification_number.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_client_identification_number.setObjectName("txt_label_client_identification_number")

        self.txt_edit_lineEdit_car_brand = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_car_brand.setGeometry(QtCore.QRect(128, 350, 181, 31))
        self.txt_edit_lineEdit_car_brand.setFont(CSS.set_font())
        self.txt_edit_lineEdit_car_brand.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_car_brand.setObjectName("txt_edit_lineEdit_car_brand")

        self.txt_edit_lineEdit_car_number = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_car_number.setGeometry(QtCore.QRect(318, 350, 141, 31))
        self.txt_edit_lineEdit_car_number.setFont(CSS.set_font())
        self.txt_edit_lineEdit_car_number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_car_number.setObjectName("txt_edit_lineEdit_car_number")

        self.txt_edit_lineEdit_car_model = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_car_model.setGeometry(QtCore.QRect(128, 390, 331, 31))
        self.txt_edit_lineEdit_car_model.setFont(CSS.set_font())
        self.txt_edit_lineEdit_car_model.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_car_model.setObjectName("txt_edit_lineEdit_car_model")

        self.txt_edit_lineEdit_car_vin_code = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_car_vin_code.setGeometry(QtCore.QRect(128, 430, 425, 31))
        self.txt_edit_lineEdit_car_vin_code.setFont(CSS.set_font())
        self.txt_edit_lineEdit_car_vin_code.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_car_vin_code.setObjectName("txt_edit_lineEdit_car_vin_code")
        
    def set_label(self):
        self.label_car_brand_and_number = QtWidgets.QLabel(self.frame)
        self.label_car_brand_and_number.setGeometry(QtCore.QRect(10, 350, 120, 30))
        self.label_car_brand_and_number.setFont(CSS.set_font(12, False, 50))
        self.label_car_brand_and_number.setObjectName("label_car_brand_and_number")

        self.label_car_vin_code = QtWidgets.QLabel(self.frame)
        self.label_car_vin_code.setGeometry(QtCore.QRect(10, 430, 120, 30))
        self.label_car_vin_code.setFont(CSS.set_font(12, False, 50))
        self.label_car_vin_code.setObjectName("label_car_vin_code")

        self.label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.label_client_identification_number.setGeometry(QtCore.QRect(10, 150, 120, 30))
        self.label_client_identification_number.setFont(CSS.set_font(12, False, 50))
        self.label_client_identification_number.setObjectName("label_client_identification_number")

        self.label_car_model = QtWidgets.QLabel(self.frame)
        self.label_car_model.setGeometry(QtCore.QRect(10, 390, 120, 30))
        self.label_car_model.setFont(CSS.set_font(12, False, 50))
        self.label_car_model.setObjectName("label_car_model")

        self.label_client_name = QtWidgets.QLabel(self.frame)
        self.label_client_name.setGeometry(QtCore.QRect(10, 110, 120, 30))
        self.label_client_name.setFont(CSS.set_font(12, False, 50))
        self.label_client_name.setObjectName("label_client_name")

        CSS.line_tab(self.frame)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.btn_pushButton_new_client.setText(_translate("MainWindow", "Новый\n"
                                                                          "клиент"))
        self.label_car_brand_and_number.setText(_translate("MainWindow", "Машина"))
        self.label_car_vin_code.setText(_translate("MainWindow", "VIN-код "))
        self.label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
        self.btn_pushButton_car_part_choice.setText(_translate("MainWindow", "Запчасти"))
        self.label_client_name.setText(_translate("MainWindow", "Клиент"))
        self.btn_pushButton_car_car_choice.setText(_translate("MainWindow", "Машина"))
        self.btn_pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.txt_label_client_name.setText(_translate("MainWindow", "Владелец машины"))
        self.label_car_model.setText(_translate("MainWindow", "Модель"))
        self.txt_label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
        self.txt_edit_lineEdit_car_brand.setText(_translate("MainWindow", "марка машины"))
        self.txt_edit_lineEdit_car_number.setText(_translate("MainWindow", "Номер машины"))
        self.txt_edit_lineEdit_car_model.setText(_translate("MainWindow", "модель машины"))
        self.txt_edit_lineEdit_car_vin_code.setText(_translate("MainWindow", "VIN код машины"))
        self.btn_pushButton_edit.setText(_translate("MainWindow", "Редакти\nровать\nданные\nмашины"))
