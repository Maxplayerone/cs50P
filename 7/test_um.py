import um

def test_valid():
    assert um.count("hello, um, world") == 1

def test_only_um():
    assert um.count("um") == 1

#technically it shouldn't work because 
#any um in a word is not um
def test_only_um_multiple_times():
    assert um.count("umumumumumumum") == 0

def test_no_um():
    assert um.count("This is a normal sentece") == 0

def test_multiple_um():
    assert um.count("So, um, I, um, you know, um, ridin in my, um, fiat") == 4