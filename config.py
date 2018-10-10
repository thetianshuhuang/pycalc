"""
pycalc configuration options


Example
-------
{
    "name": name of module,
    "namespace": name to import as; if None, the module is imported as *
        (directly to global namespace)
    "config": configuration options to pass to the _init method of the module
        (optional)
}

"""


# -----------------------------------------------------------------------------
#
#                             Module Configuration
#
# -----------------------------------------------------------------------------

MODULES = [

    # -- Math -----------------------------------------------------------------

    {
        "name": "std_math",
        "namespace": None,
        "config": {
            "degree_mode": True
        },
    },

    # -- Phasors --------------------------------------------------------------
    {
        "name": "phasor",
        "namespace": None,
        "config": {
            "enable_unicode": False,
        }
    },

    # -- Numpy ----------------------------------------------------------------
    {
        "name": "numpy",
        "namespace": "np",
    },

]
