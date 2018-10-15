
"""Pycalc Main File"""

import config
import importlib
import sys
pycalc = sys.modules[__name__]


_MODULE_VERSION = "V0.3"
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


def load_module(config):
    """Load a module with parameters specified in a dictionary.

    Parameters
    ----------
    module : dict
        Module configuration, as specified by ``config.py``.
    """

    module = importlib.import_module(config["name"])

    # Run config
    if hasattr(module, "_init"):
        module._init(config["config"] if "config" in config else {})

    # Not an 'import *'
    if config["namespace"] is not None:
        setattr(pycalc, config["namespace"], module)

    # Import * -> merge into globals
    else:

        # Check for __all__ variable, and follow if present
        if "__all__" in module.__dict__:
            names = module.__dict__["__all__"]
        else:
            # Import all names not starting with '_'
            names = [
                name for name in module.__dict__
                if not name.startswith("_")]

        globals().update(
            {name: getattr(module, name) for name in names})


def _pycalc_init():
    """Closure to initialize
       ____         ____      _
      |  _ \ _   _ / ___|__ _| | ___
      | |_) | | | | |   / _` | |/ __|
      |  __/| |_| | |__| (_| | | (__
      |_|    \__, |\____\__,_|_|\___|
             |___/
    """

    _splash()

    print(
        "Using Python {major}.{minor}.{micro}."
        .format(
            major=sys.version_info.major,
            minor=sys.version_info.minor,
            micro=sys.version_info.micro))

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

    print("")


_pycalc_init()
