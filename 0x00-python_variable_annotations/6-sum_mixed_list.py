#!/usr/bin/env python3
"""This module conatins a single function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums all the values of the list"""
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum
