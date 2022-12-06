
class Remote:
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 0
    MAX_CHANNEL = 10
    MIN_SOURCE = 0
    MAX_SOURCE = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Remote.MIN_VOLUME
        self.channel = Remote.MIN_CHANNEL
        self.source = Remote.MIN_SOURCE

    def power(self):
        if self.status == False:
            self.status = True

        else:
            self.status = False

    def mute(self):
        if self.muted == False:
            self.muted = True
        else:
            self.muted = False

    def channel_up(self):
        if self.status == True:
            if self.channel < Remote.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Remote.MIN_CHANNEL

        else:
            pass

    def change_source(self):
        if self.status == True:
            if self.source < Remote.MAX_SOURCE:
                self.source += 1
            else:
                self.source = Remote.MIN_SOURCE
        else:
            pass

    def channel_down(self):
        if self.status == True:
            if self.channel > Remote.MIN_CHANNEL:
                self.channel -= 1

            else:
                self.channel = Remote.MAX_CHANNEL
        else:
            pass

    def volume_up(self):
        if self.status == True:

            if self.volume < Remote.MAX_VOLUME:
                self.volume += 1

            else:
                pass

        else:
            pass

    def volume_down(self):
        if self.status == True:
            if self.volume > Remote.MIN_VOLUME:
                self.volume -= 1

            else:
                pass

        else:
            pass
