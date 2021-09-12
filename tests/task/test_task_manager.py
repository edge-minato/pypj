from pathlib import Path

from pytest_mock import MockFixture

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task import TaskManager


def test_default() -> None:
    package_name = "dummy_package"
    setting = PypjSetting(Version("0.0.0"), package_name)
    pypj_file_path = PypjFilePath(Path().cwd(), setting)
    tm = TaskManager(setting, pypj_file_path)
    # assert
    assert len(tm.task_list) == 6


def test_customize(mocker: MockFixture) -> None:

    package_name = "dummy_package"
    setting = PypjSetting(Version("0.0.0"), package_name)
    setting.guthub_actions = False
    setting.vscode = False
    setting.precommit = False
    setting.makefile = False
    pypj_file_path = PypjFilePath(Path().cwd(), setting)
    #
    tm = TaskManager(setting, pypj_file_path)
    assert len(tm.task_list) == 2
