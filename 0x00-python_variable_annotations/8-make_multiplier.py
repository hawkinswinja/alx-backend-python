#!/usr/bin/env python3
"""This module contains a single function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies """
    def sqrd(n: float) -> float:
        """returns the square of n"""
        return n**2
    return sqrd
