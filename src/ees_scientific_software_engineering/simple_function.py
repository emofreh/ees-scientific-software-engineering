"""
A module with simple function
"""

import numpy as np


def add(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a: number a
        b: number b

    Returns:
        added number
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments should be integers!")
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


def rms(input_array: np.ndarray) -> float:
    squared = input_array**2
    sum_squared = np.sum(squared)
    rms = sum_squared / (input_array.size)
    return rms
