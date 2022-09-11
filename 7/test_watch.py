#http://youtube.com/embed/xvFZjo5PgG0
#https://youtube.com/embed/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0
import watch

def test_valid_normal():
    assert watch.parse("https://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"

def test_valid_http():
    assert watch.parse("http://youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"

def test_valid_www():
    assert watch.parse("https://www.youtube.com/embed/xvFZjo5PgG0") == "https://youtu.be/xvFZjo5PgG0"

def test_wrong_backslashes():
    assert watch.parse("https:/youtube.com/embed/xvFZjo5PgG0") == None

def test_no_embed():
    assert watch.parse("https://youtube.com/xvFZjo5PgG0") == None

def test_different_website():
    assert watch.parse("https:://google.com") == None

def test_whole_sentence():
     assert watch.parse(" the link is https://youtube.com/embed/xvFZjo5PgG0") == None