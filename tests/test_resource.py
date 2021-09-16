import pytest
from pytest_mock import MockerFixture

from pypj.exception import PypjError
from pypj.resource import get_my_resource


def test_resource() -> None:
    with pytest.raises(PypjError):
        _ = get_my_resource("RESOURCE_ABCDE")


def test_resource_not_found(mocker: MockerFixture) -> None:
    mocker.patch("pkgutil.get_data", return_value=None)
    with pytest.raises(PypjError):
        _ = get_my_resource("RESOURCE_ABCDE")
