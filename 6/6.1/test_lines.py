import lines

def test_incorrect_filename():
    assert lines.count_lines("itdoesnotexist.lol") == -1

def test_file_not_python():
    assert lines.count_lines("notpythonprogram.cpp") == -1

#we checking the same file (but the second one doesn't have whitespaces etc.)
#so the results should be the same
def test_correct():
    assert lines.count_lines("dummy.py") == 39

def test_correct_no_comments_or_whitespaces():
    assert lines.count_lines("dummy2.py") == 39


def test_only_whitespaces():
    assert lines.count_lines("blank.py") == 0

def test_only_comments():
    assert lines.count_lines("comments.py") == 0