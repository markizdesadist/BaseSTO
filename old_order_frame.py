from PyQt5 import QtGui, QtWidgets, QtCore
from CSS_template import CSS
from datetime import datetime


class OldOrder:
    def __int__(self):
        self.frame = QtWidgets.QFrame()

    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 593))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.set_bode()
        self.retranslateUi()
        
    def set_bode(self):
        self.btn_pushButton_data_choce = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_data_choce.setGeometry(QtCore.QRect(210, 70, 151, 33))
        self.btn_pushButton_data_choce.setFont(CSS.set_font(12, True, 75))
        self.btn_pushButton_data_choce.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btn_pushButton_data_choce.setObjectName("btn_pushButton_data_choce")

        self.listWidget_list = QtWidgets.QListWidget(self.frame)
        self.listWidget_list.setGeometry(QtCore.QRect(10, 110, 551, 481))
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

        self.frame_data_po = QtWidgets.QFrame(self.frame)
        self.frame_data_po.setGeometry(QtCore.QRect(310, 0, 251, 51))
        self.frame_data_po.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_data_po.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data_po.setObjectName("frame_data_po")
        
        self.dateEdit = QtWidgets.QDateEdit(self.frame_data_po)
        self.dateEdit.setGeometry(QtCore.QRect(5, 10, 241, 37))
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
        self.frame_data.setGeometry(QtCore.QRect(10, 0, 251, 51))
        self.frame_data.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_data.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_data.setObjectName("frame_data")

        self.dateEdit_1 = QtWidgets.QDateEdit(self.frame_data)
        self.dateEdit_1.setGeometry(QtCore.QRect(5, 10, 241, 37))
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

        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_pushButton_data_choce.setText(_translate("MainWindow", "Выбрать период"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d  MMMM   yyyy"))
        self.dateEdit_1.setDisplayFormat(_translate("MainWindow", "d  MMMM   yyyy"))
