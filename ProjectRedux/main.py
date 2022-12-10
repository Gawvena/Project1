
from controller_remote import *

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = ControllerRemote()
    w.show()
    sys.exit(app.exec_())




if __name__ == "__main__":

    main()