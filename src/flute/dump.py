"""
Some utilities to dump the content of objects.
"""
import plugins

import math


def dump_event(e):
    """
    Utility to dump all discoverable properties of a MIDI event object.
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


def dump_params(index, slot_index = -1):
    """
    Utility to dump all params and the values for a plugin.
    """
    num_params = plugins.getParamCount(index, slot_index)

    params = []
    largest_param_index = 0

    res = 'Params(\n'

    for i in range(0, num_params - 1):
        param_name = plugins.getParamName(i, index, slot_index)

        if param_name:
            params.append((
                i,
                param_name,
                plugins.getParamValue(i, index, slot_index)))

            if i > largest_param_index:
                largest_param_index = i

    # FIXME: maybe just convert to str and count len, this is dependent on
    # FL Studio providing the math module (currently silent)
    digits = int(math.log10(largest_param_index)) + 1

    param_template = '    {{:0{}d}}: {{}}: {{}},\n'.format(digits)
    param_template_last = '    {{:0{}d}}: {{}}: {{}})'.format(digits)

    for i, k, v in params[:-1]:
        res += param_template.format(i, k, v)

    res += param_template_last.format(
        params[-1][0], params[-1][1], params[-1][2])

    return res
