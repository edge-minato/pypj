from collections import deque
from os import chdir
from pathlib import Path
from shutil import rmtree
from typing import Any

import pytest
from pytest_mock import MockFixture

from pypj import Environment, args, main
from pypj.environment import Platform


def test_process(mocker: MockFixture) -> None:
    PACKAGE = "tmp_package"
    user_input = deque(["N", PACKAGE])

    def sample_input() -> Any:
        return user_input.pop()

    mocker.patch("builtins.input", side_effect=sample_input)
    tmp = Path("tmp").resolve()
    # mkdir tmp && cd tmp
    if tmp.exists():
        rmtree(tmp)
    tmp.mkdir()
    chdir(tmp)
    # pypj
    main.process()
    e_pyproject = Path("pyproject.toml").exists()
    assert e_pyproject
    # rm -rf tmp
    rmtree(tmp)


def test_args(mocker: MockFixture) -> None:
    class Arg:
        def __init__(self) -> None:
            self.version = True

    def empty(*args: Any) -> None:
        pass

    mocker.patch("argparse.ArgumentParser.parse_args", return_value=Arg())
    mocker.patch("sys.exit", side_effect=empty)
    args.args()


def test_windows(mocker: MockFixture) -> None:
    mock_env = Environment()
    mock_env.os = Platform.WINDOWS
    mocker.patch("pypj.main.Environment", return_value=mock_env)
    mocker.patch("builtins.input", return_value="N")
    with pytest.raises(SystemExit) as e:
        main.process()
        assert e.value.code == 0  # type: ignore
