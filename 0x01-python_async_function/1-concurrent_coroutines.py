#!/usr/bin/env python3
"""this module defines a single function wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """this function runs wait_random n times"""
    tasks: List[any] = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    return sorted(await asyncio.gather(*tasks))
