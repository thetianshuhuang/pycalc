
"""Utility mixins for creating new math types"""


class MathCompareMixin:
    """Rich comparison method definitions

    These mixins assume the base class already has a __abs__ value function
    and a __eq__ function.
    """

    def __lt__(self, b):
        return self.__abs__() < b.__abs__()

    def __le__(self, b):
        return self.__abs__() <= b.__abs__()

    def __ne__(self, b):
        return not self.__eq__(b)

    def __ge__(self, b):
        return self.__abs__() >= b.__abs__()

    def __gt__(self, b):
        return self.__abs__() > b.__abs__()


class MathInPlaceMixin:
    """In place math mixins

    All for +=, /=, *=, and -= operations, assuming the appropriate
    arithmetic operators are already implemented.
    """

    def __iadd__(self, b):
        return self.__add__(b)

    def __radd__(self, b):
        return self.__add__(b)

    def __itruediv__(self, b):
        return self.__truediv__(b)

    def __rtruediv__(self, b):
        return self.__truediv__(b)

    def __imul__(self, b):
        return self.__mul__(b)

    def __rmul__(self, b):
        return self.__rmul__(b)

    def __isub__(self, b):
        return self.__sub__(b)

    def __rsub__(self, b):
        return self.__sub__(b)
