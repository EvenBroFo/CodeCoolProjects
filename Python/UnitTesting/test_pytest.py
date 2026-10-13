import pytest
from Math import *

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 5

def test_muliply():
    assert multiply(2, 3) == 6

def test_divide():
    with pytest.raises(ValueError):
        divide(10, 1)
