from PyQt5.QtWidgets import *
from view_remote import *
from remote import Remote


class ControllerRemote(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_power.clicked.connect(lambda: Remote.power)
        self.button_source.clicked.connect(lambda: Remote.change_source)
        self.volumeup_button.clicked.connect(lambda: Remote.volume_up)
        self.volumedown_button.clicked.connect(lambda: Remote.volume_down)
        self.button_mute.clicked.connect(lambda: Remote.mute)
