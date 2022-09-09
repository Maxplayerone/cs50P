import bank

def test_hello():
    assert bank.get_value("hello") == 100

def test_h():
    assert bank.get_value("h") == 20

def test_h_no_start():
    #if we have an h letter but it is not at the start 
    #the program should not give any points
    assert bank.get_value("ah") == 0

def test_wrong_value():
    assert bank.get_value("I do not know what to put in here") == 0
