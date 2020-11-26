"""
Provides an OOP interface to FL Studio's mixer module.
"""
import mixer


def num_tracks():
    return mixer.trackCount


def get_track(number):
    if number < mixer.trackCount:
        return Track(number)
    else:
        raise Exception(f'There are only {num_tracks()} tracks')


class Track:
    # Should not be instantiated by user
    def __init__(self, number):
        # TODO: raise an exception if number exceeds num_tracks()
        self.number_ = number

    @property
    def number(self):
        return self.number_

    @property
    def name(self):
        return mixer.getTrackName(self.number())

    @name.setter
    def name(self, name):
        mixer.setTrackName(self.number(), name)

    def is_armed(self):
        return mixer.isTrackArmed(self.number())

    def arm(self):
        mixer.armTrack(self.number())
