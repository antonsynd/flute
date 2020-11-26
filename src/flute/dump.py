"""
Some utilities to dump the content of objects
"""


def dump_event(e):
    """
    Utility to dump all discoverable properties of a MIDI event object
    """
    res = 'Event(\n'

    attributes = {}

    for k in dir(e):
        v = getattr(e, k)
        t = type(v)

        # Ignore any functions or built-ins
        # FIXME: Determine if there are any other types being used
        if t == int or t == None or t == bytes or t == bytearray:
            attributes[k] = (t, v)

    sorted_attributes = list(sorted(attributes.items()))

    # TODO: Use t for formatting?
    for k, (t, v) in sorted_attributes[:-1]:
        res += '    {}: {},\n'.format(k, v)

    last = sorted_attributes[-1]

    res += '    {}: {}\n)'.format(last[0], last[1][1])

    return res
