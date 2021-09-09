from collections import deque
from os import chdir
from pathlib import Path

from pytest_mock import MockFixture

from pypj import main
from tests.conftest import dummy_command


def src_dir_exists(package_dir: Path) -> bool:
    return package_dir.joinpath("src").exists()


def readme_exists(package_dir: Path) -> bool:
    c1 = package_dir.joinpath("README.md").exists()
    c2 = not package_dir.joinpath("README.rst").exists()
    return c1 and c2


def vscode_exists(package_dir: Path) -> bool:
    return package_dir.joinpath(".vscode").joinpath("settings.json").exists()


def makefile_exists(package_dir: Path) -> bool:
    return package_dir.joinpath("Makefile").exists()


def github_exists(package_dir: Path) -> bool:
    github_dir = package_dir.joinpath(".github")
    github_wf_dir = github_dir.joinpath("workflows")
    c1 = github_dir.joinpath("dependabot.yml").exists()
    c2 = github_wf_dir.joinpath("unittest.yml").exists()
    c3 = github_wf_dir.joinpath("publish.yml").exists()
    return c1 and c2 and c3


def test_default(mocker: MockFixture) -> None:
    PACKAGE = "tmp_package_default"
    user_input = deque(
        [
            PACKAGE,  # package name
            "N",  # customize
            "Y",  # confirmation
        ]
    )

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
    assert package_dir.joinpath(PACKAGE).exists()
    assert not src_dir_exists(package_dir)
    assert github_exists(package_dir)
    assert readme_exists(package_dir)
    assert vscode_exists(package_dir)
    assert makefile_exists(package_dir)


def test_use_src(mocker: MockFixture) -> None:
    PACKAGE = "tmp_package_use_src"
    user_input = deque(
        [
            PACKAGE,  # package name
            "Y",  # customize
            "999",  # max line length
            "Y",  # use src dir
            "Y",  # venv in pj
            "N",  # github workflow
            "N",  # vscode setting
            "N",  # Makefile
            "Y",  # confirmation
        ]
    )

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
    assert not package_dir.joinpath(PACKAGE).exists()
    assert src_dir_exists(package_dir)
    assert not github_exists(package_dir)
    assert readme_exists(package_dir)
    assert not vscode_exists(package_dir)
    assert not makefile_exists(package_dir)
