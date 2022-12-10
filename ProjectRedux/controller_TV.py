from PyQt5.QtWidgets import *
from view_TV import *



class ControllerTV(QMainWindow, Ui_MainWindow2):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)



