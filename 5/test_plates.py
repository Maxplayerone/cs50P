import plates

def test_too_short():
    assert plates.is_valid("a") == False

def test_too_long():
    assert plates.is_valid("aaaaaaa") == False

def test_disalowed_character():
    assert plates.is_valid("aaa???") == False

def test_characters_after_numbers():
    assert plates.is_valid("aa55aa") == False

def test_normal():
    assert plates.is_valid("aaa555") == True

