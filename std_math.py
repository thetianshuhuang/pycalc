
"""Basic math function definitions

Attributes
----------
sin, cos, tan
    Standard trig functions, with either radian or degree parameters
    depending on config.DEGREE_MODE and config.RADIAN_MODE.
sqrt
    Square root function
ln, log
    Logarithm
e, pi
    Standard constants math.e and math.pi
"""


import math
import cmath


# -- Trig Functions -----------------------------------------------------------

sin = math.sin
cos = math.cos
tan = math.tan


# -- Square Root --------------------------------------------------------------

sqrt = math.sqrt


# -- Log ----------------------------------------------------------------------

ln = math.log
log = math.log


# -- Exp ----------------------------------------------------------------------

def exp(x):
    if type(x) == complex:
        return cmath.exp(x)
    else:
        return math.exp(x)


# -- Constants ----------------------------------------------------------------

e = math.e
pi = math.pi


# -- Initializer --------------------------------------------------------------

def _init(cfg):

    if(cfg["degree_mode"]):

        def sin(x):
            return math.sin(math.radians(x))

        def cos(x):
            return math.cos(math.radians(x))

        def tan(x):
            return math.tan(math.radians(x))
