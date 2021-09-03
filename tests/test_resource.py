import pytest

from pypj.exception import PypjError
from pypj.resource import get_my_resource


def test_resource() -> None:
    with pytest.raises(PypjError):
        _ = get_my_resource("RESOURCE_ABCDE")
