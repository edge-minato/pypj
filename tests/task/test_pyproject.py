from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task.pyproject import Pyproject
from tests.conftest import prepare_dir, validate_toml


def test_pyproject() -> None:
    # prepare
    PACKAGE = "test_pyproject"
    package_dir = prepare_dir(PACKAGE)
    pyproject = package_dir.joinpath("pyproject.toml")
    pyproject.touch()
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Pyproject(setting, filepath).execute()
    # assert
    assert pyproject.exists()
    assert validate_toml(pyproject)
