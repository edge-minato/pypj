import json
import re
from pathlib import Path
from shutil import rmtree
from subprocess import PIPE, run
from typing import Generator

import pytest
import toml  # type: ignore
import yaml  # type: ignore


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


def prepare_dir(dir_name: str) -> Path:
    package_dir = Path("tmp").joinpath(dir_name)
    package_dir.mkdir()  # mkdir ./tmp/dirname
    return package_dir


def validate_jsonc(file_path: Path) -> bool:
    try:
        with file_path.open(mode="r") as f:
            text = f.read()
        # delete comments
        re_text = re.sub(r"/\*[\s\S]*?\*/|//.*", "", text)
        json.loads(re_text)
        return True
    except Exception:
        return False


def validate_yaml(file_path: Path) -> bool:
    try:
        with file_path.open(mode="r") as f:
            yaml.safe_load(f)
        return True
    except Exception:
        return False


def validate_toml(file_path: Path) -> bool:
    try:
        with file_path.open(mode="r") as f:
            toml.load(f)
        return True
    except Exception:
        return False


class DummyReturn:
    def __init__(self, returncode: int) -> None:
        self.returncode: int = returncode


def dummy_command(cmd: str) -> DummyReturn:
    if "poetry new" in cmd:
        r = run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        return DummyReturn(r.returncode)
    else:
        return DummyReturn(0)
