#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return int(self) != other

    def __ne__(self, other):
        """Inverts the != operator."""
        return int(self) == other
