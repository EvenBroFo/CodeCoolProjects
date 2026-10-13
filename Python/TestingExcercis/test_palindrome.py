import pytest
from palindrome import *

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_not_palindrome():
    assert is_palindrome("hello") == False

def test_mixed_case():
    assert is_palindrome("RaceCar") == True

def test_empty_str():
    assert is_palindrome("") == True

def test_single_char():
    assert is_palindrome("D") == True

def test_punct():
    assert is_palindrome("O.P.P.O") == True

def test_space():
    assert is_palindrome("nurses run") == True




