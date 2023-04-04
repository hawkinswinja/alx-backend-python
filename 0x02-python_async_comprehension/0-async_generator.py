#!/usr/bin/env python3
"""this module contains a single function async_generator"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[int, None, None]:
    """creates a generator list"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
