# pylint: disable=E2208, W0614, W0401
from index import *
from _pytest.monkeypatch import MonkeyPatch


def test_hello_world():
    assert hello_world() == "<p>Hello, World!</p><button onclick='this.parentElement.append(\"Click\")'>Add</button>"


def mock_say_hello(username):
    return "Hi, " + username


def test_hello_user():
    # pylint: disable=E1120,E0602
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr("hello.say_hello", mock_say_hello)
    assert hello_user("Boris") == "Hi, Boris"
