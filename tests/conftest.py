from pathlib import Path
from shutil import rmtree
from typing import Generator

import pytest


def prepare_tmp_dir(tmp: Path) -> None:
    if tmp.exists():
        rmtree(tmp)
    tmp.mkdir()


def remove_tmp_dir(tmp: Path) -> None:
    rmtree(tmp)


@pytest.fixture(scope="session", autouse=True)
def scope_session() -> Generator:
    print("setup before session")
    tmp = Path("tmp").resolve()
    prepare_tmp_dir(tmp)
    yield
    remove_tmp_dir(tmp)
    print("teardown after session")
