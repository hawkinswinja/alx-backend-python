#!/usr/bin/env python3
"""This module contains a single function async_comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of random numbers"""
    return [i async for i in async_generator()]
