from collections import deque
from os import chdir
from pathlib import Path
from subprocess import PIPE, run
from typing import Any

import pytest
from pytest_mock import MockFixture

from pypj import args, main


def test_process(mocker: MockFixture) -> None:
    PACKAGE = "tmp_package"
    user_input = deque(["N", PACKAGE])

    def dummy_input() -> str:
        r = user_input.pop()
        print(r)
        return r

    class DummyReturn:
        def __init__(self, returncode: int) -> None:
            self.returncode: int = returncode

    def dummy_command(cmd: str) -> DummyReturn:
        if "poetry new" in cmd:
            r = run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
            return DummyReturn(r.returncode)
        else:
            return DummyReturn(0)

    mocker.patch("builtins.input", side_effect=dummy_input)
    mocker.patch("pypj.task.poetry.Poetry._Poetry__command", side_effect=dummy_command)
    # pushd
    cwd = Path().cwd().resolve()
    tmp = cwd.joinpath("tmp")
    chdir(tmp)
    # poetry new
    try:
        main.process()
    finally:
        # popd
        chdir(cwd)
    package_dir = tmp.joinpath(PACKAGE)
    assert not package_dir.joinpath("src").exists()
    assert package_dir.joinpath(PACKAGE).exists()


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
    def dummy_input() -> Any:
        print("N")
        return "N"

    mocker.patch("platform.system", return_value="Windows")
    mocker.patch("builtins.input", side_effect=dummy_input)
    with pytest.raises(SystemExit) as e:
        main.process()
        assert e.value.code == 0  # type: ignore
