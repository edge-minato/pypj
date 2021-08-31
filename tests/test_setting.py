from collections import deque

import pytest
from pytest_mock import MockerFixture

from pypj.environment import Version
from pypj.setting import PypjSetting


def test_PypjSetting(mocker: MockerFixture) -> None:
    r = deque(["dummy", "Y", "999", "N", "N", "N"])

    def dummy_input() -> str:
        return r.popleft()

    mocker.patch("builtins.input", side_effect=dummy_input)
    setting = PypjSetting(python_version=Version("0.0.0"))
    with pytest.raises(SystemExit) as e:
        setting.customize()
        assert e.value.code == 0
