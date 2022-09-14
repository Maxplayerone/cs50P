import seasons
from datetime import date

def test_valid_date():
    assert seasons.get_dates_object_types("2019-12-04") == date.fromisoformat("2019-12-04")

def test_wrong_format():
    assert seasons.get_dates_object_types("1999-3-4") == None

def test_month_overflow():
    assert seasons.get_dates_object_types("2019-13-04") == None

def test_day_overflow():
    assert seasons.get_dates_object_types("1420-04-32") == None