MIN_VOLUME = 0
MAX_VOLUME = 2
MIN_CHANNEL = 0
MAX_CHANNEL = 3


class Television:

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = MIN_VOLUME
        self.channel = MIN_CHANNEL

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
            if self.channel < MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = MIN_CHANNEL

        else:
            pass

    def channel_down(self):
        if self.status == True:
            if self.channel > MIN_CHANNEL:
                self.channel -= 1

            else:
                self.channel = MAX_CHANNEL
        else:
            pass

    def volume_up(self):
        if self.status == True:

            if self.volume < MAX_VOLUME:
                self.volume += 1

            else:
                pass

        else:
            pass

    def volume_down(self):
        if self.status == True:
            if self.volume > MIN_VOLUME:
                self.volume -= 1

            else:
                pass

        else:
            pass

    def __str__(self):
        if self.muted == True:
            return f'TV status: Power - {self.status}, Channel - {self.channel}, Volume - {MIN_VOLUME}.'
        else:
            return f'TV status: Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}.'

