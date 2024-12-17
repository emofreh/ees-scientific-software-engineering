import numpy as np
import pytest

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
    input_array = np.array([5.0, 4.0, 3.0])
    expected_result = np.sqrt((5.0**2 + 4.0**2 + 3.0**2) / 3)  # RMS formula
    assert np.isclose(rms(input_array), expected_result)  # Assert that the results is as expected


def test_rms_arraytype():
    # Test case 1: Input array of integers
    input_array = [5.0, 4.0, 3.0]
    with pytest.raises(TypeError, match="Array must be of type np.ndarray"):
        rms(input_array)


def test_rms_dimension():
    # Test case 1: Input array of integers
    input_array = np.array([[5.0], [4.0], [3.0]])
    with pytest.raises(TypeError, match="Array must be one dimensional"):
        rms(input_array)


def test_rms_error_nan():
    with pytest.raises(ValueError, match="input array cannot contain nans!") as error:
        input_array = np.array([np.nan, 4.0, 3.0])
        rms(input_array)


def test_rms_error_inf():
    with pytest.raises(ValueError, match="input array cannot contain ninfinite values!") as error:
        input_array = np.array([np.inf, 4.0, 3.0])
        rms(input_array)
