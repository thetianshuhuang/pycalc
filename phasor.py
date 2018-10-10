

import math
import cmath
from math_mixins import MathCompareMixin, MathInPlaceMixin


_ENABLE_UNICODE = False


def _init(cfg):

    if cfg["unicode"]:
        global _ENABLE_UNICODE
        _ENABLE_UNICODE = True


class Phasor(MathCompareMixin, MathInPlaceMixin):

    def __init__(self, *args, **kwargs):

        # Initialize to zero, just in case
        self.r = 0
        self.theta = 0

        # Rectangular mode
        if len(args) == 1 and len(kwargs) == 0:
            self.r, self.theta = cmath.polar(args[0])

        # Degree/radian inferencing (do not use this in programs)
        elif len(args) == 2 and len(kwargs) == 0:
            mode = "degree" if args[1] > math.pi * 2 else "radian"
            print(
                (
                    "Warning: Phasor angle mode assumed to be {mode}."
                    " Use deg= or rad= to specify an input mode."
                ).format(mode=mode))
            self.r = math.abs(args[0])
            self.theta = args[1] if mode == "rad" else math.radians(args[1])
            if args[0] < 0:
                self.theta += math.pi

        # Radian or degree mode via kwargs
        elif len(args) == 1 and len(kwargs) == 1:
            self.r = args[0]
            if "rad" in kwargs:
                self.theta = kwargs["rad"]
            elif "deg" in kwargs:
                self.theta = math.radians(kwargs["deg"])

        # Unrecognized input mode
        else:
            print("Input mode not recognized.")

    def __str__(self):

        return (
            (u"{r}\u2220{theta}" if _ENABLE_UNICODE else "{r}<{theta}")
            .format(r=round(self.r, 2), theta=round(self._fmt_theta(), 2))
        )

    def __repr__(self):

        return "Phasor " + self.__str__()

    def __abs__(self):
        return abs(self.r)

    def __add__(self, x):
        return Phasor(self.rect() + x.rect())

    def __div__(self, x):
        return Phasor(self.rect() / x.rect())

    def __mul__(self, x):
        return Phasor(self.r * x.r, rad=self.theta + x.theta)

    def __neg__(self, x):
        return Phasor(self.r, rad=self.theta + math.pi)

    def __sub__(self, x):
        return Phasor(self.rect() - x.rect())

    def __ipow__(self, b):
        return Phasor(
            self.rect() ** (
                b if (type(b) == int or type(b) == float)
                else b.rect()
            )
        )

    def __or__(self, b):
        return Phasor(1. / (1. / self.rect() + 1. / b.rect()))

    def _fmt_theta(self):
        return self.theta % (2 * math.pi)

    def norm(self):

        return self.r

    def rect(self):

        return cmath.rect(self.r, self.theta)

    def rad(self):

        return (self.r, self._fmt_theta())

    def deg(self):

        return (self.r, math.degrees(self._fmt_theta()))
