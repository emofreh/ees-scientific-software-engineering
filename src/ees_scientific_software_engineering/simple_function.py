"""
A module with simple function
"""

import numpy as np


class RMSError(Exception):
    """RMS ERROR"""

    pass


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
    if not isinstance(input_array, np.ndarray):
        raise TypeError("Array must be of type np.ndarray")
    if input_array.ndim != 1:
        raise TypeError("Array must be one dimensional")
    if any(np.isnan(input_array)):
        raise ValueError("input array cannot contain nans!")
    if any(np.isinf(input_array)):
        raise ValueError("input array cannot contain ninfinite values!")

    if not input_array.dtype == np.float64:
        raise RMSError("Dtype error: correct it!")

    squared = input_array**2
    sum_squared = np.sum(squared)
    a = sum_squared / (input_array.size)
    a = np.sqrt(a)
    return a
