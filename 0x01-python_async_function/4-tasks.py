#!/usr/bin/env python3
"""This module defines ta single function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """this function runs wait_random n times"""
    tasks: List[float] = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    return sorted(tasks)
