import fuel

def test_no_backslash():
    assert fuel.convert("1234") == "No backslash error"

def test_disalowed_characters():
    assert fuel.convert("asweerjf") == "disalowed characters error"

def test_division_by_zero():
    assert fuel.convert("0/0") == "division by zero error"

def test_value_bigger_than_one():
    assert fuel.convert("2/1") == "value bigger than 1"

def test_normal():
    assert fuel.convert("3/4") == "75.0%"