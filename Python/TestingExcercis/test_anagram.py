import pytest
from anagram import *

def test_simple_anagram():
    assert is_anagram("listen", "silent") == True

def test_not_anagram():
    assert is_anagram("Darth", "Vader") == False

def test_different_lengths():
    assert is_anagram("apple", "app") == False

def test_mixed_case():
    assert is_anagram("Listen", "Silent") == True

def test_repeated_letters():
    assert is_anagram("aabb", "abab") == True

def test_empty_str():
    assert is_anagram("", "") == True

