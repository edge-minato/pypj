import pytest
from pytest_mock import MockFixture

from pypj import main
from tests.conftest import dummy_input


def test_windows(mocker: MockFixture) -> None:
    mocker.patch("platform.system", return_value="Windows")
    mocker.patch("builtins.input", side_effect=dummy_input(["N"]))
    with pytest.raises(SystemExit) as e:
        main.process()
        assert e.value.code == 0  # type: ignore
