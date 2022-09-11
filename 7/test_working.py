import working

def test_valid_only_hours():
    assert working.convert("9 AM to 5 PM") == "9:00 to 17:00"

def test_valid_hours_and_minutes():
    assert working.convert("9:00 AM to 5:45 PM") == "9:00 to 17:45"

def test_minutes_overflow():
    assert working.convert("9:15 AM to 7:69 PM") == None

def test_no_spaces():
    assert working.convert("9AMto5PM") == None

def test_lowercase_hours():
    assert working.convert("9 am to 5 pm") == None

def test_hours_overflow():
    assert working.convert("1 AM to 13 PM") == None