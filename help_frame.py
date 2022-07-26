from PyQt5 import QtWidgets, QtCore


class Help:
    def __init__(self):
        self.frame_help = None
        self.txt_plainTextEdit_help = None

    def set_body(self, frame):
        self.frame_help = QtWidgets.QFrame(frame)

        self.frame_help.setGeometry(QtCore.QRect(0, 0, 571, 593))
        self.frame_help.setAutoFillBackground(True)
        self.frame_help.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_help.setObjectName("frame_help")
        self.txt_plainTextEdit_help = QtWidgets.QPlainTextEdit(self.frame_help)

        self.txt_plainTextEdit_help.setGeometry(QtCore.QRect(10, 10, 551, 581))
        self.txt_plainTextEdit_help.setAutoFillBackground(True)
        self.txt_plainTextEdit_help.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.txt_plainTextEdit_help.setObjectName("txt_plainTextEdit_help")
