
"""Basic system utilities

Attributes
----------
ls : str
    Contents of the current directory; fetched at module load.
"""

import os
import sys


def _init(config):
    """Returns a print statement for module info"""

    def pf():
        print("  > Type 'exit' to exit, or 'man' for more information.")
    return pf


class _ListDir():
    """Class to hijack the ``ls`` keyword to list directory contents"""

    def __str__(self):
        return self._get_cwd()

    def __repr__(self):
        print(self._get_cwd())
        return ""

    def _get_cwd(self):
        """Get current working directory, and return as a formatted string."""

        cwd = os.getcwd()
        contents = os.listdir(cwd)

        return (
            "Current directory: {cwd}\nDirectory contents:\n    "
            .format(cwd=cwd) + "\n    ".join(contents))


class _Exit():
    """Class to hijack the ``exit`` keyword to exit without needing
    to type ``exit()``"""

    def __repr__(self):
        sys.exit(1)


class _Man():
    """Class to hijack the ``man`` keyword to show directory information"""

    def __repr__(self):
        print("""<util.py> keywords:
    exit        Exit python
    ls          List current directory
    man         This command
    cd(path)    Change current directory""")
        return ""


ls = _ListDir()
exit = _Exit()
man = _Man()


def cd(path):
    """Function to change directory"""
    os.chdir(path)
