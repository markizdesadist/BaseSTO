from PyQt5 import QtWidgets, QtCore
from CSS_template import CSS


class ListWClient:
    def __int__(self):
        self.frame = QtWidgets.QFrame()


    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.set_body()
        return self.frame
        
    def set_body(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 250, 631))
        self.gridLayoutWidget.setAutoFillBackground(False)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_listWidget = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_listWidget.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_listWidget.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_listWidget.setHorizontalSpacing(1)
        self.gridLayout_listWidget.setVerticalSpacing(1)
        self.gridLayout_listWidget.setObjectName("gridLayout_listWidget")

        self.frame_label = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_label.setMaximumSize(QtCore.QSize(250, 30))
        self.frame_label.setAutoFillBackground(False)
        self.frame_label.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.frame_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label.setObjectName("frame_label")

        self.label_list = QtWidgets.QLabel(self.frame_label)
        self.label_list.setGeometry(QtCore.QRect(0, 0, 250, 30))
        self.label_list.setMinimumSize(QtCore.QSize(250, 30))
        self.label_list.setMaximumSize(QtCore.QSize(250, 30))
        self.label_list.setFont(CSS.set_font(14))
        self.label_list.setAutoFillBackground(False)
        self.label_list.setStyleSheet("")
        self.label_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_list.setObjectName("label_list")

        self.frame_listWidget = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_listWidget.setAutoFillBackground(False)
        self.frame_listWidget.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.frame_listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_listWidget.setObjectName("frame_listWidget")

        self.listWidget_list = QtWidgets.QListWidget(self.frame_listWidget)
        self.listWidget_list.setGeometry(QtCore.QRect(0, 0, 250, 557))
        self.listWidget_list.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget_list.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_list.setFont(CSS.set_font())
        self.listWidget_list.setAutoFillBackground(True)
        self.listWidget_list.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.listWidget_list.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_list.setAutoScroll(True)
        self.listWidget_list.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.listWidget_list.setTabKeyNavigation(True)
        self.listWidget_list.setProperty("showDropIndicator", False)
        self.listWidget_list.setAlternatingRowColors(True)
        self.listWidget_list.setObjectName("listWidget_list")

        self.frame_btn = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_btn.setMinimumSize(QtCore.QSize(250, 30))
        self.frame_btn.setMaximumSize(QtCore.QSize(250, 30))
        self.frame_btn.setAutoFillBackground(False)
        self.frame_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_btn.setObjectName("frame_btn")

        self.btn_pushButton_update = QtWidgets.QPushButton(self.frame_btn)
        self.btn_pushButton_update.setGeometry(QtCore.QRect(65, 0, 117, 30))
        self.btn_pushButton_update.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_pushButton_update.setFont(CSS.set_font())
        self.btn_pushButton_update.setAutoFillBackground(False)
        self.btn_pushButton_update.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                                             "border-bottom-color: rgb(255, 255, 127);")
        self.btn_pushButton_update.setObjectName("btn_pushButton_update")

        self.gridLayout_listWidget.addWidget(self.frame_label, 0, 0, 1, 1)
        self.gridLayout_listWidget.addWidget(self.frame_listWidget, 1, 0, 1, 1)
        self.gridLayout_listWidget.addWidget(self.frame_btn, 2, 0, 1, 1)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_list.setText(_translate("MainWindow", "Клиенты"))
        self.frame_btn.setStyleSheet(_translate("MainWindow", "background-color: rgb(85, 170, 0);"))
        self.btn_pushButton_update.setText(_translate("MainWindow", "Обновить"))

