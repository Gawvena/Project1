import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from view_remote import *
from PyQt5.QtGui import QPixmap
from view_TV import Ui_MainWindow2
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class ControllerRemote(QMainWindow, Ui_MainWindow):
    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.a = Ui_MainWindow2()
        self.a.setupUi(self.window)
        self.window.show()

    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9
    MIN_SOURCE = 1
    MAX_SOURCE = 3

    def __init__(self, *args, **kwargs):
        self.status = False
        self.muted = False
        self.volume = ControllerRemote.MIN_VOLUME
        self.channel = ControllerRemote.MIN_CHANNEL
        self.source = ControllerRemote.MIN_SOURCE

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.open_window()
        self.tv()

        self.button_power.clicked.connect(lambda: self.power())
        self.button_source.clicked.connect(lambda: self.change_source())
        self.volumeup_button.clicked.connect(lambda: self.volume_up())
        self.volumedown_button.clicked.connect(lambda: self.volume_down())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.channelup_button.clicked.connect(lambda: self.channel_up())
        self.channeldown_button.clicked.connect(lambda: self.channel_down())

        self.button_0.clicked.connect(lambda: self.button_channel(0))
        self.button_1.clicked.connect(lambda: self.button_channel(1))
        self.button_2.clicked.connect(lambda: self.button_channel(2))
        self.button_3.clicked.connect(lambda: self.button_channel(3))
        self.button_4.clicked.connect(lambda: self.button_channel(4))
        self.button_5.clicked.connect(lambda: self.button_channel(5))
        self.button_6.clicked.connect(lambda: self.button_channel(6))
        self.button_7.clicked.connect(lambda: self.button_channel(7))
        self.button_8.clicked.connect(lambda: self.button_channel(8))
        self.button_9.clicked.connect(lambda: self.button_channel(9))

    def tv(self):
        self.effect = QMediaPlayer()
        if self.status:
            self.a.label_power.setText('🔴')
            self.a.label.setEnabled(True)

            if self.channel == 0:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Spray.mp3'))))
                self.effect.play()

                self.a.label.setPixmap(QPixmap('pictures/channel0.jpg'))
            elif self.channel == 1:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Country.mp3'))))
                self.effect.play()

                self.a.label.setPixmap(QPixmap('pictures/channel1.jpg'))
            elif self.channel == 2:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Kids.mp3'))))
                self.effect.play()

                self.a.label.setPixmap(QPixmap('pictures/channel2.jpg'))
            elif self.channel == 3:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel3.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Port.mp3'))))
                self.effect.play()

            elif self.channel == 4:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel4.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'SGallery.mp3'))))
                self.effect.play()

            elif self.channel == 5:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel5.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Ambulance.mp3'))))
                self.effect.play()

            elif self.channel == 6:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel6.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Cougar.mp3'))))
                self.effect.play()

            elif self.channel == 7:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel7.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Street.mp3'))))
                self.effect.play()

            elif self.channel == 8:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel8.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'Birds.mp3'))))
                self.effect.play()

            elif self.channel == 9:
                self.a.label_channel.setText('Channel: ' + str(self.channel))
                self.a.label.setPixmap(QPixmap('pictures/channel9.jpg'))
                self.effect.setMedia(QMediaContent(QUrl(os.path.join(os.getcwd(), 'MedLab.mp3'))))
                self.effect.play()

            if self.muted:
                self.a.label_volume.setText('Volume: 0')
                self.effect.setVolume(0)

            else:
                self.a.label_volume.setText('Volume: ' + str(self.volume))
                self.effect.setVolume(self.volume)

            if self.source == 1:
                self.a.label_source.setText('Source: ' + str(self.source))
                self.a.label_channel.setText('Channel: ' + str(self.channel))

            elif self.source == 2:
                self.a.label_source.setText('Source: ' + str(self.source))
                self.a.label.setPixmap(QPixmap('pictures/source2.jpg'))
                self.a.label_channel.setText('Channel: 0')

            else:
                self.a.label_source.setText('Source: ' + str(self.source))
                self.a.label.setPixmap(QPixmap('pictures/source3.jpg'))
                self.a.label_channel.setText('Channel: 0')

        else:
            self.a.label_source.setText('Source: ')
            self.a.label_power.setText('⭕')
            self.a.label_volume.setText('Volume: ')
            self.a.label_channel.setText('Channel: ')
            self.a.label.setDisabled(True)
            self.effect.stop()


    def power(self):
        if not self.status:
            self.status = True
            self.tv()


        else:
            self.status = False
            self.tv()

    def mute(self):
        if not self.muted:
            self.muted = True
            self.tv()
        else:
            self.muted = False
            self.tv()

    def channel_up(self):
        if self.status:
            if self.source == 1:
                if self.channel < ControllerRemote.MAX_CHANNEL:
                    self.channel += 1
                    self.tv()
                else:
                    self.channel = ControllerRemote.MIN_CHANNEL
                    self.tv()
            else:
                pass

        else:
            pass

    def change_source(self):
        if self.status:
            if self.source < ControllerRemote.MAX_SOURCE:
                self.source += 1
                self.tv()
            else:
                self.source = ControllerRemote.MIN_SOURCE
                self.tv()
        else:
            pass

    def channel_down(self):
        if self.status:
            if self.source == 1:
                if self.channel > ControllerRemote.MIN_CHANNEL:
                    self.channel -= 1
                    self.tv()

                else:
                    self.channel = ControllerRemote.MAX_CHANNEL
                    self.tv()
            else:
                pass
        else:
            pass

    def volume_up(self):
        if self.status:

            if self.volume < ControllerRemote.MAX_VOLUME:
                self.volume += 1
                self.tv()

            else:
                pass

        else:
            pass

    def volume_down(self):
        if self.status:
            if self.volume > ControllerRemote.MIN_VOLUME:
                self.volume -= 1
                self.tv()

            else:
                pass

        else:
            pass

    def button_channel(self, num):
        if self.status:
            if self.source == 1:
                self.channel = num
                self.tv()
            else:
                pass
        else:
            pass
