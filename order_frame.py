from PyQt5 import QtWidgets, QtCore
from CSS_template import CSS
from datetime import datetime
from dbapi import APIAxiomDB


class Order:
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
                
                self.set_body()
        
        def set_body(self):
                self.txt_edit_lineEdit_client_owner_name = QtWidgets.QLineEdit(self.frame)
                self.txt_edit_lineEdit_client_owner_name.setGeometry(QtCore.QRect(128, 190, 425, 31))
                self.txt_edit_lineEdit_client_owner_name.setAutoFillBackground(True)
                self.txt_edit_lineEdit_client_owner_name.setClearButtonEnabled(True)
                self.txt_edit_lineEdit_client_owner_name.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.txt_edit_lineEdit_client_owner_name.setObjectName("txt_edit_lineEdit_client_owner_name")


                self.txt_label_order_number = QtWidgets.QLabel(self.frame)
                self.txt_label_order_number.setGeometry(QtCore.QRect(228, 48, 96, 30))
                self.txt_label_order_number.setFont(CSS.set_font(14, True, 75))
                self.txt_label_order_number.setAutoFillBackground(False)
                self.txt_label_order_number.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_order_number.setAlignment(
                        QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                self.txt_label_order_number.setObjectName("txt_label_order_number")
                self.txt_label_order_number.setIndent(10)

                self.txt_label_car_brand = QtWidgets.QLabel(self.frame)
                self.txt_label_car_brand.setGeometry(QtCore.QRect(128, 350, 181, 30))
                self.txt_label_car_brand.setFont(CSS.set_font(12, False, 50))
                self.txt_label_car_brand.setAutoFillBackground(False)
                self.txt_label_car_brand.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_car_brand.setObjectName("txt_label_car_brand")
                self.txt_label_car_brand.setIndent(10)

                self.txt_label_car_number = QtWidgets.QLabel(self.frame)
                self.txt_label_car_number.setGeometry(QtCore.QRect(318, 350, 141, 30))
                self.txt_label_car_number.setFont(CSS.set_font(12, False, 50))
                self.txt_label_car_number.setAutoFillBackground(False)
                self.txt_label_car_number.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_car_number.setObjectName("txt_label_car_number")
                self.txt_label_car_number.setIndent(10)
                
                self.txt_label_order_number_prefix = QtWidgets.QLabel(self.frame)
                self.txt_label_order_number_prefix.setGeometry(QtCore.QRect(358, 48, 31, 30))
                self.txt_label_order_number_prefix.setFont(CSS.set_font(14, True, 75))
                self.txt_label_order_number_prefix.setAutoFillBackground(False)
                self.txt_label_order_number_prefix.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_order_number_prefix.setAlignment(QtCore.Qt.AlignCenter)
                self.txt_label_order_number_prefix.setObjectName("txt_label_order_number_prefix")
                
                self.txt_label_client_name = QtWidgets.QLabel(self.frame)
                self.txt_label_client_name.setGeometry(QtCore.QRect(128, 110, 331, 30))
                self.txt_label_client_name.setFont(CSS.set_font(12, False, 50))
                self.txt_label_client_name.setAutoFillBackground(True)
                self.txt_label_client_name.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_client_name.setObjectName("txt_label_client_name")
                self.txt_label_client_name.setIndent(10)
                
                self.txt_label_car_model = QtWidgets.QLabel(self.frame)
                self.txt_label_car_model.setGeometry(QtCore.QRect(128, 390, 331, 30))
                self.txt_label_car_model.setFont(CSS.set_font(12, False, 50))
                self.txt_label_car_model.setAutoFillBackground(False)
                self.txt_label_car_model.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_car_model.setObjectName("txt_label_car_model")
                self.txt_label_car_model.setIndent(10)
                
                self.txt_edit_lineEdit_client_job_title = QtWidgets.QLineEdit(self.frame)
                self.txt_edit_lineEdit_client_job_title.setGeometry(QtCore.QRect(128, 150, 333, 31))
                self.txt_edit_lineEdit_client_job_title.setAutoFillBackground(True)
                self.txt_edit_lineEdit_client_job_title.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.txt_edit_lineEdit_client_job_title.setObjectName("txt_edit_lineEdit_client_job_title")

                
                self.txt_label_car_vin_code = QtWidgets.QLabel(self.frame)
                self.txt_label_car_vin_code.setGeometry(QtCore.QRect(128, 430, 425, 30))
                self.txt_label_car_vin_code.setFont(CSS.set_font(12, False, 50))
                self.txt_label_car_vin_code.setAutoFillBackground(False)
                self.txt_label_car_vin_code.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_car_vin_code.setObjectName("txt_label_car_vin_code")
                self.txt_label_car_vin_code.setIndent(10)
                
                self.txt_label_client_identification_number = QtWidgets.QLabel(self.frame)
                self.txt_label_client_identification_number.setGeometry(QtCore.QRect(128, 230, 425, 30))
                self.txt_label_client_identification_number.setFont(CSS.set_font(12, False, 50))
                self.txt_label_client_identification_number.setAutoFillBackground(True)
                self.txt_label_client_identification_number.setStyleSheet("background-color: rgb(221, 221, 221);")
                self.txt_label_client_identification_number.setObjectName("txt_label_client_identification_number")
                self.txt_label_client_identification_number.setIndent(10)

                self.set_btn()
                self.set_checkBox()
                self.set_datetime()
                self.set_label()
                self.add_action()

                self.retranslateUi()

        def clear_txt(self, txt):
                txt.clear()

        def add_action(self):
                self.btn_pushButton_car_part_choice.clicked.connect(lambda: self.part_choice())
                self.btn_pushButton_car_car_choice.clicked.connect(lambda: self.car_choice())
                self.btn_pushButton_refresh.clicked.connect(lambda: self.refresh())
                self.btn_pushButton_print_order.clicked.connect(lambda: self.print())

                # self.txt_edit_lineEdit_client_owner_name.mousePressEvent(
                #         self.txt_edit_lineEdit_client_owner_name)

        def print(self):
                if self.current_id:
                        pass

                # dict_order = {
                #         'car_id':car_id
                #         'company_id':company_id,
                #         'prefix':prefix,
                #         'data':data,
                #         'closing_mark':closing_mark,
                #         'first_open':first_open,
                #         'data_close':data_close,
                #         'path_file':path,
                #         'driver_name':driver_name,
                #         'driver_job':driver_job
                # }


        def refresh(self):
                temp = APIAxiomDB()
                self.txt_label_order_number.setText(str(temp.count_act() + 1))
                self.txt_label_order_number_prefix.setText('A')
                self.current_id = None

        def part_choice(self):
                """Действие, при нажатии кнопки 'Запчасти'."""

                self.txt_label_car_brand.setText('Запчасти')
                self.txt_label_car_number.setText('Запчасти')
                self.txt_label_car_model.setText('Запчасти')
                self.txt_label_car_vin_code.setText('Запчасти')
                self.btn_pushButton_car_part_choice.setDown(True)

                self.btn_pushButton_car_part_choice.setStyleSheet("background-color: rgb(199, 170, 199);")
                self.btn_pushButton_car_car_choice.setStyleSheet("background-color: rgb(85, 170, 0);")

        def car_choice(self):
                """Действие, при нажатии кнопки 'Машина'."""
                temp = APIAxiomDB()
                try:
                        if self.current_id:
                                temp_car = temp.get_car_from_order(self.current_id)
                                self.txt_label_car_brand.setText(temp_car.name)
                                self.txt_label_car_number.setText(temp_car.number)
                                self.txt_label_car_model.setText(temp_car.model)
                                self.txt_label_car_vin_code.setText(temp_car.vin_code)
                        else:
                                self.txt_label_car_brand.setText('Машина')
                                self.txt_label_car_number.setText('Номер')
                                self.txt_label_car_model.setText('Модель')
                                self.txt_label_car_vin_code.setText('VIN код')
                        self.btn_pushButton_car_part_choice.setDown(True)

                        self.btn_pushButton_car_part_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
                        self.btn_pushButton_car_car_choice.setStyleSheet("background-color: rgb(199, 170, 199);")
                except Exception as err:
                        print(err)

        def get_fields_car(self):
                pass

        def set_btn(self):
                self.btn_pushButton_refresh = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_refresh.setGeometry(QtCore.QRect(453, 480, 101, 33))
                self.btn_pushButton_refresh.setFont(CSS.set_font(12, False, 50))
                self.btn_pushButton_refresh.setAutoFillBackground(False)
                self.btn_pushButton_refresh.setStyleSheet("background-color: rgb(85, 170, 0);")
                self.btn_pushButton_refresh.setObjectName("btn_pushButton_order_close")

                self.btn_pushButton_new_client = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_new_client.setGeometry(QtCore.QRect(468, 110, 85, 71))
                self.btn_pushButton_new_client.setAutoFillBackground(False)
                self.btn_pushButton_new_client.setStyleSheet("background-color: rgb(85, 170, 0);")
                self.btn_pushButton_new_client.setObjectName("btn_pushButton_new_client")

                self.btn_pushButton_car_part_choice = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_car_part_choice.setGeometry(QtCore.QRect(225, 310, 85, 33))
                self.btn_pushButton_car_part_choice.setAutoFillBackground(False)
                self.btn_pushButton_car_part_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
                self.btn_pushButton_car_part_choice.setObjectName("btn_pushButton_car_part_choice")

                self.btn_pushButton_order_close = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_order_close.setGeometry(QtCore.QRect(453, 50, 101, 33))
                self.btn_pushButton_order_close.setFont(CSS.set_font(12, False, 50))
                self.btn_pushButton_order_close.setAutoFillBackground(False)
                self.btn_pushButton_order_close.setStyleSheet("background-color: rgb(255, 170, 0);")
                self.btn_pushButton_order_close.setObjectName("btn_pushButton_order_close")

                self.btn_pushButton_car_car_choice = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_car_car_choice.setGeometry(QtCore.QRect(128, 310, 85, 33))
                self.btn_pushButton_car_car_choice.setAutoFillBackground(False)
                self.btn_pushButton_car_car_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
                self.btn_pushButton_car_car_choice.setObjectName("btn_pushButton_car_car_choice")

                self.btn_pushButton_new_car = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_new_car.setGeometry(QtCore.QRect(468, 350, 85, 71))
                self.btn_pushButton_new_car.setAutoFillBackground(False)
                self.btn_pushButton_new_car.setStyleSheet("background-color: rgb(85, 170, 0);")
                self.btn_pushButton_new_car.setObjectName("btn_pushButton_new_car")

                self.btn_pushButton_print_order = QtWidgets.QPushButton(self.frame)
                self.btn_pushButton_print_order.setGeometry(QtCore.QRect(468, 520, 85, 71))
                self.btn_pushButton_print_order.setAutoFillBackground(False)
                self.btn_pushButton_print_order.setStyleSheet("background-color: rgb(85, 170, 0);")
                self.btn_pushButton_print_order.setObjectName("btn_pushButton_print_order")

        def set_checkBox(self):
                self.checkBox_1_repair_request = QtWidgets.QCheckBox(self.frame)
                self.checkBox_1_repair_request.setGeometry(QtCore.QRect(100, 480, 300, 21))
                self.checkBox_1_repair_request.setAutoFillBackground(False)
                self.checkBox_1_repair_request.setChecked(True)
                self.checkBox_1_repair_request.setObjectName("checkBox_1_repair_request")

                self.checkBox_2_application_order = QtWidgets.QCheckBox(self.frame)
                self.checkBox_2_application_order.setGeometry(QtCore.QRect(100, 510, 300, 21))
                self.checkBox_2_application_order.setAutoFillBackground(False)
                self.checkBox_2_application_order.setChecked(True)
                self.checkBox_2_application_order.setObjectName("checkBox_2_application_order")

                self.checkBox_3_act_of_acceptance = QtWidgets.QCheckBox(self.frame)
                self.checkBox_3_act_of_acceptance.setGeometry(QtCore.QRect(100, 540, 300, 21))
                self.checkBox_3_act_of_acceptance.setAutoFillBackground(False)
                self.checkBox_3_act_of_acceptance.setChecked(True)
                self.checkBox_3_act_of_acceptance.setObjectName("checkBox_3_act_of_acceptance")

                self.checkBox_4_internal_consumption = QtWidgets.QCheckBox(self.frame)
                self.checkBox_4_internal_consumption.setGeometry(QtCore.QRect(100, 570, 300, 21))
                self.checkBox_4_internal_consumption.setAutoFillBackground(False)
                self.checkBox_4_internal_consumption.setChecked(True)
                self.checkBox_4_internal_consumption.setObjectName("checkBox_4_internal_consumption")

        def set_datetime(self):
                self.frame_data = QtWidgets.QFrame(self.frame)
                self.frame_data.setGeometry(QtCore.QRect(130, 0, 421, 51))
                self.frame_data.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_data.setFrameShadow(QtWidgets.QFrame.Plain)
                self.frame_data.setObjectName("frame_data")

                self.dateEdit = QtWidgets.QDateEdit(self.frame_data)
                self.dateEdit.setGeometry(QtCore.QRect(80, 10, 241, 37))
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
                self.dateEdit.setDate(datetime.now())
                self.dateEdit.setObjectName("dateEdit")

        def set_label(self):
                self.label_car_brand_and_number = QtWidgets.QLabel(self.frame)
                self.label_car_brand_and_number.setGeometry(QtCore.QRect(10, 350, 120, 30))
                self.label_car_brand_and_number.setFont(CSS.set_font(12, False, 50))
                self.label_car_brand_and_number.setAutoFillBackground(False)
                self.label_car_brand_and_number.setObjectName("label_car_brand_and_number")

                self.label_car_vin_code = QtWidgets.QLabel(self.frame)
                self.label_car_vin_code.setGeometry(QtCore.QRect(10, 430, 120, 30))
                self.label_car_vin_code.setFont(CSS.set_font(12, False, 50))
                self.label_car_vin_code.setAutoFillBackground(False)
                self.label_car_vin_code.setObjectName("label_car_vin_code")

                self.label_client_job_title = QtWidgets.QLabel(self.frame)
                self.label_client_job_title.setGeometry(QtCore.QRect(10, 150, 120, 30))
                self.label_client_job_title.setFont(CSS.set_font(12, False, 50))
                self.label_client_job_title.setAutoFillBackground(False)
                self.label_client_job_title.setObjectName("label_client_job_title")

                self.label_client_name = QtWidgets.QLabel(self.frame)
                self.label_client_name.setGeometry(QtCore.QRect(10, 110, 120, 30))
                self.label_client_name.setFont(CSS.set_font(12, False, 50))
                self.label_client_name.setAutoFillBackground(False)
                self.label_client_name.setObjectName("label_client_name")

                self.label_client_owner_name = QtWidgets.QLabel(self.frame)
                self.label_client_owner_name.setGeometry(QtCore.QRect(10, 190, 120, 30))
                self.label_client_owner_name.setFont(CSS.set_font(12, False, 50))
                self.label_client_owner_name.setAutoFillBackground(False)
                self.label_client_owner_name.setObjectName("label_client_owner_name")

                self.label_order_number = QtWidgets.QLabel(self.frame)
                self.label_order_number.setGeometry(QtCore.QRect(128, 48, 101, 30))
                self.label_order_number.setFont(CSS.set_font(14, True, 75))
                self.label_order_number.setAutoFillBackground(False)
                self.label_order_number.setObjectName("label_order_number")

                self.label_car_model = QtWidgets.QLabel(self.frame)
                self.label_car_model.setGeometry(QtCore.QRect(10, 390, 120, 30))
                self.label_car_model.setFont(CSS.set_font(12, False, 50))
                self.label_car_model.setAutoFillBackground(False)
                self.label_car_model.setObjectName("label_car_model")

                self.label_order_number_sep = QtWidgets.QLabel(self.frame)
                self.label_order_number_sep.setGeometry(QtCore.QRect(333, 48, 16, 30))
                self.label_order_number_sep.setFont(CSS.set_font(14, True, 75))
                self.label_order_number_sep.setAutoFillBackground(False)
                self.label_order_number_sep.setAlignment(QtCore.Qt.AlignCenter)
                self.label_order_number_sep.setObjectName("label_order_number_sep")

                self.label_client_identification_number = QtWidgets.QLabel(self.frame)
                self.label_client_identification_number.setGeometry(QtCore.QRect(10, 230, 120, 30))
                self.label_client_identification_number.setFont(CSS.set_font(12, False, 50))
                self.label_client_identification_number.setAutoFillBackground(False)
                self.label_client_identification_number.setObjectName("label_client_identification_number")

                CSS.line_tab(self.frame)

        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate

                new = APIAxiomDB()

                self.btn_pushButton_refresh.setText(_translate("MainWindow", "Очистить"))
                self.checkBox_2_application_order.setText(_translate("MainWindow", " -  Заявка - Заказ"))
                self.btn_pushButton_new_client.setText(_translate("MainWindow", "Новый\nклиент"))
                self.label_car_brand_and_number.setText(_translate("MainWindow", "Машина"))
                self.txt_edit_lineEdit_client_owner_name.setText(_translate("MainWindow", "Фамилия И.О."))
                self.label_car_vin_code.setText(_translate("MainWindow", "VIN-код "))
                self.label_client_job_title.setText(_translate("MainWindow", "Должность"))
                self.btn_pushButton_car_part_choice.setText(_translate("MainWindow", "Запчасти"))
                self.txt_label_order_number.setText(_translate("MainWindow", str(new.count_act() + 1)))
                self.txt_label_car_brand.setText(_translate("MainWindow", "марка машины"))
                self.btn_pushButton_order_close.setText(_translate("MainWindow", "Закрыть Акт"))
                self.label_client_name.setText(_translate("MainWindow", "Клиент"))
                self.txt_label_car_number.setText(_translate("MainWindow", "номер машины"))
                self.btn_pushButton_car_car_choice.setText(_translate("MainWindow", "Машина"))
                self.btn_pushButton_new_car.setText(_translate("MainWindow", "Новая\nмашина"))
                self.btn_pushButton_print_order.setText(_translate("MainWindow", "Распечатать"))
                self.txt_label_order_number_prefix.setText(_translate("MainWindow", "А"))
                self.checkBox_1_repair_request.setText(_translate("MainWindow", " -  Заявка - Заказ на ремонт"))
                self.label_client_owner_name.setText(_translate("MainWindow", "ФИО заказчика"))
                self.label_order_number.setText(_translate("MainWindow", "Заявка №"))
                self.txt_label_client_name.setText(_translate("MainWindow", "название клиента"))
                self.txt_label_car_model.setText(_translate("MainWindow", "модель машины"))
                self.label_car_model.setText(_translate("MainWindow", "Модель"))
                self.checkBox_4_internal_consumption.setText(_translate("MainWindow", " -  Внутренняя накладная"))
                self.txt_edit_lineEdit_client_job_title.setText(_translate("MainWindow", "должность"))
                self.checkBox_3_act_of_acceptance.setText(_translate("MainWindow", " -  Акт приёмки-сдачи"))
                self.label_order_number_sep.setText(_translate("MainWindow", "-"))
                self.txt_label_car_vin_code.setText(_translate("MainWindow", "VIN код машины"))
                self.label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
                self.txt_label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
                self.dateEdit.setDisplayFormat(_translate("MainWindow", "d  MMMM   yyyy"))
