#!/usr/bin/env python3
"""This module ocntains a single function task_wait_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create a tan asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
