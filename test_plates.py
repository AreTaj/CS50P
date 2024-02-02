# Re-requesting a Vanity Plate
# Problem Set 5

import plates
from plates import is_valid

def main():
    # Call all test functions.
    test_is_valid_len()
    test_is_valid_start()
    test_is_valid_numbers()
    test_is_valid_zero()
    test_is_valid_punctuation()

def test_is_valid_len():
    # Test for length [2,6]
    assert is_valid("AA") == True
    assert is_valid("ALPHAB") == True
    assert is_valid("A") == False
    assert is_valid("ALPHABETICAL") == False

def test_is_valid_start():
    # Test for start with two letters.
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False

def test_is_valid_numbers():
    # Test for numbers only at end.
    assert is_valid("AAA222") == True
    assert is_valid("AA222A") == False

def test_is_valid_zero():
    # Test for zero only last number.
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_is_valid_punctuation():
    # Test for exclude all punctuation.
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False
