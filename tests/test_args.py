import pytest
from pytest_mock import MockFixture

from pypj.args import args


def test_args(mocker: MockFixture) -> None:
    class MockArgParser:
        def __init__(self) -> None:
            self.version = True

    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser())
    with pytest.raises(SystemExit) as e:
        args()
    assert e.value.code == 0  # type: ignore
