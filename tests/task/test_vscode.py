from pathlib import Path

from pytest_mock import MockFixture

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task.vscode import Vscode
from tests.conftest import prepare_dir, validate_jsonc


def test_readme(mocker: MockFixture) -> None:
    # prepare
    PACKAGE = "test_vscode"
    package_dir = prepare_dir(PACKAGE)
    vscode_dir = package_dir.joinpath(".vscode")
    vscode_setting = vscode_dir.joinpath("settings.json")
    # execute
    mocker.patch("builtins.input", return_value=PACKAGE)
    setting = PypjSetting(Version("0.0.0"))
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    Vscode(setting, filepath).execute()
    # assert
    assert vscode_dir.is_dir()
    assert vscode_setting.exists()
    assert validate_jsonc(vscode_setting)
