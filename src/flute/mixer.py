"""
Provides an OOP interface to FL Studio's mixer module.
"""
from flute.version import require_version

import mixer


def num_mixer_tracks():
    return mixer.trackCount()


def set_current_track(index, flags):
    mixer.setTrackNumber(index, flags)


def get_current_track():
    return mixer.getTrackNumber()


class MixerTrack(int):
    """
    Derives from int so it can be passed to the native FL Studio Python API
    without any modification.
    """
    def __new__(cls, index):
        if index >= mixer.trackCount():
            raise IndexError(
                'Index must be in the range [0, {})'.format(num_mixer_tracks()))

        x = int.__new__(cls, index)
        return x

    @property
    def name(self):
        return mixer.getTrackName(self)

    @name.setter
    def name(self, name):
        mixer.setTrackName(self, name)

    @property
    def color(self):
        return mixer.getTrackColor(self)

    @color.setter
    def color(self, color):
        mixer.setTrackColor(self, color)

    def is_armed(self):
        return mixer.isTrackArmed(self)

    def arm(self):
        if not self.is_armed():
            mixer.armTrack(self)

    def unarm(self):
        if self.is_armed():
            mixer.armTrack(self)

    def toggle_arm(self):
        mixer.armTrack(self)

    @require_version(2)
    def is_muted(self):
        return mixer.isTrackMuted(self)

    @require_version(2)
    def mute(self):
        if not self.is_muted():
            mixer.muteTrack(self)

    @require_version(2)
    def unmute(self):
        if self.is_muted():
            mixer.muteTrack(self)

    @require_version(8)
    def toggle_mute(self):
        mixer.muteTrack(self)
