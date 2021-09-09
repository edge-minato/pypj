from typing import Any

import pytest
from pytest_mock import MockFixture

from pypj import args, main


def test_args(mocker: MockFixture) -> None:
    class Arg:
        def __init__(self) -> None:
            self.version = True

    mocker.patch("argparse.ArgumentParser.parse_args", return_value=Arg())
    with pytest.raises(SystemExit) as e:
        args.args()
        assert e.value.code == 0  # type: ignore


def test_windows(mocker: MockFixture) -> None:
    def dummy_input() -> Any:
        print("N")
        return "N"

    mocker.patch("platform.system", return_value="Windows")
    mocker.patch("builtins.input", side_effect=dummy_input)
    with pytest.raises(SystemExit) as e:
        main.process()
        assert e.value.code == 0  # type: ignore
