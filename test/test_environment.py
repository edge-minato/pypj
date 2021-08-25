from pypj import Environment, Version


def test_Environment() -> None:
    e = Environment()
    assert type(e) == Environment


def test_Version() -> None:
    v = Version("1.2.3")
    assert v.major == "1"
    assert v.minor == "2"
    assert v.patch == "3"
    assert str(v) == "1.2.3"
    v = Version("1.2")
    assert v.major == "1"
    assert v.minor == "2"
    assert v.patch == ""
    assert v.version == "1.2"
    v = Version("a.b.c")
    assert v.major == "a"
    assert v.minor == "b"
    assert v.patch == "c"
    assert str(v) == "a.b.c"
    v = Version("1-2-3", separator="-")
    assert v.major == "1"
    assert v.minor == "2"
    assert v.patch == "3"
    assert str(v) == "1-2-3"
