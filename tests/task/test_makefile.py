from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task.makefile import Makefile
from tests.conftest import prepare_dir


def test_makefile() -> None:
    # prepare
    PACKAGE = "test_makefile"
    package_dir = prepare_dir(PACKAGE)
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Makefile(setting, filepath).execute()
    # assert
    makefile = package_dir.joinpath("Makefile")
    assert makefile.exists()
