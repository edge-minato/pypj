from collections import deque

import pytest
from pytest_mock import MockerFixture

from pypj.environment import Version
from pypj.setting import PypjSetting


def test_package_name_validation() -> None:
    # if already exists
    with pytest.raises(SystemExit) as e:
        PypjSetting(Version("0.0.0"), "tmp")  # tmp dir already exists
        assert e.value.code == 1  # type: ignore
    # if not already exists
    assert PypjSetting(Version("0.0.0"), "abc123")


def test_default(mocker: MockerFixture) -> None:
    r = deque(
        [  # try not default pattern
            "",  # max line length
            "",  # use src dir
            "",  # venv in pj
            "",  # github workflow
            "",  # vscode setting
            "",  # precommit
            "",  # Makefile
        ]
    )

    def dummy_input() -> str:
        return r.popleft()

    mocker.patch("builtins.input", side_effect=dummy_input)
    setting = PypjSetting(Version("0.0.0"), "dummy_package")
    setting.customize()
    assert setting.max_line_length == 119
    assert setting.use_src is False
    assert setting.venv_in_pj is True
    assert setting.guthub_actions is True
    assert setting.vscode is True
    assert setting.precommit is True
    assert setting.makefile is True


def test_customize(mocker: MockerFixture) -> None:
    r = deque(
        [  # try not default pattern
            "999",  # max line length
            "Y",  # use src dir
            "N",  # venv in pj
            "N",  # github workflow
            "N",  # vscode setting
            "N",  # precommit
            "N",  # Makefile
        ]
    )

    def dummy_input() -> str:
        return r.popleft()

    mocker.patch("builtins.input", side_effect=dummy_input)
    setting = PypjSetting(Version("0.0.0"), "dummy_package")
    setting.customize()
    assert setting.max_line_length == 999
    assert setting.use_src is True
    assert setting.venv_in_pj is False
    assert setting.guthub_actions is False
    assert setting.vscode is False
    assert setting.precommit is False
    assert setting.makefile is False
