
"""Phasor manipulation class

Example
-------
>>> x = Phasor(1 + 1j)
>>> x
Phasor 1.41 <0.79
>>> x + x
Phasor 2.83 <0.79
>>> y = Phasor(1, deg=30)
>>> y.rect()
(0.8660254037844387+0.49999999999999994j)
>>> y.deg()
(1, 29.999999999999996)
>>> y | y
Phasor 0.5 <0.52
"""

import math
import cmath
from math_mixins import MathCompareMixin, MathInPlaceMixin


# Flag to enable unicode symbols
_ENABLE_UNICODE = False
# Enable degree mode
_DEGREE_MODE = False
# Rounding
_PRECISION = 2
# Allowed complex number types
_COMPLEX_TYPES = [int, float, complex]


def _is_c(b):
    """Check if b is a valid complex number
    (by extension floating point numbers and integers as well)

    Parameters
    ----------
    b : arbitrary type
        Object to check

    Returns
    -------
    bool
        True if b matches an approved complex number type
    """

    return type(b) in _COMPLEX_TYPES


def _init(cfg):
    """Module initializer"""

    if cfg["enable_unicode"]:
        global _ENABLE_UNICODE
        _ENABLE_UNICODE = True
    if cfg["degree_mode"]:
        global _DEGREE_MODE
        _DEGREE_MODE = True
    if "precision" in cfg:
        global _PRECISION
        _PRECISION = cfg["precision"]


class PhasorMathMixin:
    """Phasor math mixins"""

    def __abs__(self):
        return abs(self.r)

    def __add__(self, x):
        return Phasor(self.rect() + self._pass_or_rect(x))

    def __truediv__(self, x):
        return Phasor(self.rect() / self._pass_or_rect(x))

    def __mul__(self, x):
        x = self._pass_or_cvt(x)
        return Phasor(self.r * x.r, rad=self.theta + x.theta)

    def __neg__(self):
        return Phasor(self.r, rad=self.theta + math.pi)

    def __sub__(self, x):
        return Phasor(self.rect() - self._pass_or_rect(x))

    def __ipow__(self, b):
        return Phasor(self.rect() ** (self._pass_or_rect(b)))

    def __or__(self, b):
        return Phasor(1. / (1. / self.rect() + 1. / self._pass_or_rect(b)))

    def __eq__(self, b):
        return self.rect() == b.rect()

    def _pass_or_cvt(self, b):
        """Convert b to a phasor if not already a phasor

        Parameters
        ----------
        b : arbitrary type
            Input type to be converted

        Returns
        -------
        Phasor
            b converted into a phasor (if b isn't already a phasor)
        """
        return (Phasor(b) if _is_c(b) else b)

    def _pass_or_rect(self, b):
        """Pass b, or take rectangular coordinates if b is a phasor

        Parameters
        ----------
        b : arbitrary type
            Type to be turned into a rect

        Returns
        -------
        complex
            intial value converted into a rectangular compelx number, if it
            isn't one already
        """
        return (b if _is_c(b) else b.rect())


class Phasor(MathCompareMixin, MathInPlaceMixin, PhasorMathMixin):
    """Phasor class

    Phasor class allowing addition, subtraction, multiplication, division, and
    exponentiation. If phasors are compared, then the magnitude is used as the
    value. Phasors in parallel (1/(1/a + 1/b)) can be computed with ``a | b``
    (the 'or' operator).

    Parameters
    ----------
    *args : complex[1] or complex[2]
        complex number to initialize the phasor with, or the magnitude of the
        phasor

    Keyword Args
    ------------
    rad : float
        Radian angle of the phasor
    deg : float
        Degree angle of the phasor
    """

    def __init__(self, *args, **kwargs):

        # Initialize to zero, just in case
        self.r = 0
        self.theta = 0

        # Rectangular mode
        if len(args) == 1 and len(kwargs) == 0:
            self._init_rect(args)

        # Degree/radian inferencing (do not use this in programs)
        elif len(args) == 2 and len(kwargs) == 0:
            self._init_inference(args)

        # Radian or degree mode via kwargs
        elif len(args) == 1 and len(kwargs) == 1:
            self._init_mode_specified(args, kwargs)

        # Unrecognized input mode
        else:
            self._init_fail()

    def __str__(self):

        return (
            (u"{r} \u2220{theta}" if _ENABLE_UNICODE else "{r} <{theta}")
            .format(
                r=round(self.r, _PRECISION),
                theta=round(self._fmt_theta(), _PRECISION))
        )

    def __repr__(self):

        return "Phasor " + self.__str__()

    def _init_rect(self, args):

        if hasattr(args[0], "r") and hasattr(args[0], "theta"):
            self.r = args[0].r
            self.theta = args[0].theta

        else:
            self.r, self.theta = cmath.polar(args[0])

    def _init_inference(self, args):
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

    def _init_mode_specified(self, args, kwargs):
        self.r = args[0]
        if "rad" in kwargs:
            self.theta = kwargs["rad"]
        elif "deg" in kwargs:
            self.theta = math.radians(kwargs["deg"])

    def _init_fail(self, args, kwargs):
        print("Input mode not recognized.")

    def _fmt_theta(self):
        rad = (self.theta + math.pi) % (2 * math.pi) - math.pi
        return math.degrees(rad) if _DEGREE_MODE else rad

    def rect(self):
        """Get the rectanguar representation of the phasor.

        Returns
        -------
        complex
            Rectangular representation of the phasor
        """

        return cmath.rect(self.r, self.theta)

    def rad(self):
        """Get the radian representation of the phasor.

        Returns
        -------
        float[]
            (magnitude, angle in radians)
        """

        return (self.r, self._fmt_theta())

    def deg(self):
        """Get the degree representation of the phasor.

        Returns
        -------
        float[]
            (magnitude, angle in degrees)
        """

        return (self.r, math.degrees(self._fmt_theta()))
