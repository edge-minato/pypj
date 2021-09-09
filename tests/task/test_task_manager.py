from collections import deque
from pathlib import Path

from pytest_mock import MockFixture

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting
from pypj.task import TaskManager


def test_default() -> None:
    package_name = "dummy_package"
    setting = PypjSetting(Version("0.0.0"), package_name)
    customize = False
    pypj_file_path = PypjFilePath(Path().cwd(), setting)
    tm = TaskManager(setting, pypj_file_path, customize)
    # assert
    assert len(tm.task_list) == 5


def test_customize(mocker: MockFixture) -> None:
    user_input = deque(
        [
            "N",  # github workflow
            "N",  # vscode setting
            "N",  # Makefile
        ]
    )

    def dummy_input() -> str:
        r = user_input.popleft()
        print(r)
        return r

    package_name = "dummy_package"
    setting = PypjSetting(Version("0.0.0"), package_name)
    customize = True
    pypj_file_path = PypjFilePath(Path().cwd(), setting)
    #
    mocker.patch("builtins.input", side_effect=dummy_input)
    tm = TaskManager(setting, pypj_file_path, customize)
    assert len(tm.task_list) == 2
