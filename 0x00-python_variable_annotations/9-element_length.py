#!/usr/bin/env python3
"""this module contains a single function element_length"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples of item and its length"""
    return [(i, len(i)) for i in lst]
