import pytest
from fizzbuzz import *

def test_normal_numbers():
    assert fizzbuzz(2) == ["1", "2"]


def test_fizz():
    assert fizzbuzz(3) == ["1", "2", "Fizz"]


def test_buzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fizzbuzz():
    assert fizzbuzz(15)[-1] == "FizzBuzz"

def test_zero():
    with pytest.raises(ValueError):
        fizzbuzz(0)


def test_negative():
    with pytest.raises(ValueError):
        fizzbuzz(-5)


def test_non_integer():
    with pytest.raises(ValueError):
        fizzbuzz("hello")

