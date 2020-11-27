"""
Provides an OOP interface to FL Studio's mixer module.
"""
from flute.enum import _Enum
from flute.version import require_version

import mixer


def num_mixer_tracks():
    return mixer.trackCount()


def set_current_track(index, flags):
    mixer.setTrackNumber(index, flags)


def get_current_track():
    return mixer.getTrackNumber()


def get_song_step_pos():
    return mixer.getSongStepPos()


def get_current_tempo(as_int = 0):
    return mixer.get_current_tempo(as_int)


def get_rec_pps():
    return mixer.getRecPPS()


def get_song_tick_pos(mode):
    return mixer.getSongTickPos(mode)


def link_to_channel(mode):
    # FIXME: probably the current track?
    mixer.linkTrackToChannel(mode)


class _MixerTrackPeakMode(_Enum):
    @property
    def L(self):
        return _MixerTrackPeakMode(0)

    @property
    def R(self):
        return _MixerTrackPeakMode(1)

    @property
    def LR(self):
        return _MixerTrackPeakMode(2)

    @property
    def L_INVERTED(self):
        return _MixerTrackPeakMode(0)

    @property
    def R_INVERTED(self):
        return _MixerTrackPeakMode(1)

    @property
    def LR_INVERTED(self):
        return _MixerTrackPeakMode(3)


MixerTrackPeakMode = _MixerTrackPeakMode(-1)


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
        """
        Setting name to empty string returns it to the default value.
        """
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

    @require_version(2)
    def toggle_mute(self):
        mixer.muteTrack(self)

    def is_solo(self):
        return mixer.isTrackSolo(self)

    def solo(self):
        # TODO: support mode
        mixer.soloTrack(self, 1)

    def unsolo(self):
        mixer.soloTrack(self, 0)

    def toggle_solo(self):
        mixer.soloTrack(self)

    def is_enabled(self):
        return mixer.isTrackEnabled(self)

    def enable(self):
        if not self.is_enabled():
            mixer.enableTrack(self)

    def unenable(self):
        if self.is_enabled():
            mixer.enableTrack(self)

    def toggle_enable(self):
        mixer.enableTrack(self)

    def is_automation_enabled(self):
        # TODO: what does plugIndex do?
        raise NotImplementedError()

    def get_plugin_id(self, index):
        return mixer.getTrackPluginId(self, index)

    def is_plugin_valid(self, index):
        return mixer.isTrackPluginValid(self, index)

    @property
    def volume(self):
        return mixer.getTrackVolume(self)

    @volume.setter
    def volume(self, volume):
        mixer.setTrackVolume(self, volume)

    @property
    def pan(self):
        return mixer.getTrackPan(self)

    @pan.setter
    def pan(self, pan):
        mixer.setTrackPan(self, pan)

    def is_selected(self):
        return mixer.isTrackSelected(self)

    def select(self):
        if not self.is_selected():
            return mixer.selectTrack(self)

    def deselect(self):
        if self.is_selected():
            return mixer.selectTrack(self)

    def toggle_selected(self):
        return mixer.selectTrack(self)

    @staticmethod
    def select_all():
        mixer.selectAll()

    @staticmethod
    def deselect_all():
        mixer.deselectAll()

    def set_route_to(self, dest_index, value):
        mixer.setRouteTo(self, dest_index, value)

    def is_routed_to(self, dest_index):
        return mixer.getRouteSendActive(self, dest_index)

    @staticmethod
    def after_routing_changed():
        # TODO: maybe name this something else
        raise NotImplementedError()

    # TODO: event methods???

    @property
    def peak(self, mode):
        return mixer.getTrackPeak(self, mode)

    @property
    def recording_file_name(self):
        return mixer.getTrackRecordingFileName(self)
