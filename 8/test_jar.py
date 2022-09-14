import jar

_jar = jar.Jar(100)
def test_deposit_overflow():
    assert _jar.deposit(101) == None

def test_widthdraw_overflow():
    assert _jar.withdraw(101) == None

def test_amount_is_not_int():
    assert _jar.deposit("A string") == None

def test_cookie_count():
    _jar.deposit(10)
    assert _jar.__str__() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"