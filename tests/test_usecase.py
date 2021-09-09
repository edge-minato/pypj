from collections import deque
from os import chdir
from pathlib import Path

from pytest_mock import MockFixture

from pypj import main
from tests.conftest import dummy_command


def test_default(mocker: MockFixture) -> None:
    PACKAGE = "tmp_package_default"
    user_input = deque([PACKAGE, "N"])

    def dummy_input() -> str:
        r = user_input.popleft()
        print(r)
        return r

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


def test_use_src(mocker: MockFixture) -> None:
    PACKAGE = "tmp_package_use_src"
    user_input = deque([PACKAGE, "Y", "999", "Y", "Y", "Y"])

    def dummy_input() -> str:
        r = user_input.popleft()
        print(r)
        return r

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
    assert package_dir.joinpath("src").exists()
    assert not package_dir.joinpath(PACKAGE).exists()
