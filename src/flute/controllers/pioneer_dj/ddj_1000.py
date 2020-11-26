"""
Enums for working with the Pioneer DJ DDJ-1000 controller

https://www.pioneerdj.com/-/media/pioneerdj/software-info/controller/ddj-1000/ddj-1000_midi_message_list_e1.pdf
"""
from ... import enum


class _MidiChannel(enum.Enum_):
    @property
    def DECK_1(self):
        return _MidiChannel(0x00)

    @property
    def DECK_2(self):
        return _MidiChannel(0x01)

    @property
    def DECK_3(self):
        return _MidiChannel(0x02)

    @property
    def DECK_4(self):
        return _MidiChannel(0x03)

    @property
    def EFFECT(self):
        return _MidiChannel(0x04)

    @property
    def UNUSED(self):
        return _MidiChannel(0x05)

    @property
    def BROWSER(self):
        return _MidiChannel(0x06)

    @property
    def DECK_1_PERFORMANCE_PAD(self):
        return _MidiChannel(0x07)

    @property
    def DECK_1_PERFORMANCE_PAD_WITH_SHIFT(self):
        return _MidiChannel(0x08)

    @property
    def DECK_2_PERFORMANCE_PAD(self):
        return _MidiChannel(0x09)

    @property
    def DECK_2_PERFORMANCE_PAD_WITH_SHIFT(self):
        return _MidiChannel(0x0A)

    @property
    def DECK_3_PERFORMANCE_PAD(self):
        return _MidiChannel(0x0B)

    @property
    def DECK_3_PERFORMANCE_PAD_WITH_SHIFT(self):
        return _MidiChannel(0x0C)

    @property
    def DECK_4_PERFORMANCE_PAD(self):
        return _MidiChannel(0x0D)

    @property
    def DECK_4_PERFORMANCE_PAD_WITH_SHIFT(self):
        return _MidiChannel(0x0E)


class _DeckControlNumber(enum.Enum_):
    @property
    def JOG_ROTATE(self):
        return _DeckControlNumber(0x21)

    @property
    def JOG_ROTATE_VINYL_ON(self):
        return _DeckControlNumber(0x22)

    @property
    def JOG_ROTATE_VINYL_OFF(self):
        return _DeckControlNumber(0x22)


class _MixerControlNumber(enum.Enum_):
    @property
    def CHANNEL_FADER_LEAST_SIGNIFICANT_BYTE(self):
        return _MixerControlNumber(0x33)

    @property
    def CHANNEL_FADER_MOST_SIGNIFICANT_BYTE(self):
        return _MixerControlNumber(0x13)


MidiChannel = _MidiChannel(-1)
DeckControlNumber = _DeckControlNumber(-1)
MixerControlNumber = _MixerControlNumber(-1)
