import pytest
from pytest_mock import MockFixture

from pypj import main


def test_keyboard_interrupt(mocker: MockFixture) -> None:
    def interrupt() -> None:
        raise KeyboardInterrupt()

    mocker.patch("builtins.input", side_effect=interrupt)
    with pytest.raises(SystemExit) as e:
        main.main()
        assert e.value.code == 1  # type: ignore


def test_unknown_error(mocker: MockFixture) -> None:
    def error() -> None:
        raise Exception("Unknown error")

    mocker.patch("builtins.input", side_effect=error)
    with pytest.raises(SystemExit) as e:
        main.main()
        assert e.value.code == 2  # type: ignore
