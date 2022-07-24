from PyQt5 import QtWidgets, QtCore
from CSS_template import CSS
from datetime import datetime


class LogoFrame:
    def __int__(self):
        self.frame = QtWidgets.QFrame()
        
    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.set_body()
        return self.frame
        
    def set_body(self):
        self.txt_label_logo = QtWidgets.QLabel(self.frame)
        self.txt_label_logo.setGeometry(QtCore.QRect(181, 0, 900, 35))
        self.txt_label_logo.setFont(CSS.set_font(16, True, 75))
        self.txt_label_logo.setAutoFillBackground(False)
        self.txt_label_logo.setStyleSheet("")
        self.txt_label_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txt_label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_label_logo.setObjectName("txt_label_logo")

        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(50, 0, 118, 37))
        self.timeEdit.setFont(CSS.set_font(14))
        self.timeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeEdit.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit.setKeyboardTracking(False)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setTime(datetime.now().time())

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.txt_label_logo.setText(_translate("MainWindow", "BaseSTO"))