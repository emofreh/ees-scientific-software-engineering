import pytest
import numpy

from ees_scientific_software_engineering.simple_function import add, multiply, rms


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
    input_array = np.array([5, 4, 3])
    expected_result = np.sqrt((5**2 + 4**2 + 3**2) / 3)  # RMS formula
    assert np.isclose(rms(input_array), expected_result), 
