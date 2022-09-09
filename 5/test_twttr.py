import twttr

def test_no_vowels():
    assert twttr.shorten("qwrtpsdfghjklzxcvbnm") == "qwrtpsdfghjklzxcvbnm"

def test_vowels():
    assert twttr.shorten("eyuioa") == ''

def test_every_letter():
    assert twttr.shorten("hello") == "hll"