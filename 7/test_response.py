import response

def test_valid():
    assert response.validate("poop.fart@gmail.com") == "Valid"

def test_no_email():
     assert response.validate("Oh the misery, everybody wants to be my enemyyyyyyyy") == "Invalid"

def tes_email_in_a_sentence():
    assert response.validate("Hey man, my email is itchy_balls23@gmail.com") == "Invalid"