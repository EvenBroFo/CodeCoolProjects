import pytest
from password_validator import *

def test_length():
    assert is_valid_password("Valid123!") is True
    assert is_valid_password("Va1!abc") is False


def test_uppercase():
    assert is_valid_password("Valid123!") is True
    assert is_valid_password("valid123!") is False


def test_lowercase():
    assert is_valid_password("Valid123!") is True
    assert is_valid_password("VALID123!") is False


def test_digit():
    assert is_valid_password("Valid123!") is True
    assert is_valid_password("Validabc!") is False


def test_special_character():
    assert is_valid_password("Valid123!") is True
    assert is_valid_password("Valid1234") is False