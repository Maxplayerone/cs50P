import numb3rs

def test_valid():
    assert numb3rs.validate("245.63.128.16") == True

def test_too_high_numbers():
    assert numb3rs.validate("265.420.1337.999") == False

def test_no_numbers():
    assert numb3rs.validate("....") == False

def test_letters():
    assert numb3rs.validate("amogus.thomas.the.train") == False

def test_more_than_four_dots():
    assert numb3rs.validate("255.255.255.255.255.255") == False

def test_something_completely_different():
    assert numb3rs.validate("this is a random string of text") == False