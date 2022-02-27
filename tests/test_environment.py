import pytest
from pytest_mock import MockerFixture

from pypj import Environment, Platform, Version


def test_Environment(mocker: MockerFixture) -> None:
    env = Environment()
    assert env.python.major == "3"

    mocker.patch("pypj.environment.platform.system", return_value="Others")
    mocker.patch("builtins.input", return_value="N")
    with pytest.raises(SystemExit) as e:
        _ = Environment()
    assert e.value.code == 0

    mocker.patch("builtins.input", return_value="Y")
    env3 = Environment()
    assert env3.os == Platform.OTHERS
    assert env3.poetry is not None
    assert env3.python.major == "3"


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


def test_Version_exception() -> None:
    with pytest.raises(ValueError):
        Version("1")


def test_no_poetry_found(mocker: MockerFixture) -> None:
    mocker.patch("shutil.which", return_value=None)
    with pytest.raises(SystemExit) as e:
        Environment()
    assert e.value.code == 1  # type: ignore


def test_Plarform() -> None:
    w = Platform.WINDOWS
    assert w.name == "WINDOWS"
