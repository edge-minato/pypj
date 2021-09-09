from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task.readme import Readme
from tests.conftest import prepare_dir


def test_readme() -> None:
    # prepare
    PACKAGE = "test_readme"
    package_dir = prepare_dir(PACKAGE)
    readme_rst = package_dir.joinpath("README.rst")
    readme_rst.touch()
    readme_md = package_dir.joinpath("README.md")
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Readme(setting, filepath).execute()
    # assert
    assert not readme_rst.exists()
    assert readme_md.exists()
    assert readme_md.stat().st_size > 0
