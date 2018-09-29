

import config
import importlib
import sys
pycalc = sys.modules[__name__]


_MODULE_VERSION = "V0.1"
_MODULE_INFO = "Tianshu Huang"


def load_module(module):

    if module["namespace"] is not None:

        setattr(
            pycalc,
            module["namespace"],
            importlib.import_module(module["name"]))

    else:

        merge_in = importlib.import_module(module["name"])

        # is there an __all__?  if so respect it
        if "__all__" in merge_in.__dict__:
            names = merge_in.__dict__["__all__"]
        else:
            # otherwise we import all names that don't begin with _
            names = [x for x in merge_in.__dict__ if not x.startswith("_")]

        globals().update({k: getattr(merge_in, k) for k in names})


def _pycalc_init():

    print("""
   ____         ____      _
  |  _ \ _   _ / ___|__ _| | ___
  | |_) | | | | |   / _` | |/ __|
  |  __/| |_| | |__| (_| | | (__
  |_|    \__, |\____\__,_|_|\___|
         |___/ {version} {info}
""".format(version=_MODULE_VERSION, info=_MODULE_INFO))

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
