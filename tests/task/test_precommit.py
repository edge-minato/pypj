from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PackageName, PypjSetting
from pypj.task import PreCommit
from tests.conftest import does_contain_specific_words, prepare_dir


def test_precommit() -> None:
    # prepare
    PACKAGE = PackageName("test_precommit")
    package_dir = prepare_dir(PACKAGE)
    precommit = package_dir.joinpath(".pre-commit-config.yaml")
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    PreCommit(setting, filepath).execute()
    # assert
    assert precommit.exists()
    assert precommit.stat().st_size > 0
    with precommit.open(mode="r") as f:
        content = f.read()
    assert not does_contain_specific_words(content)
