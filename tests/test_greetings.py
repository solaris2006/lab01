from greetings import farewell, greet


def test_greet_default():
    assert greet() == "hello, world"


def test_greet_name():
    assert greet("git") == "hello, git"


def test_farewell():
    assert farewell("git") == "bye, git"
