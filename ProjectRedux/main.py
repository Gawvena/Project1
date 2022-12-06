from controller_remote import *


def main():
    app = QApplication([])
    window = ControllerRemote()
    window.show
    app.exec_()


if __name__ == '__main__':
    main()
