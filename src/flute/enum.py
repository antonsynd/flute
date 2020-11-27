"""
Poor man's enum because FL Studio doesn't expose the enum module

See flute.controllers.pioneer_dj.ddj_1000 for an example
"""


class _Enum(int):
    def __new__(cls, value):
        x = int.__new__(cls, value)
        return x

    def __eq__(self, other):
        if _Enum in other.__class__.__bases__:
            return type(other) == type(self) and int(self) == int(other)

        return other == int(self)
