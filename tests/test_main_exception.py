import pytest
from pytest_mock import MockFixture

from pypj import main
from tests.conftest import pypj_error


def test_keyboard_interrupt(mocker: MockFixture) -> None:
    mocker.patch("pypj.main.args", side_effect=KeyboardInterrupt)
    with pytest.raises(SystemExit) as e:
        main.main()
    assert e.value.code == 1  # type: ignore


def test_error_in_main(mocker: MockFixture) -> None:
    mocker.patch("pypj.main.args", side_effect=pypj_error)
    with pytest.raises(SystemExit) as e:
        main.main()
    assert e.value.code == 1  # type: ignore

    mocker.patch("pypj.main.args", side_effect=KeyboardInterrupt)
    with pytest.raises(SystemExit) as e:
        main.main()
    assert e.value.code == 1  # type: ignore

    mocker.patch("pypj.main.args", side_effect=ValueError)
    with pytest.raises(SystemExit) as e:
        main.main()
    assert e.value.code == 1  # type: ignore
