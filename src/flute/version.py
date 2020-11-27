"""
Decorator to gate some of the tools here on what is available in the FL Studio
MIDI Scripting API version.
"""
import general


_fl_midi_scripting_api_version_number = general.getVersion()


def require_version(version):
    def require_version_decorator(f):
        def require_version_wrapper(*args, **kwargs):
            if version > _fl_midi_scripting_api_version_number:
                raise NotImplementedError(
                    '{}() not available in FL Studio MIDI Scripting API '
                    'version {}, requires version {}'.format(
                        f.__name__, _fl_midi_scripting_api_version_number,
                        version))

            return f(*args, **kwargs)

        return require_version_wrapper

    return require_version_decorator
