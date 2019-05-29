
"""Pycalc Main File"""

import config
import importlib
import sys

from print import *

pycalc = sys.modules[__name__]


_MODULE_VERSION = "V1.1"
_MODULE_INFO = "Tianshu Huang"
_ERRORS = {}
_SUCCESS = {}


def _splash():
    """Print splash text"""
    print("""
     ____         ____      _
    |  _ \ _   _ / ___|__ _| | ___
    | |_) | | | | |   / _` | |/ __|
    |  __/| |_| | |__| (_| | | (__
    |_|    \__, |\____\__,_|_|\___|
           |___/ {version} {info}

""".format(version=_MODULE_VERSION, info=_MODULE_INFO), RED, BOLD)


def _load_module(config, silent=False):
    """Load a module with parameters specified in a dictionary.

    Parameters
    ----------
    module : dict
        Module configuration, as specified by ``config.py``.
    """

    module = importlib.import_module(config["name"])

    # Run config
    if hasattr(module, "_init"):
        status = module._init(
            config["config"] if "config" in config else {})
    else:
        status = None

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

    return status


def _pycalc_init(silent=False):
    """Closure to initialize
       ____         ____      _
      |  _ \ _   _ / ___|__ _| | ___
      | |_) | | | | |   / _` | |/ __|
      |  __/| |_| | |__| (_| | | (__
      |_|    \__, |\____\__,_|_|\___|
             |___/
    """

    if not silent:
        _splash()

        print(
            "Using Python {major}.{minor}.{micro}."
            .format(
                major=sys.version_info.major,
                minor=sys.version_info.minor,
                micro=sys.version_info.micro), BR + BLUE, BOLD)

    success = 0
    for module in config.MODULES:

        try:
            status = _load_module(module)

            if not silent:
                print(
                    "Module <{name}> loaded successfully."
                    .format(name=module["name"]), BR + GREEN)

                if hasattr(status, '__call__'):
                    status()

            success += 1
            _SUCCESS[module["name"]] = module

        except ImportError as e:

            if not silent:
                print(
                    "Module <{name}> could not be loaded."
                    .format(name=module["name"]), BR + RED)
                print(
                    "  > Call info(\"{name}\") to display the error message."
                    .format(name=module["name"]))

            else:
                print(
                    "Error loading module <" + module["name"] +
                    ">; load full pycalc shell for more information")

            # Save error
            _ERRORS[module["name"]] = e

    if not silent:
        print(
            "{n} modules specified ({s} loaded successfully)."
            .format(n=len(config.MODULES), s=success), BR + BLUE, BOLD)
        print("")

    sys.ps1 = render(">>> ", BR + RED, BOLD)
    sys.ps2 = render("... ", BR + BLACK)


def info(name):
    """Get the error for a module.

    Parameters
    ----------
    name : str
        Target module name

    Returns
    -------
    ImportError
        If error found; error generated on module load
    dict
        If no error found, but module was loaded
    None
        No module found
    """

    if name in _ERRORS:
        return _ERRORS[name]
    elif name not in _SUCCESS:
        print("No such module: <{name}>".format(name=name), BR + YELLOW)
        return None
    else:
        print(
            "Module <{name}> reported no errors.".format(name=name),
            BR + GREEN)
        return _SUCCESS[name]


if __name__ == "__main__":

    if len(sys.argv) < 2:
        _pycalc_init()

    else:
        _pycalc_init(silent=True)
        cmd = " ".join(sys.argv[1:])
        try:
            res = eval(cmd)
            print(
                render("[pycalc] ", BR + RED, BOLD) +
                render(cmd + " = ") +
                render(str(eval(cmd))), BOLD)
        except Exception as e:
            print(
                render("[pycalc] ", BR + RED, BOLD) +
                render(cmd))
            print(" => " + str(e), BR + RED, BOLD)
