#!/usr/bin/env python3
"""this module defines a single function wait_n"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """this function runs wait_random n times"""
    return await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
