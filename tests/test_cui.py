from pytest_mock import MockerFixture

from pypj import cui

YES = ["y", "Y", "yes", "Yes", "YES"]
NO = ["n", "N", "no", "No", "NO"]


def test_is_yes() -> None:
    for r in YES:
        assert cui.is_yes(r)
    for r in NO:
        assert not cui.is_yes(r)
    assert not cui.is_yes("")


def test_is_no() -> None:
    for r in NO:
        assert cui.is_no(r)
    for r in YES:
        assert not cui.is_no(r)
    assert not cui.is_no("")


def test_is_yes_or_no() -> None:
    for r in YES:
        assert cui.is_yes_or_no(r)
    for r in NO:
        assert cui.is_yes_or_no(r)
    assert not cui.is_yes_or_no("aaa")
    assert not cui.is_yes_or_no("")


def test_is_empty() -> None:
    assert cui.is_empty("")
    assert not cui.is_empty("a")


def test_can_be_int() -> None:
    assert cui.can_be_int("1")
    assert not cui.can_be_int("")
    assert not cui.can_be_int("a")


def test_ask_with_default(mocker: MockerFixture) -> None:
    mocker.patch("builtins.input", return_value="")
    assert cui.ask_with_default("test", "default") == "default"
    mocker.patch("builtins.input", return_value="sample")
    assert cui.ask_with_default("test", "default") == "sample"


def test_ask_with_default_num(mocker: MockerFixture) -> None:
    mocker.patch("builtins.input", return_value="")
    assert cui.ask_with_default_num("test", 100) == 100
    mocker.patch("builtins.input", return_value="50")
    assert cui.ask_with_default_num("test", 100) == 50


def test_ask_yn(mocker: MockerFixture) -> None:
    mocker.patch("builtins.input", return_value="")
    assert cui.ask_yn("test", default=True) is True
    assert cui.ask_yn("test", default=False) is False
    mocker.patch("builtins.input", return_value="Y")
    assert cui.ask_yn("test", default=True) is True
    assert cui.ask_yn("test", default=False) is True
    mocker.patch("builtins.input", return_value="N")
    assert cui.ask_yn("test", default=True) is False
    assert cui.ask_yn("test", default=False) is False


def test_ask_Yn(mocker: MockerFixture) -> None:
    mocker.patch("builtins.input", return_value="")
    assert cui.ask_Yn("test") is True
    mocker.patch("builtins.input", return_value="Y")
    assert cui.ask_Yn("test") is True
    mocker.patch("builtins.input", return_value="N")
    assert cui.ask_Yn("test") is False


def test_ask_yN(mocker: MockerFixture) -> None:
    mocker.patch("builtins.input", return_value="")
    assert cui.ask_yN("test") is False
    mocker.patch("builtins.input", return_value="Y")
    assert cui.ask_yN("test") is True
    mocker.patch("builtins.input", return_value="N")
    assert cui.ask_yN("test") is False
