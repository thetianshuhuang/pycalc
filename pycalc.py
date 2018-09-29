
"""Pycalc Main File"""

import config
import importlib
import sys
pycalc = sys.modules[__name__]


_MODULE_VERSION = "V0.1"
_MODULE_INFO = "Tianshu Huang"


def _splash():
    """Print splash text"""
    print("""
   ____         ____      _
  |  _ \ _   _ / ___|__ _| | ___
  | |_) | | | | |   / _` | |/ __|
  |  __/| |_| | |__| (_| | | (__
  |_|    \__, |\____\__,_|_|\___|
         |___/ {version} {info}
""".format(version=_MODULE_VERSION, info=_MODULE_INFO))


def load_module(module):
    """Load a module with parameters specified in a dictionary.

    Parameters
    ----------
    module : dict
        Module configuration, as specified by ``config.py``.
    """

    # Not an 'import *'
    if module["namespace"] is not None:

        setattr(
            pycalc,
            module["namespace"],
            importlib.import_module(module["name"]))

    # Import * -> merge into globals
    else:

        merge_in = importlib.import_module(module["name"])

        # Check for __all__ variable, and follow if present
        if "__all__" in merge_in.__dict__:
            names = merge_in.__dict__["__all__"]
        else:
            # Import all names not starting with '_'
            names = [
                name for name in merge_in.__dict__
                if not name.startswith("_")]

        globals().update(
            {name: getattr(merge_in, name) for name in names})


def _pycalc_init():
    """Closure to initialize
       ____         ____      _
      |  _ \ _   _ / ___|__ _| | ___
      | |_) | | | | |   / _` | |/ __|
      |  __/| |_| | |__| (_| | | (__
      |_|    \__, |\____\__,_|_|\___|
             |___/
    """

    success = 0
    for module in config.MODULES:

        try:
            load_module(module)
            print(
                "Module <{name}> loaded successfully."
                .format(name=module["name"]))
            success += 1

        except ImportError:
            print(
                "Module <{name}> could not be loaded."
                .format(name=module["name"]))

    print(
        "{n} modules specified ({s} loaded successfully)."
        .format(n=len(config.MODULES), s=success))


_pycalc_init()
