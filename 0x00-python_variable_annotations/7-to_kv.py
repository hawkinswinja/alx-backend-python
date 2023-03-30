#!/usr/bin/env python3
"""This module contains a single function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of k and the square of v"""
    return tuple([k, v**2])
