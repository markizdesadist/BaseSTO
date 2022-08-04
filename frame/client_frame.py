from PyQt5 import QtCore, QtWidgets

from frame.CSS_template import CSS
from dbase.dbapi import APIAxiomDB
from dbase.databasecreate import CreateDB


class Client:
    def __init__(self):
        self.frame = None
        self.btn_pushButton_smile = None
        self.btn_pushButton_edit = None
        self.btn_pushButton_save = None
        self.txt_edit_lineEdit_client_name = None
        self.txt_edit_textEdit_client_full_name = None
        self.txt_edit_textEdit_client_address = None
        self.txt_edit_lineEdit_client_identification_number = None
        self.txt_edit_lineEdit_client_phone = None
        self.txt_edit_lineEdit_client_mobile_phone = None
        self.label_client_identification_number = None
        self.label_client_name = None
        self.label_client_address = None
        self.label_client_full_name = None
        self.label_client_phone = None
        self.label_client_mobile_phone = None

        self.current_id = None

    @CSS.logger_wrap
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

    @CSS.logger_wrap
    def add_action(self):
        try:
            self.btn_pushButton_save.clicked.connect(lambda: self.check_client_name())
            self.btn_pushButton_edit.clicked.connect(lambda: self.edit_client())
            # self.btn_pushButton_smile.clicked.connect(lambda: self.smile_fun())
            self.btn_pushButton_edit.clicked.connect(lambda: self.edit_client())
            # self.txt_edit_textEdit_client_full_name.
        except Exception as err:
            pass

    @CSS.logger_wrap
    def edit_client(self):
        edit = CreateDB()
        try:
            edit.update_client(
                id=self.current_id,
                name=self.txt_edit_lineEdit_client_name.text(),
                full_name=self.txt_edit_textEdit_client_full_name.toPlainText(),
                address=self.txt_edit_textEdit_client_address.toPlainText(),
                telefone=self.txt_edit_lineEdit_client_phone.text(),
                mobile=self.txt_edit_lineEdit_client_mobile_phone.text()
            )
        except Exception as err:
            print(err)

    # @classmethod
    # def smile_fun(cls):
        # app = QtWidgets.QApplication(sys.argv)
        # Dialog = QtWidgets.QDialog()
        # ppw = PopUpWin()
        # ppw.setupUi()
        # ppw.set_text('Улыбнуться', 'green')
        # ppw.show()
        # sys.exit(app.exec_())
        # pass

    def check_client_name(self):
        query = APIAxiomDB()
        if self.txt_edit_lineEdit_client_name.text() in query.get_list_company():
            print('error name')
        else:
            self.save_new_client()

    def save_new_client(self):
        new = CreateDB()
        try:
            new.company_create(
                name=self.txt_edit_lineEdit_client_name.text(),
                full_name=self.txt_edit_textEdit_client_full_name.toPlainText(),
                address=self.txt_edit_textEdit_client_address.toPlainText(),
                pan_code=int(self.txt_edit_lineEdit_client_identification_number.text()),
                telefone=self.txt_edit_lineEdit_client_phone.text(),
                mobile=self.txt_edit_lineEdit_client_mobile_phone.text()
            )
        except ValueError as err:
            print(err)
        except Exception as err:
            print(err)

    def set_body(self):
        self.btn_pushButton_smile = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_smile.setGeometry(QtCore.QRect(468, 350, 85, 71))
        self.btn_pushButton_smile.setAutoFillBackground(False)
        self.btn_pushButton_smile.setStyleSheet(CSS.set_btn_color())
        self.btn_pushButton_smile.setFont(CSS.set_font())
        self.btn_pushButton_smile.setObjectName("btn_pushButton_new_car")

        self.btn_pushButton_edit = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_edit.setGeometry(QtCore.QRect(468, 110, 85, 71))
        self.btn_pushButton_edit.setAutoFillBackground(False)
        self.btn_pushButton_edit.setStyleSheet(CSS.set_btn_color())
        self.btn_pushButton_edit.setFont(CSS.set_font())
        self.btn_pushButton_edit.setObjectName("btn_pushButton_new_client")

        self.btn_pushButton_save = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_save.setGeometry(QtCore.QRect(453, 520, 101, 71))
        self.btn_pushButton_save.setStyleSheet(CSS.set_btn_color())
        self.btn_pushButton_save.setFont(CSS.set_font())
        self.btn_pushButton_save.setObjectName("btn_pushButton_save")

        self.txt_edit_lineEdit_client_name = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_client_name.setGeometry(QtCore.QRect(128, 110, 333, 31))
        self.txt_edit_lineEdit_client_name.setFont(CSS.set_font())
        self.txt_edit_lineEdit_client_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_client_name.setPlaceholderText("Короткое название клиента")
        self.txt_edit_lineEdit_client_name.setObjectName("txt_edit_lineEdit_client_name")
        self.txt_edit_lineEdit_client_name.setClearButtonEnabled(True)
        self.txt_edit_lineEdit_client_name.setTextMargins(CSS.set_margins())

        self.txt_edit_textEdit_client_full_name = QtWidgets.QTextEdit(self.frame)
        self.txt_edit_textEdit_client_full_name.setGeometry(QtCore.QRect(128, 150, 333, 61))
        self.txt_edit_textEdit_client_full_name.setFont(CSS.set_font())
        self.txt_edit_textEdit_client_full_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_textEdit_client_full_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_edit_textEdit_client_full_name.setTabChangesFocus(True)
        self.txt_edit_textEdit_client_full_name.setPlaceholderText("Полное название клиента")
        self.txt_edit_textEdit_client_full_name.setObjectName("txt_edit_textEdit_client_full_name")
        # self.txt_edit_textEdit_client_full_name.setTextMargins(CSS.set_margins())

        self.txt_edit_textEdit_client_address = QtWidgets.QTextEdit(self.frame)
        self.txt_edit_textEdit_client_address.setGeometry(QtCore.QRect(128, 220, 421, 61))
        self.txt_edit_textEdit_client_address.setFont(CSS.set_font())
        self.txt_edit_textEdit_client_address.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_textEdit_client_address.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_edit_textEdit_client_address.setTabChangesFocus(True)
        self.txt_edit_textEdit_client_address.setPlaceholderText("Адрес клиента")
        self.txt_edit_textEdit_client_address.setObjectName("txt_edit_textEdit_client_address")
        # self.txt_edit_textEdit_client_address.setTextMargins(CSS.set_margins())

        self.txt_edit_lineEdit_client_identification_number = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_client_identification_number.setGeometry(QtCore.QRect(128, 350, 333, 31))
        self.txt_edit_lineEdit_client_identification_number.setFont(CSS.set_font())
        self.txt_edit_lineEdit_client_identification_number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_client_identification_number.setObjectName(
            "txt_edit_lineEdit_client_identification_number")
        self.txt_edit_lineEdit_client_identification_number.setPlaceholderText("УНП клиента")
        self.txt_edit_lineEdit_client_identification_number.setClearButtonEnabled(True)
        self.txt_edit_lineEdit_client_identification_number.setTextMargins(CSS.set_margins())

        self.txt_edit_lineEdit_client_phone = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_client_phone.setGeometry(QtCore.QRect(128, 390, 333, 31))
        self.txt_edit_lineEdit_client_phone.setFont(CSS.set_font())
        self.txt_edit_lineEdit_client_phone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_client_phone.setObjectName("txt_edit_lineEdit_client_phone")
        self.txt_edit_lineEdit_client_phone.setPlaceholderText("городские номера телефонов клиента")
        self.txt_edit_lineEdit_client_phone.setClearButtonEnabled(True)
        self.txt_edit_lineEdit_client_phone.setTextMargins(CSS.set_margins())

        self.txt_edit_lineEdit_client_mobile_phone = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_client_mobile_phone.setGeometry(QtCore.QRect(128, 430, 425, 31))
        self.txt_edit_lineEdit_client_mobile_phone.setFont(CSS.set_font())
        self.txt_edit_lineEdit_client_mobile_phone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_client_mobile_phone.setObjectName("txt_edit_lineEdit_client_mobile_phone")
        self.txt_edit_lineEdit_client_mobile_phone.setPlaceholderText("мобильный номер телефона клиента")
        self.txt_edit_lineEdit_client_mobile_phone.setClearButtonEnabled(True)
        self.txt_edit_lineEdit_client_mobile_phone.setTextMargins(CSS.set_margins())

    def set_label(self):
        self.label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.label_client_identification_number.setGeometry(QtCore.QRect(10, 350, 120, 30))
        self.label_client_identification_number.setFont(CSS.set_font(12, False, 50))
        self.label_client_identification_number.setObjectName("label_client_identification_number")

        self.label_client_name = QtWidgets.QLabel(self.frame)
        self.label_client_name.setGeometry(QtCore.QRect(10, 110, 120, 30))
        self.label_client_name.setFont(CSS.set_font(12, False, 50))
        self.label_client_name.setObjectName("label_client_name")

        self.label_client_address = QtWidgets.QLabel(self.frame)
        self.label_client_address.setGeometry(QtCore.QRect(10, 220, 120, 30))
        self.label_client_address.setFont(CSS.set_font(12, False, 50))
        self.label_client_address.setObjectName("label_client_address")

        self.label_client_full_name = QtWidgets.QLabel(self.frame)
        self.label_client_full_name.setGeometry(QtCore.QRect(10, 150, 120, 30))
        self.label_client_full_name.setFont(CSS.set_font(12, False, 50))
        self.label_client_full_name.setObjectName("label_client_full_name")

        self.label_client_phone = QtWidgets.QLabel(self.frame)
        self.label_client_phone.setGeometry(QtCore.QRect(10, 390, 120, 30))
        self.label_client_phone.setFont(CSS.set_font(12, False, 50))
        self.label_client_phone.setObjectName("label_client_phone")

        self.label_client_mobile_phone = QtWidgets.QLabel(self.frame)
        self.label_client_mobile_phone.setGeometry(QtCore.QRect(10, 430, 120, 30))
        self.label_client_mobile_phone.setFont(CSS.set_font(12, False, 50))
        self.label_client_mobile_phone.setObjectName("label_client_mobile_phone")

        CSS.line_tab(self.frame)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.btn_pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_pushButton_edit.setText(_translate("MainWindow", "Редакти\nровать\nданные\nклиента"))
        self.btn_pushButton_smile.setText(_translate("MainWindow", "Улыбнуться"))

        self.label_client_name.setText(_translate("MainWindow", "Клиент"))
        self.label_client_full_name.setText(_translate("MainWindow", "Название"))
        self.label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
        self.label_client_address.setText(_translate("MainWindow", "Адрес почты"))
        self.label_client_phone.setText(_translate("MainWindow", "Телефон"))
        self.label_client_mobile_phone.setText(_translate("MainWindow", "Мобильный"))
        
        # self.txt_edit_lineEdit_client_name.setText(_translate("MainWindow", "  клиент"))
        # self.txt_edit_textEdit_client_full_name.setHtml(_translate(
        #     "MainWindow",
        #     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #     "<html>"
        #     "<head>"
        #     "<meta name=\"qrichtext\" content=\"1\" />"
        #     "<style type=\"text/css\">\n"
        #     "p, li { white-space: pre-wrap; }\n"
        #     "</style>"
        #     "</head>"
        #     "<body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        #     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
        #     "-qt-block-indent:0; text-indent:0px;\">"
        #     "<span style=\" font-size:10pt;\">  полное название клиента</span>"
        #     "</p>"
        #     "</body>"
        #     "</html>")
        # )
        # self.txt_edit_textEdit_client_address.setHtml(_translate(
        #     "MainWindow",
        #     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #     "<html>"
        #     "<head>"
        #     "<meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        #     "p, li { white-space: pre-wrap; }\n"
        #     "</style>"
        #     "</head>"
        #     "<body style=\" font-family:\'Droid Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        #     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
        #     "text-indent:0px;\">"
        #     "<span style=\" font-size:10pt;\">  Адрес</span>"
        #     "</p>"
        #     "</body>"
        #     "</html>")
        # )
        # self.txt_edit_lineEdit_client_identification_number.setText(_translate("MainWindow", "  УНП клиента"))
        # self.txt_edit_lineEdit_client_phone.setText(_translate("MainWindow", "  городской телефон"))
        # self.txt_edit_lineEdit_client_mobile_phone.setText(_translate("MainWindow", "  мобильный номер клиента"))


if __name__ == '__main__':
    pass
