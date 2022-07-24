from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QLabel

from windowstomodel.templateCSS import CSS


class Logo:
    def __int__(self):
        pass

    def set_logo(self, frame):
        self.frame_logo = QFrame(frame)
        self.frame_logo.setGeometry(QtCore.QRect(0, 0, 420, 30))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")

        self.label_logo = QLabel(self.frame_logo)
        self.label_logo.setGeometry(QtCore.QRect(5, 5, 411, 21))
        self.label_logo.setFont(CSS.set_font(14))
        self.label_logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_logo.setAutoFillBackground(False)
        self.label_logo.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi()
        self.frame_logo.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_logo.setText(_translate("MainWindow", "TextLabel"))