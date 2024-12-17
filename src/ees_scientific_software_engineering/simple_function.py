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
    """Finds RMS value"""
    if any(np.isnan(input_array)):
        raise ValueError("input array cannot contain nans!")
    if any(np.isinf(input_array)):
        raise ValueError("input array cannot contain ninfinite values!")
    squared = input_array**2
    sum_squared = np.sum(squared)
    a = sum_squared / (input_array.size)
    a = np.sqrt(a)
    return a
