#name=DDJ 1000

from flute import dump
from flute.controllers.pioneer_dj.ddj_1000 import MidiChannel, DeckControlNumber, MixerControlNumber

import device
import midi
import ui


current_color = 0


def clamp(v, min, max):
    if v < min:
        return min
    elif v > max:
        return max

    return v


def overflow(v, min, max):
    if v < min:
        return max
    elif v > max:
        return min

    return v


def signum(v):
    if v > 0:
        return 1
    return -1


def rotate_color(d):
    global current_color

    if not device.isAssigned():
        return

    d = signum(d)

    # new_current_color = int(clamp(d + current_color, 0, 127))
    new_current_color = int(overflow(d + current_color, 0, 127))

    for x in range(0, 8):
        device.midiOutMsg(144, 7, x, new_current_color)
        device.midiOutMsg(144, 9, x, new_current_color)

    # print(d, new_current_color)

    current_color = new_current_color


def shift_color(d, c):
    global current_color

    if not device.isAssigned():
        return

    d = int(clamp(d, 0, 127))

    if c == 0:
        targets = (1, 5)
    elif c == 1:
        targets = (2, 6)
    elif c == 2:
        targets = (0, 4)
    else:
        targets = (3, 7)

    for x in targets:
        device.midiOutMsg(144, 7, x, d)
        device.midiOutMsg(144, 9, x, d)

    # print(d)

    current_color = d



def OnMidiMsg(e):
    e.handled = True

    channel = e.midiChan
    cc = e.controlNum
    val = e.controlVal

    if channel == MidiChannel.DECK_1 and \
        (cc == DeckControlNumber.JOG_ROTATE or cc == DeckControlNumber.JOG_ROTATE_VINYL_ON
            or cc == DeckControlNumber.JOG_ROTATE_VINYL_OFF):
        if val > 64:
            # rotated clockwise
            # print('clockwise', val - 65)

            rotate_color(val - 65)
        else:
            # rotated ccw
            # print('countercw', val - 63)
            rotate_color(val - 63)
    elif MidiChannel.DECK_1 <= channel <= MidiChannel.DECK_4:
        if cc == MixerControlNumber.CHANNEL_FADER_MOST_SIGNIFICANT_BYTE:
            shift_color(val, channel)
    else:
        # print(dump.dump_event(e))
        pass
