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
            "degree_mode": True,
            "complex_alias": True,
        },
    },

    # -- System Utilities -----------------------------------------------------
    {
        "name": "util",
        "namespace": None,
    },

    # -- Phasors --------------------------------------------------------------
    {
        "name": "phasor",
        "namespace": None,
        "config": {
            "enable_unicode": False,
            "degree_mode": True,
            "precision": 3,
        }
    },

    # -- AC Circuits ----------------------------------------------------------
    {
        "name": "circuits",
        "namespace": "ac",
        "config": {
            "abbreviate_names": True,
            "use_w": True,
        }
    },

    # -- Numpy ----------------------------------------------------------------
    {
        "name": "numpy",
        "namespace": "np",
    },
]
