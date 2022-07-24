from PyQt5 import QtWidgets, QtCore, QtGui


class BtnFrame:
    def __int__(self):
        self.frame = QtWidgets.QFrame()

    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.set_body()
        return self.frame

    def set_body(self):
        self.btn_pushButton_exit = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_exit.setGeometry(QtCore.QRect(1110, 5, 117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_pushButton_exit.setFont(font)
        self.btn_pushButton_exit.setAutoFillBackground(False)
        self.btn_pushButton_exit.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                               "border-bottom-color: rgb(255, 255, 127);")
        self.btn_pushButton_exit.setObjectName("btn_pushButton_exit")
        self.btn_pushButton_help = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_help.setGeometry(QtCore.QRect(900, 5, 117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_pushButton_help.setFont(font)
        self.btn_pushButton_help.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_pushButton_help.setAutoFillBackground(False)
        self.btn_pushButton_help.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                               "border-bottom-color: rgb(255, 255, 127);")
        self.btn_pushButton_help.setObjectName("btn_pushButton_help")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 5, 117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                        "border-bottom-color: rgb(255, 255, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 5, 117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                        "border-bottom-color: rgb(255, 255, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 5, 117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                        "border-bottom-color: rgb(255, 255, 127);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(410, 5, 117, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                        "border-bottom-color: rgb(255, 255, 127);")
        self.pushButton_9.setObjectName("pushButton_9")

        # self.btn_pushButton_exit.clicked.connect(QtWidgets.QApplication.exit())  # type: ignore

        # self.add_action_btn()

        self.retranslateUi()

    def add_action_btn(self):
        self.btn_pushButton_exit.clicked.connect(lambda: self.frame.parent().parent().close())
        # self.btn_pushButton_help.clicked.connect(lambda: self.frame.parent().tabWidget.setCurrentIndex(4))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.btn_pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.btn_pushButton_help.setText(_translate("MainWindow", "Справка"))
        self.pushButton_6.setText(_translate("MainWindow", "....."))
        self.pushButton_7.setText(_translate("MainWindow", "....."))
        self.pushButton_8.setText(_translate("MainWindow", "....."))
        self.pushButton_9.setText(_translate("MainWindow", "....."))