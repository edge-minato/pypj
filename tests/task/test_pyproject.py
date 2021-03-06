from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PackageName, PypjSetting
from pypj.task.pyproject import Pyproject
from tests.conftest import does_contain_specific_words, prepare_dir, validate_toml


def test_pyproject() -> None:
    # prepare
    PACKAGE = PackageName("test_pyproject")
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
    with pyproject.open(mode="r") as f:
        content = f.read()
    assert not does_contain_specific_words(content)
