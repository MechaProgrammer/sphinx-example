"""This module is for example purposes. This text here shows as a module docstring."""
import deprecation

from ._version import __version__


class ExampleClass:
    """Example class

    Args:
        a (float): a is float and it will do things.
        b (str): b is a string which length can be anything.

    Raises:
        ValueError: If a > 10.

    .. versionadded:: 0.0.1
       The `b` parameter was added.
    """
    def __init__(self, a: float, b: str):
        if a > 10:
            raise ValueError('a > 10')
        self.a = a
        self.b = b

    def a_method(self, c: int):
        """This is a method.

        Args:
            c (int): c is an integer and is raised to the power of 2.

        Returns:
            int: Integer value.

        Example:
            >>> obj = ExampleClass(1, 'bar')
            >>> print(obj.a_method(2))
            4
        """
        return c**2

    @deprecation.deprecated(
        deprecated_in="0.0.1", removed_in="0.0.2",
        current_version=__version__,
        details="Useless function, so no harm done.")
    def b_method(self):
        """This is a b method."""
        pass
