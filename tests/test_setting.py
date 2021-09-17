import pytest
from pytest_mock import MockerFixture

from pypj.environment import Version
from pypj.exception import PypjError
from pypj.setting import PackageName, PypjSetting
from tests.conftest import dummy_input

VER = Version("0.0.0")


def test_package_name() -> None:
    # mixed up
    assert PackageName("ABC-def_ghi") == "abc_def_ghi"
    # hyphen to underscore
    assert PackageName("a-b-c") == "a_b_c"
    # capital to lower
    assert PackageName("ABC") == "abc"
    # as it is
    assert PackageName("abc_def") == "abc_def"


def test_invalid_package_name() -> None:
    with pytest.raises(PypjError):
        PackageName("1abc")
    with pytest.raises(PypjError):
        PackageName("#abc")
    with pytest.raises(PypjError):
        PackageName("-abc")
    with pytest.raises(PypjError):
        PackageName("_abc")


def test_pypj_setting_package_name() -> None:
    assert PypjSetting(VER, PackageName("ABC-def_ghi")).package_name == "abc_def_ghi"
    assert PypjSetting(VER, PackageName("ABC")).package_name == "abc"


def test_package_dir_validation() -> None:
    # if already exists
    with pytest.raises(SystemExit) as e:
        PypjSetting(VER, PackageName("tmp"))  # tmp dir already exists
        assert e.value.code == 1  # type: ignore
    # if not already exists
    assert PypjSetting(VER, PackageName("abc123"))


def test_default(mocker: MockerFixture) -> None:
    inp = [  # try not default pattern
        "",  # max line length
        "",  # use src dir
        "",  # venv in pj
        "",  # github workflow
        "",  # vscode setting
        "",  # precommit
        "",  # Makefile
    ]

    mocker.patch("builtins.input", side_effect=dummy_input(inp))
    setting = PypjSetting(VER, PackageName("dummy_package"))
    setting.customize()
    assert setting.max_line_length == 119
    assert setting.use_src is False
    assert setting.venv_in_pj is True
    assert setting.guthub_actions is True
    assert setting.vscode is True
    assert setting.precommit is True
    assert setting.makefile is True


def test_customize(mocker: MockerFixture) -> None:
    inp = [  # try not default pattern
        "999",  # max line length
        "Y",  # use src dir
        "N",  # venv in pj
        "N",  # github workflow
        "N",  # vscode setting
        "N",  # precommit
        "N",  # Makefile
    ]

    mocker.patch("builtins.input", side_effect=dummy_input(inp))
    setting = PypjSetting(VER, PackageName("dummy_package"))
    setting.customize()
    assert setting.max_line_length == 999
    assert setting.use_src is True
    assert setting.venv_in_pj is False
    assert setting.guthub_actions is False
    assert setting.vscode is False
    assert setting.precommit is False
    assert setting.makefile is False
