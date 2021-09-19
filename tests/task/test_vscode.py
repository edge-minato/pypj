from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PackageName, PypjSetting
from pypj.task.vscode import Vscode
from tests.conftest import does_contain_specific_words, prepare_dir, validate_jsonc


def test_vscode() -> None:
    # prepare
    PACKAGE = PackageName("test_vscode")
    package_dir = prepare_dir(PACKAGE)
    vscode_dir = package_dir.joinpath(".vscode")
    vscode_setting = vscode_dir.joinpath("settings.json")
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Vscode(setting, filepath).execute()
    # assert
    assert vscode_dir.is_dir()
    assert vscode_setting.exists()
    assert validate_jsonc(vscode_setting)
    with vscode_setting.open(mode="r") as f:
        content = f.read()
    assert not does_contain_specific_words(content)
