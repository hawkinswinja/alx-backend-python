#!/usr/bin/env python3
"""This module conatins a single function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums all the values of the list"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
