#!/usr/bin/env python3
"""This module contains a single function measure_time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the time taken to run wait_n"""
    starttime: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - starttime) / n
