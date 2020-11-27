import general


_fl_midi_scripting_api_version_number = general.getVersion()


# TODO: turn this into a decorator
def require_version(version):
    if version > _fl_midi_scripting_api_version_number:
        raise NotImplementedError(
            f'This method requires FL MIDI Scripting API version {version}, '
            f'but this version of FL Studio is providing '
            f'{_fl_midi_scripting_api_version_number}')
