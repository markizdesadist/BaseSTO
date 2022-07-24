from PyQt5.QtWidgets import QFrame
from mainframe import MainFrame
from client import Client
from windowstomodel.order import Order
from car import Car
from windowstomodel import BaseSTO


def body_frame(frame: QFrame = None, hide: bool = True):
    if hide:
        frame.hide()
    else:
        frame.show()


def action_to_change_window(btn, text):
    body_frame(BaseSTO.frame_order, hide=True)
    body_frame(BaseSTO.frame_client, hide=True)
    body_frame(BaseSTO.frame_car, hide=True)
    change_body_and_action_dict = {
        'новый клиент': lambda: Client.set_body(BaseSTO.frame_client),
        # '... client': lambda: Ui_MainWindow.client.set_body(self.frame_client),
        # 'новый акт': lambda: Ui_MainWindow.order.set_body(self.frame_order),
        'новая машина': lambda: Car.set_body(BaseSTO.frame_car),
        # '... car': lambda: Ui_MainWindow.car.set_body(self.frame_car),
        # 'save': print,
        # 'справка': print,
        # 'quit': QApplication.quit,
        # 'закрыть акт': print
    }
    if btn.objectName().startswith('pushButton'):
        btn.setDown(True)
    change_body_and_action_dict[text.lower().strip()]()
