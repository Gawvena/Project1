from PyQt5.QtWidgets import *
from view_remote import *
from remote import Remote


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_power.clicked.connect(lambda: Remote.power)
