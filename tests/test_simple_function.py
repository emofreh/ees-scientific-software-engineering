import pytest

from ees_scientific_software_engineering.simple_function import add, multiply, rms
import numpy as np

def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4

def test_rms():
    assert rms(np.array([3, 3])) == 3


def test_add_error():
    a = 1.0
    b = 1
    with pytest.raises(TypeError, match="Arguments should be integers!"):
        add(a, b)
