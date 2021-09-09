from pathlib import Path

from pytest_mock import MockFixture

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task.pyproject import Pyproject
from tests.conftest import prepare_dir, validate_toml


def test_pyproject(mocker: MockFixture) -> None:
    # prepare
    PACKAGE = "test_pyproject"
    package_dir = prepare_dir(PACKAGE)
    pyproject = package_dir.joinpath("pyproject.toml")
    pyproject.touch()
    # execute
    mocker.patch("builtins.input", return_value=PACKAGE)
    setting = PypjSetting(Version("0.0.0"))
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Pyproject(setting, filepath).execute()
    # assert
    assert pyproject.exists()
    assert validate_toml(pyproject)
