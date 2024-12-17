import numpy as np
import pytest

from ees_scientific_software_engineering.simple_function import add, multiply, rms, RMSError


def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4


def test_add_error():
    a = 1.0
    b = 1
    with pytest.raises(TypeError, match="Arguments should be integers!"):
        add(a, b)


def test_rms():
    # Test case 1: Input array of integers
    input_array = np.array([5.0, 4.0, 3.0])
    expected_result = np.sqrt((5.0**2 + 4.0**2 + 3.0**2) / 3)  # RMS formula
    assert np.isclose(rms(input_array), expected_result)  # Assert that the results is as expected


def test_rms_incorrect_type():
    """Test with incorrect input type (not float64)."""
    input_array = np.array([1, 2, 3], dtype=np.int64) # or any other type
    with pytest.raises(RMSError, match='Dtype error: correct it!') as excinfo:
        rms(input_array)