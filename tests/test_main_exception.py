import pytest
from pytest_mock import MockFixture

from pypj import main
from pypj.exception import Emsg, PypjError


def test_keyboard_interrupt(mocker: MockFixture) -> None:
    def interrupt() -> None:
        raise KeyboardInterrupt()

    mocker.patch("builtins.input", side_effect=interrupt)
    with pytest.raises(SystemExit) as e:
        main.main()
        assert e.value.code == 1  # type: ignore


def test_error_in_main(mocker: MockFixture) -> None:
    def pypj_error() -> None:
        raise PypjError(Emsg.OS_NOT_SUPPORTED)

    def keyboard_interapt_error() -> None:
        raise KeyboardInterrupt()

    def other_error() -> None:
        raise ValueError()

    mocker.patch("pypj.main.args", side_effect=pypj_error)
    with pytest.raises(SystemExit) as e:
        main.main()
        assert e.value.code == 1  # type: ignore
    mocker.patch("pypj.main.args", side_effect=KeyboardInterrupt)
    with pytest.raises(SystemExit) as e:
        main.main()
        assert e.value.code == 1  # type: ignore

    mocker.patch("pypj.main.args", side_effect=other_error)
    with pytest.raises(ValueError):
        main.main()
