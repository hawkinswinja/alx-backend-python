#!/usr/bin/env python3
"""this module cpntains a single function wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """awaits for max_delay seconds before returning it"""
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
