from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PackageName, PypjSetting
from pypj.task.makefile import Makefile
from tests.conftest import does_contain_specific_words, prepare_dir


def test_makefile() -> None:
    # prepare
    PACKAGE = PackageName("test_makefile")
    package_dir = prepare_dir(PACKAGE)
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    setting.set_replace_words()
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Makefile(setting, filepath).execute()
    # assert
    makefile = package_dir.joinpath("Makefile")
    assert makefile.exists()
    with makefile.open(mode="r") as f:
        content = f.read()
    assert "pre-commit" in content
    assert PACKAGE in content
    assert "PACKAGE_SRC_DIR" not in content
    assert not does_contain_specific_words(content)


def test_makefile_wo_precommit() -> None:
    # prepare
    PACKAGE = PackageName("test_makefile_wo_precommit")
    package_dir = prepare_dir(PACKAGE)
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    setting.precommit = False
    setting.set_replace_words()
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Makefile(setting, filepath).execute()
    # assert
    makefile = package_dir.joinpath("Makefile")
    assert makefile.exists()
    with makefile.open(mode="r") as f:
        content = f.read()
    assert "pre-commit" not in content
    assert PACKAGE in content
    assert "PACKAGE_SRC_DIR" not in content
    assert not does_contain_specific_words(content)
