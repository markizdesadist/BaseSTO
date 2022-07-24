from PyQt5 import QtGui


class CSS:
    @classmethod
    def set_font(cls, size, bold=False, weight=0):
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        font.setWeight(weight)
        return font

    @classmethod
    def set_label_param(cls):
        return (120, 20)