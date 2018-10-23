
"""AC circuit analysis bindings"""

from phasor import Phasor


# Global frequency value
FREQUENCY = 1

# Flag for whether 'w' should be used instead
_USE_W = False


def set_frequency(x):
    """Set the global frequency.

    Parameters
    ----------
    x : float
        Desired omega value (period)
    """
    if _USE_W:
        global w
        w = x
    else:
        global FREQUENCY
        FREQUENCY = x


def _get_frequency():
    """Internal function to get the current frequency

    Returns
    -------
    float
        Current global phasor frequency
    """
    if _USE_W:
        return w
    else:
        return FREQUENCY


def capacitor(c):
    """Create a capacitor

    Parameters
    ----------
    c : float
        Capacitance

    Returns
    -------
    Phasor
        Phasor with impedence of 1/(jwC)
    """
    return Phasor(1. / (1j * _get_frequency() * c))


def inductor(l):
    """Create an inductor

    Parameters
    ----------
    l : float
        Inductance

    Returns
    -------
    Phasor
        Phasor with impedance of jwL
    """
    return Phasor(1j * _get_frequency() * l)


def resistor(r):
    """Create a resistor

    Parameters
    ----------
    r : float
        Resistance

    Returns
    -------
    Phasor
        Phasor with impedance of r
    """
    return Phasor(r)


def _init(cfg):

    if cfg["abbreviate_names"]:
        global C
        global L
        global R
        global Ph
        C = capacitor
        L = inductor
        R = resistor
        Ph = Phasor

    if cfg["use_w"]:
        global w
        global _USE_W
        w = 1
        _USE_W = True
